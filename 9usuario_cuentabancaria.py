from bank import BankAccount

class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = BankAccount(interest_rate=0.02, balance=0)



    def hacer_deposito(self, amount):
        self.cuenta += amount
        return self

    def balance_usuario(self):
        print('uruario: ', self.name)
        print('Balance:', self.cuenta)
        return self

    
    def retiro(self, amount):
        if amount > self.cuenta:
            print('Sobregiro, no se puede hacer retiro.')
        else:
            self.cuenta -= amount
        return self

    def transferir_dinero(self, usuario_destino, amount):
        if amount > self.cuenta:
            print('sobregiro, no se  puede transferir')
        else:
            self.cuenta -= amount

        usuario_destino.cuenta += amount

    


"""
carlos = Usuario('Carlos', "cmrivas20@gmail.com", )

carlos.hacer_deposito(100).hacer_deposito(200).hacer_deposito(200).retiro(200)
print(carlos.name, 'Balance Bancario: ', carlos.cuenta)

Ally = Usuario('ally', 'ally@gmail.com')
Ally.hacer_deposito(100).hacer_deposito(100).retiro(25).retiro(15)
print(Ally.name, 'Balance Bancario: ', Ally.cuenta)

Pedro = Usuario('Pedro', 'pedro@gmail.com')
Pedro.hacer_deposito(1200).retiro(100).retiro(10).retiro(50)
print(Pedro.name, 'Balance Bancario: ', Pedro.cuenta)
"""