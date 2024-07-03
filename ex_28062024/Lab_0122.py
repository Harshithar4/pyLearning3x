class Car:

    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year

    def engine(self):
        print("Car name is --> ",self.name)
        print("Car model is --> ",self.model)
        print("Car Manufactured year--> ",self.year)

car=Car("Ritz","VDI","2017")
car.engine()
car1=Car("Swift","ZDI","2020")
car1.engine()