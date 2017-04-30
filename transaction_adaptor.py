
import csv
import string
import datetime

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
    date = change_date(discover_transaction["Trans. Date"])
    amount = change_amount(discover_transaction["Amount"])
    merchant = change_merchant(discover_transaction["Description"])
    transaction_object = Transaction(date = date, amount = amount, merchant = merchant)
    return transaction_object

def change_date(trans_date : str):
    correct_date = trans_date.split(sep = "/")
    correct_date = list(map(int, correct_date))
    correct_date = month_day_year_to_date(*correct_date)
    return correct_date

def month_day_year_to_date(month, day, year):
    return date(year, month, day)

def change_amount(amount : str):
    correct_amount = float(amount)
    return correct_amount

def change_merchant(merchant : str):
    regex = re.compile('[^a-zA-Z -]')
    correct_merchant = regex.sub('', merchant).title()
    return correct_merchant


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
    date = change_date(barclay_transaction["Transaction Date"])
    amount = -change_amount(barclay_transaction["Amount"])
    merchant = change_merchant(barclay_transaction["Description"])
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
    date = change_date(chase_transaction["Trans Date"])
    amount = -change_amount(chase_transaction["Amount"])
    merchant = change_merchant(chase_transaction["Description"])
    transaction_object = Transaction(date = date, amount = amount, merchant = merchant)
    return transaction_object
