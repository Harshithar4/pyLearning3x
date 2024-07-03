class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a* self.b




calc=Calc(3,4)
print(calc.sum())
calc1=Calc(4,5)
print(calc1.mul())