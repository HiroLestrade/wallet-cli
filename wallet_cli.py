import json_manager
import click


@click.group()
def wallet_cli():
    pass


@wallet_cli.command()
@click.option('--account', required=True, help='Name account')
@click.option('--atype', required=True, help='Account type: cash, credit, voucher, debit or departamental')
@click.option('--amount', required=True, type=float, help='Available money')
@click.option('--limit', type=float, help='Limit in case of credit or departamental')
def new_account(account, atype, amount, limit):
    data = json_manager.read_json()

    new_id = len(data['accounts']) + 1
    new_reg = {'id': new_id, 'account': account,
               'type': atype, 'amount': amount, 'limit': limit}
    data['accounts'].append(new_reg)

    json_manager.write_json(data)
    print(f"new account created with id {new_id}")


@wallet_cli.command()
@click.option('--amount', required=True, type=float, help='Amount of the bill')
@click.option('--date', required=True, help='Date of the bill')
@click.option('--detail', required=True, help='Detail of the bill')
@click.option('--account', required=True, help='Account target')
def add_bill(amount, date, detail, account):
    data = json_manager.read_json()

    new_id = len(data['bills']) + 1
    new_reg = {'id': new_id, 'amount': amount,
               'date': date, 'detail': detail, 'account': account}
    for element in data['accounts']:
        if element['account'] == account:
            element['amount'] -= amount
    data['bills'].append(new_reg)

    json_manager.write_json(data)
    print(f"new bill added with id {new_id} to account {account}")


@wallet_cli.command()
@click.option('--id', required=True, type=int, help='Id of bill to remove')
def remove_bill(id):
    data = json_manager.read_json()

    bills = data['bills']
    bill = next((x for x in bills if x['id'] == id), None)
    if bill is None:
        print('Bill not found')
        return
    for element in data['accounts']:
        if element['account'] == bill['account']:
            element['amount'] += bill['amount']
    data['bills'].remove(bill)
    data = reasign_ids(data, 'bills')

    json_manager.write_json(data)
    print(f"remove bill {id} success")


@wallet_cli.command()
@click.pass_context
def add_income():
    pass


@wallet_cli.command()
@click.option('--field', required=True, help='accounts, bills or services')
def read_data(field):
    data = json_manager.read_json()
    regs = data[field]

    for element in regs:
        if field == 'accounts':
            print(
                f"{element['id']} - {element['account']} - {element['type']} - {element['amount']} - {element['limit']}")
        elif field == 'bills':
            print(
                f"{element['id']} - {element['amount']} - {element['date']} - {element['detail']} - {element['account']}")
        # TODO: add services


@wallet_cli.command()
@click.option('--amount', required=True, help='Amount to transfer')
@click.option('--origin', required=True, help='Account from')
@click.option('--destination', required=True, help='Account to')
def transfer(amount, origin, destination):
    data = json_manager.read_json()
    accounts = data['accounts']

    for account in accounts:
        if account['account'] == origin:
            account['amount'] -= float(amount)
        if account['account'] == destination:
            account['amount'] += float(amount)
    json_manager.write_json(data)
    print(
        f"Amount {amount} removed from {origin} and added to {destination} success")


@wallet_cli.command()
@click.option('--amount', required=True, type=float, help='Amount of the income')
@click.option('--date', required=True, help='Date of the income')
@click.option('--detail', required=True, help='Detail of the income')
@click.option('--account', required=True, help='Account target')
def add_income(amount, date, detail, account):
    data = json_manager.read_json()

    new_id = len(data['incomes'])
    new_reg = {'id': new_id, 'amount': amount, 'date': date, 'detail': detail, 'account':account}
    for element in data['accounts']:
        if element['account'] == account:
            pass
            element['amount'] += amount
    data['incomes'].append(new_reg)

    json_manager.write_json(data)
    print(f"new income added with id {new_id} to account {account}")

@wallet_cli.command()
@click.option('--id', required=True, type=int, help='Id of income to remove')
def remove_income(id):
    data = json_manager.read_json()

    incomes = data['incomes']
    income = next((x for x in incomes if x['id'] == id), None)
    if income is None:
        print('Income not found')
        return
    for element in data['accounts']:
        if element['account'] == income['account']:
            element['amount'] -= income['amount']
    data['incomes'].remove(income)
    data = reasign_ids(data, 'incomes')

    json_manager.write_json(data)
    print(f"remove income {id} success")


def reasign_ids(data, field):
    data_length = len(data[field])
    for i in range(data_length):
        data[field][i]['id'] += 1
    return data


if __name__ == '__main__':
    wallet_cli()
