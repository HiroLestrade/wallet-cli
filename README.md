# wallet-cli
wallet-cli is a command-line interface to manage personal finances manually through accounts, incomes, and periodic services, saving the data directly in a JSON file.
'''json
{
    "accounts": []
    "incomes": []
    "bills": []
    "services": []
}
'''
Each field consists of an array that collects the registers with their own proper fields that determine the parameters of the CLI commands.
## Installation
The project is written in Python and uses the click package to implement the cli functionality, to install it, run in terminal:
'''bash
pip install click
'''
Then, clone the repository with:
'''bash
git clone https://github.com/HiroLestrade/wallet-cli.git
'''
Move to the folder:
'''bash
cd wallet-cli
'''
And add a new account to create the JSON file, e.g.:
'''bash
python wallet-cli.py new-account --account Card --atype credit --amount 7500 --limit 1000
'''
## Functionality
### new-account
Allows adding a new account for cash, voucher, credit, debit, or departmental purposes. It requires the account name, the amount (free amount in the case of credit or departmental accounts), the account type, and an optional limit (again, for credit or departmental accounts).
### read-data
A generic command with a field parameter that allows exploring the registers in the data file.
### add-bill
Allows adding a bill register, charging the amount to the corresponding account. The command requires the bill amount, the date, a detail about it, and the account to properly record the charge.
### remove-bill
Allows removing a bill register, discharging the amount from the corresponding account. The command only needs the ID of the register, which can be obtained with the command read-data. After removal, the command reassigns the IDs of the field.

##To do
[] add-income
[] remove-income
[] add-service
[] remove-service
[] charge-service
[] extend the functionality of read-data for services
[] add filter features to read-data
[] create an abbreviated script

---
This project is inspired by the following tutorial by Fazt:
![Python Click Tutorial](https://github.com/fazt/python-click-tutorial/blob/master/cli.py)
