# create a class called cars with the following attributes
# model,yearof manufacturing,type,color
# 
# create a method to print
# "my dream car is...manufactured in...being a...type...in color"
# 
# initialize with at least 5 objects

class cars:
    def __init__(self,model,yearofmanufacture,type,color):
        self.model=model
        self.yearofmanufacture=yearofmanufacture
        self.type=type
        self.color=color
# method
    def display(self):
             print(f"my dream cars is {self.model},{self.yearofmanufacture},{self.type},{self.color}")

my_cars=cars('toyota','2016','premio','green')
my_cars.display()
my_cars1=cars('mazda','2018','demio','blue')
my_cars1.display()
my_cars2=cars('toyota','2012','harrier','black')
my_cars2.display()
my_cars3=cars('toyota','2016','juke','green')
my_cars3.display()
my_cars4=cars('benz','2016','c-200','green')
my_cars4.display()
