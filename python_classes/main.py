# Classes in python, basic

class Addition():
    #Member variables
    __a = 0
    __b = 0
    sum = 0
    #constructor
    def __init__(self,a,b):
        self.a = a
        self.__b = b 
    def show(self):
        print(f"a={self.a}, b={self.__b}, sum={self.sum}")
    def calculate(self):
        self.sum = self.a+self.__b

my_add = Addition(5,6)
print(f"a = {my_add.__a}")
print(f"b = {my_add.__b}")
my_add.show()
my_add.calculate()
my_add.show()
print("Hello World!")