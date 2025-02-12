class BankAccount:
    def __init__(self,name,age,gender,id_no,bank_branch,amount_in_bank,withdrawal_or_deposit,amount_withdrawn,amount_deposited):
        self.name = name
        self.age = age
        self.gender = gender
        self.id_no = id_no
        self.bank_branch = bank_branch
        self.amount_in_bank = amount_in_bank
        self.withdrawal_or_deposit = withdrawal_or_deposit
        self.amount_withdrawn = amount_withdrawn
        self.amount_deposited = amount_deposited
    def deposit(self):
        self.amount_in_bank = self.amount_in_bank + self.amount_deposited
        return self.amount_in_bank
    def withdraw(self):
        self.amount_in_bank = self.amount_in_bank - self.amount_withdrawn
        return self.amount_in_bank
    def bank_fees(self):
        bank_fees = self.amount_in_bank*0.05
        return self.amount_in_bank
    def display(self):
        return f"Name: {self.name} ,Amount_in_bank: {self.amount_in_bank}"


