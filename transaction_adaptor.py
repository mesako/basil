
import csv
import string
import datetime
import re
from decimal import Decimal
from transaction import Transaction

def discover_adaptor(file_path : str):
    '''
    Discover
    export as CSV file
    Trans. Date, Post Date, Description, Amount, Category
    '''
    transaction_list = []
    with open(file_path) as discover_csv:
        discover_data = list(csv.DictReader(discover_csv))
    
    for row in discover_data:
        transaction_list.append(make_transaction_from_discover(row))
    return transaction_list

def make_transaction_from_discover(discover_transaction):
    date = datetime.datetime.strptime(discover_transaction["Trans. Date"], "%m/%d/%Y").date()
    amount = change_amount(discover_transaction["Amount"])
    merchant = clean_merchant_name(discover_transaction["Description"])
    transaction_object = Transaction(date = date, amount = amount, merchant = merchant)
    return transaction_object

def change_amount(amount : str):
    correct_amount = Decimal(amount)
    return correct_amount

def clean_merchant_name(merchant : str):
    regex = re.compile('[^a-zA-Z -]')
    clean_merchant = regex.sub('', merchant).title()
    return clean_merchant

def barclay_adaptor(file_path : str):
    '''
    BarclayCard
    export as CSV file
    header with Barclays Bank Delaware, Account number (last four digits), Account Balance as of DATE: AMOUNT
    Transaction Date, Description, Amount, Category (DEBIT OR CREDIT)
    '''
    transaction_list = []
    with open(file_path) as barclay_csv:
        barclay_data = list(csv.DictReader(barclay_csv, fieldnames = ["Transaction Date", "Description",
        "Category", "Amount"]))
    
    for row in barclay_data:
        for k, v in row.items():
            if None in [k, v] or k == v:
                break
        else:
            transaction_list.append(make_transaction_from_barclay(row))
    return transaction_list

def make_transaction_from_barclay(barclay_transaction):
    date = datetime.datetime.strptime(barclay_transaction["Transaction Date"], "%m/%d/%Y").date()
    amount = -change_amount(barclay_transaction["Amount"])
    merchant = clean_merchant_name(barclay_transaction["Description"])
    transaction_object = Transaction(date = date, amount = amount, merchant = merchant)
    return transaction_object


def chase_adaptor(file_path : str):
    '''
    Chase
    export as CSV file
    Type, Trans Date, Post Date, Description, Amount, Category, Memo
    '''
    transaction_list = []
    with open(file_path) as chase_csv:
        chase_data = list(csv.DictReader(chase_csv))
    
    for row in chase_data:
        transaction_list.append(make_transaction_from_chase(row))
    return transaction_list

def make_transaction_from_chase(chase_transaction):
    date = datetime.datetime.strptime(chase_transaction["Trans Date"], "%m/%d/%Y").date()
    amount = -change_amount(chase_transaction["Amount"])
    merchant = clean_merchant_name(chase_transaction["Description"])
    transaction_object = Transaction(date = date, amount = amount, merchant = merchant)
    return transaction_object
