import json_manager
import click

@click.group()
def wallet_cli():
    pass

@wallet_cli.command()
@click.option('--account', required=True, help='Name account')
@click.option('--atype', required=True, help='Account type: cash, credit, debit or departamental')
@click.option('--amount', required=True, help='Available money')
@click.option('--limit', help='Limit in case of credit or departamental')
@click.pass_context
def new_account(ctx, account, atype, amount, limit):
    if not account or not atype or not amount:
        ctx.fail('Account, atype and amount are required')
    else:
        data = json_manager.read_json()
        new_id = len(data['accounts']) + 1
        new_reg = {'id':new_id, 'account':account, 'type':atype, 'amount': amount, 'limit':limit}
        data['accounts'].append(new_reg)
        json_manager.write_json(data)
        print(f"new account created with id {new_id}")

if __name__ == '__main__':
    wallet_cli()