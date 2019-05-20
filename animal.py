class Animal (object):
    def __init__(self):
        self.years = 0
        self.name = None

    def getAge(self):
        return self.years

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def setAge (self, newAge):
        self.years = newAge
    
class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid)

    def get_parent1(self):
        return self.parent1
    
    def get_parent2(self):
        return self.parent2

    def get_parents (self):
      Name = print(self.parent1.getName(),' ', self.parent2.getName())
      
        
    
Bobby = Rabbit(8)
Bobby.setName('Bobby')
Angela = Rabbit(7)
Angela.setName('Angela')
print(Bobby.get_rid())
jane = Rabbit(5, Angela, Bobby)
print(jane.get_parents())

