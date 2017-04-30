import numpy as np
import pandas as pd
from operator import attrgetter, methodcaller

COLUMNS = ["date", "merchant", "amount", "description", "category"]

def convert_transaction_list_to_matrix(transaction_list):
    transaction_matrix = np.matrix(list(map(attrgetter(COLUMNS), transaction_list)))
    return transaction_matrix

def convert_transaction_matrix_to_df(transaction_matrix):
    transaction_df = pd.DataFrame(data = transaction_matrix[:,:], columns = list(map(methodcaller("title"), COLUMNS)))
    return transaction_df

def convert_transaction_list_to_df(transaction_list):
    transaction_matrix = convert_transaction_list_to_matrix(transaction_list)
    transaction_df = convert_transaction_matrix_to_df(transaction_matrix)
    return transaction_df
