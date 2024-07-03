class Dog:
    name=None
    id=None

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def sleeping(self):
        print("who is sleeping-->"+self.name)

dog1=Dog("chow",1)
dog2=Dog("Mow",2)
print(dog1.name,dog1.id)
dog1.sleeping()
dog2.sleeping()