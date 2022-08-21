class BankAccount:
    name_bank = 'Future Bank'
    def __init__(self, interest_rate=0.01, balance=100):
        self.interest_rate= interest_rate                                                      
        self.balance = balance
        

    def deposit(self, amount):
        self.balance += amount
        return self

    def whithdrawal(self, amount):
        if amount > self.balance:
            self.balance - 5
            print('insuficient fund: charging a 5$ fee')
        else:
            self.balance -= amount
        return self

    def show_account_information(self):
        print(f'Account balance:  {self.balance} \nInteres: {self.interest_rate}')
        return self

    def generate_interes(self):
        rate = self.balance * self.interest_rate
        print(f'interes:  {rate}')
        self.balance = self.balance + rate
        return self
            

account1 = BankAccount()
account1.deposit(500).deposit(500).deposit(6000).whithdrawal(100).generate_interes().show_account_information()


account2 = BankAccount(0.025, 10)

account2.deposit(500).deposit(500).whithdrawal(100).whithdrawal(100).whithdrawal(100).whithdrawal(100).generate_interes().show_account_information()


