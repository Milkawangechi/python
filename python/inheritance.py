# class Animal:
#     def speak(self):
#         print('Animal speaking')
#         # the child class Dog inherits the base class Animal

# class Dog(Animal):
#     def bark(self):
#         print('dog is barking')
# # the child class Dog inherits another child class Dog

# class Dogchild(Animal):
#     def eat(self):
#         print('Dogchild is eating meat')

# class Cow(Animal):
#     def mooh(self):
#         print('cow is moohing')
        
# a=Animal()
# a.speak()
# d=Dog()
# d.bark()
# d=Dogchild()
# d.eat()
# c=Cow()
# c.mooh()

class person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def print_name(self):
        print(f"my name is {self.first_name}, {self.last_name}, and i am {self.age} years old") 

class Student(person):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
myStudent=Student("john","smith",30)
myStudent.print_name()
myStudent=Student("rose","smith",30)
myStudent.print_name()

        
        