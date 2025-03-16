#dog class that is init with name and breed

class Dog:
    
    all = []
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.all.append(self)



fido = Dog("fido")
print(fido)    
fido.name = "Mark"
