


class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0



    def hacer_deposito(self, amount):
        self.balance_cuenta += amount

    def balance_usuario(self, amount):
        self.balance_cuenta = amount
    
    def retiro(self, amount):
        if amount >self.balance_cuenta:
            print('Sobregiro, no se puede hacer retiro.')
        else:
            self.balance_cuenta -= amount
        return self

    def transferir_dinero(self, name, amount):
        self.retiro(amount)
        name.hacer_depositoposito(amount)
        return self 
    



Carlos = Usuario('Carlos', "cmrivas20@gmail.com")
Ally = Usuario('ally', 'ally@gmail.com')
Pedro = Usuario('Pedro', 'pedro@gmail.com')
