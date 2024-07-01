class Person:
    name = None
    id = None

    def __init__(self):  # Default constructor
        print("Hello World!")

    def __init__(self, name, id):#parameterized constructor
        self.name = name
        self.id = id

person=Person("Gani","2")
person1=Person("Amit","4")
print(f"{person.name}, {person.id}")
print(f"{person1.name}, {person1.id}")