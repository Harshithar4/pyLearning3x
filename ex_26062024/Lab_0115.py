class Person:
    name=None
    age=None
    address=None

    def talk(self):# No Argument and no return type
        print("Talking..")
    def walk(self,name):#Argument with no return type
        print("Walking...")
        self.name=name

    def sleep(self,name):# argument with return type
        self.name=name
        return "I am sleeping"

    def eat(self):# No argument with return type
        print("Eating")
        return "I am eating"

person=Person()
person.eat()
