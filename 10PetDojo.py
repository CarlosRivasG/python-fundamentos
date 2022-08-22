class ninja:
    def __init__(self, name, surname, pet, reward, pet_food):
        self.name= name
        self.surname= surname
        self.pet= pet
        self.reward= reward
        self.pet_food= pet_food

    def to_walk(self):
        print('Esta caminando')
        self.pet.play()
        return self

    def feed(self):
        print('Esta comiendo')
        self.pet.eat()
        return self

    def wash(self):
        print('Se esta bañando')
        self.pet.sound()
        return self

    def __repr__(self):
        return f'----\nname:{self.name}\npet:{self.pet}\npet_food:{self.pet_food} '




class pet:
    def __init__(self, name, type_pet, candy):
        self.name =name
        self.type_pet = type_pet
        self.candy = candy
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy = self.energy + 25
        return self

    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        return self

    def play(self):
        self.health = self.health + 5
        return self

    def sound(self):
        print('¡GUAU! ¡GUAU!')
        return self
    
    def __repr__(self):
        return f'----\nname:{self.name}\nEnergy:{self.energy}\nHealth:{self.health} '



perro = pet('azzy', 'perro', 'croquette')
carlos = ninja('carlos', 'rivas', perro, 'croquette', 'meat')
print(carlos)
carlos.feed().to_walk().wash()

#perro.sound().play().eat().sleep()
#print(perro)