class Person:
    def __init__(self):
        self.name=str(input("Enter your name: "))
        self.id=int(input("Enter your id: "))

    def display(self):
        print(f'{self.name},{self.id}')


person=Person()
person.display()