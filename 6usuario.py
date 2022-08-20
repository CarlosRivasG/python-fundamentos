


class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta =  0



    def hacer_deposito(self, amount):
        self.balance_cuenta += amount

    def balance_usuario(self):
        print('uruario: ', self.name)
        print('Balance:', self.balance_cuenta)

    
    def retiro(self, amount):
        if amount > self.balance_cuenta:
            print('Sobregiro, no se puede hacer retiro.')
        else:
            self.balance_cuenta -= amount
        return self

    def transferir_dinero(self, usuario_destino, amount):
        if amount > self.balance_cuenta:
            print('sobregiro, no se  puede transferir')
        else:
            self.balance_cuenta -= amount

        usuario_destino.balance_cuenta += amount

    



carlos = Usuario('Carlos', "cmrivas20@gmail.com")

carlos.hacer_deposito(100)
carlos.hacer_deposito(200)
carlos.hacer_deposito(200)
carlos.retiro(200)
print(carlos.name, 'Balance Bancario: ', carlos.balance_cuenta)

Ally = Usuario('ally', 'ally@gmail.com')
Ally.hacer_deposito(100)
Ally.hacer_deposito(100)
Ally.retiro(25)
Ally.retiro(15)
print(Ally.name, 'Balance Bancario: ', Ally.balance_cuenta)

Pedro = Usuario('Pedro', 'pedro@gmail.com')
Pedro.hacer_deposito(1200)
Pedro.retiro(100)
Pedro.retiro(10)
Pedro.retiro(50)
print(Pedro.name, 'Balance Bancario: ', Pedro.balance_cuenta)