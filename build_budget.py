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
    filter_df = transaction_df.loc[keep_ind]
    return filter_df

def summary_stats_category_expenses_from_df(transaction_df, categories : list, date_window : tuple = None, amount_window : tuple = (0, None)):
    filter_df = transaction_df.copy()
    if date_window is not None:
        filter_df = filter_df_by_date_window(filter_df, date_window[0], date_window[1])
    if amount_window is not None:
        filter_df = filter_df_by_amount_window(filter_df, amount_window[0], amount_window[1])
    
    abs_total_spent = filter_df["Amount"].sum()
    filter_df = filter_df_by_categories(filter_df, categories)
    categories_sums = get_sums_by_categories(filter_df, categories)
    categories_percents = get_relative_percents_by_categories(filter_df, categories)
    categories_abs_percents = get_absolute_percents_by_categories(filter_df, abs_total_spent, categories)
    categories_results = {"Sum": categories_sums, "Relative Percent": categories_percents, "Percent" : categories_abs_percents}
    summary_stats_df = pd.DataFrame(categories_results)
    return summary_stats_df

def get_sums_by_categories(pre_filtered_transaction_df, categories : list):
    sums = []
    for category in categories:
        temp_df = filter_df_by_categories(pre_filtered_transaction_df, [category])
        sums.append(temp_df["Amount"].sum())
    categories_sums = pd.Series(sums, index = categories)
    return(categories_sums)

def get_relative_percents_by_categories(pre_filtered_transaction_df, categories : list):
    percents = []
    total_spent = pre_filtered_transaction_df["Amount"].sum()
    for category in categories:
        temp_df = filter_df_by_categories(pre_filtered_transaction_df, [category])
        percents.append(round(temp_df["Amount"].sum() / total_spent, 2))
    categories_percents = pd.Series(percents, index = categories)
    return(categories_percents)
    
def get_absolute_percents_by_categories(pre_filtered_transaction_df, abs_total_spent : Decimal, categories : list):
    abs_percents = []
    for category in categories:
        temp_df = filter_df_by_categories(pre_filtered_transaction_df, [category])
        abs_percents.append(round(temp_df["Amount"].sum() / abs_total_spent, 2))
    categories_abs_percents = pd.Series(abs_percents, index = categories)
    return(categories_abs_percents)
