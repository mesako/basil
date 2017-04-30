from math import inf
from decimal import Decimal
import datetime
import re

def filter_df_by_date_window(transaction_df, start_date : datetime.date = None, end_date : datetime.date = None):
    if start_date is None:
        start_date = datetime.date(datetime.MINYEAR, 1, 1)
    if end_date is None:
        end_date = datetime.date(datetime.MAXYEAR, 12, 31)
    filter_df = transaction_df[transaction_df["Date"] >= start_date]
    filter_df = filter_df[filter_df["Date"] <= end_date]
    return filter_df

def filter_df_by_amount_window(transaction_df, low_amount : Decimal = None, high_amount : Decimal = None):
    if low_amount is None:
        low_amount = -math.inf
    if high_amount is None:
        high_amount = math.inf
    filter_df = transaction_df[transaction_df["Amount"] >= low_amount]
    filter_df = filter_df[filter_df["Amount"] <= high_amount]
    return filter_df

def filter_df_by_categories(transaction_df, categories : list):
    keep_ind = []
    for category in categories:
        bool_col = transaction_df["Category"].str.contains(category, na = False)
        keep_ind = keep_ind + bool_col[bool_col == True].index.tolist()
    filter_df = transaction_df.iloc[keep_ind]
    return filter_df
