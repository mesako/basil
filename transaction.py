from datetime import date

class Transaction:
    """A simple example class"""
    def __init__(self, date : date, merchant : str, amount : float, description = None, category = None):
        self.date = date
        self.merchant = merchant
        self.amount = amount
        self.description = description
        self.category = category
        
    def __repr__(self):
        return f"<Transaction for ${self.amount} at {self.merchant} on {self.date}>"






