import json_manager
import click

@click.group()
def wallet_cli():
    pass

@cli.command()
@click.option('--account', requred=True, help='Name account')
@click.option('--type', required=True, help='Cash, credit, debit or departamental')
@click.option('--amount', require=True, help='Available money')
@clicl.option('--limit', help='Limit in case of credit or departamental')
@click.pass_context
def new_account(ctx, account, atype, amount, limit):
    if not account or not atype or not amount:
        ctx.fail('Account, type and amount are required')
    else:
        data = json_manager.read_json()
        new_id = len(data) + 1
        new_reg = {'id':new_id, 'account':account, 'type':atype, 'amount': amount, 'limit':limit}
        data['accounts'].append(new_reg)
        json_manager.write_json(data)
        print(f"new account created with id {new_id}")