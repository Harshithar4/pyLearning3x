class Person:
    name=None
    age=None
    address= None

    def talk(self):
        print("Talking...")

    def walk(self):
        print("Walking..")

person=Person()
person.name="gani"
print(person.name)
person.talk()
person.walk()