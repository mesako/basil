import numpy

def convert_transaction_list_to_matrix(transaction_list):
    date_vec = []
    merchant_vec = []
    amount_vec = []
    desc_vec = []
    category_vec = []
    for t in transaction_list:
        print(t)
        date_vec.append(t.date)
        merchant_vec.append(t.merchant)
        amount_vec.append(t.amount)
        desc_vec.append(t.description)
        category_vec.append(t.category)
    
    transaction_matrix = numpy.matrix([date_vec, merchant_vec, amount_vec, desc_vec, category_vec])
    transaction_matrix = transaction_matrix.T
    return(transaction_matrix)
