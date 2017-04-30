import numpy
import pandas as pd

def convert_transaction_list_to_matrix(transaction_list):
    date_vec = []
    merchant_vec = []
    amount_vec = []
    desc_vec = []
    category_vec = []
    for t in transaction_list:
        date_vec.append(t.date)
        merchant_vec.append(t.merchant)
        amount_vec.append(t.amount)
        desc_vec.append(t.description)
        category_vec.append(t.category)
    
    transaction_matrix = numpy.matrix([date_vec, merchant_vec, amount_vec, desc_vec, category_vec])
    transaction_matrix = transaction_matrix.T
    return(transaction_matrix)

def convert_transaction_matrix_to_df(transaction_matrix):
    transaction_df = pd.DataFrame(data = transaction_matrix[:,:], columns = ["Date", "Merchant", "Amount", "Description", "Category"])
    return(transaction_df)

def convert_transaction_list_to_df(transaction_list):
    transaction_matrix = convert_transaction_list_to_matrix(transaction_list)
    transaction_df = convert_transaction_matrix_to_df(transaction_matrix)
    return(transaction_df)

