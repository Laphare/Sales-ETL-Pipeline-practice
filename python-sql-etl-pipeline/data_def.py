"""
data_def class
"""
class Rec:
    def __init__(self,date,id,amount,country):
        self.date = date
        self.id = id
        self.amount = amount
        self.country = country
    def __str__(self):
        return f'{self.date} {self.id} {self.amount} {self.country}'