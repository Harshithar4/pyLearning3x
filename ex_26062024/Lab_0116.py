class Person:
    name=None
    age=None

    def talk(self):
        print("Talking...")
    def walk(self):
        print("Walking...")

person=Person()
print(person.name)#None
person.name="Ganishka"
print(person.name)#Ganishka
person.walk()

person2=Person()
print(person2.name)
person2.name="Amit"
print(person2.name)
person2.talk()