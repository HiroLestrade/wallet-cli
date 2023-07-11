import json_manager
import click


@click.group()
def wallet_cli():
    pass


@wallet_cli.command()
@click.option('--account',  required=True, help='Name account')
@click.option('--atype',    required=True, help='Account type: cash, credit, debit or departamental')
@click.option('--amount',   required=True, help='Available money')
@click.option('--limit',                   help='Limit in case of credit or departamental')
@click.pass_context
def new_account(ctx, account, atype, amount, limit):
    if not account or not atype or not amount:
        ctx.fail('Account, atype and amount are required')
    data = json_manager.read_json()
    new_id = len(data['accounts']) + 1
        
    new_reg = {'id': new_id, 'account': account, 'type': atype, 'amount': float(amount), 'limit': float(limit)} if limit != None else {'id': new_id, 'account': account, 'type': atype, 'amount': float(amount), 'limit': limit}

    data['accounts'].append(new_reg)
    json_manager.write_json(data)
    print(f"new account created with id {new_id}")


@wallet_cli.command()
@click.option('--amount', required=True, help='Amount of the bill')
@click.option('--date', required=True, help='Date of the bill')
@click.option('--detail', required=True, help='Detail of the bill')
@click.option('--account', required=True, help='Account target')
@click.pass_context
def add_bill(ctx, amount, date, detail, account):
    if not amount or not date or not detail or not account:
        ctx.fail('Amount, date, detail and account are required')
    data = json_manager.read_json()
    new_id = len(data['bills']) + 1
    new_reg = {'id': new_id, 'amount': float(amount), 'date': date, 'detail': detail, 'account': account}
# *******charge the amount in the account*********************************************
    for element in data['accounts']:
        if element['account'] == account:
            element['amount'] -= float(amount)
# ************************************************************************************
    data['bills'].append(new_reg)
    json_manager.write_json(data)
    print(f"new bill added with id {new_id} to account {account}")


@wallet_cli.command()
@click.option('--id', required=True, help='Id of bill to remove')
@click.pass_context
def remove_bill(ctx, id):
    if not id:
        ctx.fail('Id is required')
    data = json_manager.read_json()
    bills = data['bills']
    bill = next((x for x in bills if x['id'] == int(id)), None)
    if bill is None:
        print('Bill not found')
        return
# *******discharge the amount in the account*******************************************
    for element in data['accounts']:
        if element['account'] == bill['account']:
            element['amount'] += float(bill['amount'])
# ************************************************************************************
    data['bills'].remove(bill)
    json_manager.write_json(data)
    print(f"remove bill {id} success")
    reasign_ids(data, 'bills')


@wallet_cli.command()
@click.option('--field', required=True, help='accounts, bills or services')
@click.pass_context
def read_data(ctx, field):
    if not field:
        ctx.fail('Field is required')
    data = json_manager.read_json()
    regs = data[field]
    for element in regs:
        if field == 'accounts':
            print(f"{element['id']} - {element['account']} - {element['type']} - {element['amount']} - {element['limit']}")
        elif field == 'bills':
            print(
                f"{element['id']} - {element['amount']} - {element['date']} - {element['detail']} - {element['account']}")
        # TODO: add services

def reasign_ids(data, field):
    data_length = len(data[field])
    for i in range(data_length):
        data[field][i]['id'] = i + 1
    json_manager.write_json(data)

if __name__ == '__main__':
    wallet_cli()
