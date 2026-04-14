# Inside the editor, complete the following steps:
# Create a class called Dog
# Add an __init__ method with parameters name and age, and store them as properties using self
# Add a method called bark that prints the dog's name followed by " says Woof!"
# Create an object d1 of the Dog class with name "Buddy" and age 3
# Call the bark method on d1

# class dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def bark(self):
#         # print(f'{self.name} woof!')
#         return f'{self.name} woof!'

# ash = dog("ash",5)

# print(ash.bark())


# class hello():
#     def __init__(self,name):
#         self.name=name
#     def greet(self):
#         return f'hi welcome {self.name}'
#     def welcome(self):
#         msg = self.greet()
#         print('HI there',msg)

# p1=hello("ahmad")

# p1.welcome()


# Create a class called Car
# Add an __init__ method with a brand parameter, and store it as a property
# Add a method called show that prints the brand
# Create an object c1 of the Car class with brand "Ford"
# Call the show method on c1

# class Car():
#     def __init__(self,name):
#         self.name=name
#     def brand(self):
#         return self.name
    
# c1=Car('Toyota')
# print(c1.brand())


# class hello():
#     name='ahmad'
#     def __init__(self,degreeg="cs"):
#         self.degreeg=degreeg
#     def info(self):
#         return f'{self.name} age is {self.age} and degree is {self.degreeg} '
    

# hello.age=18

# s1=hello()

# print(s1.info())


# class uog():
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def info(self):
#         return f'{self.name} your is is = {self.id}'
    
# class student(uog):
#     def __init__(self, name, id,dept):
#         super().__init__(name, id)
#         self.dept =dept
    
#     def all_info(self):
#         return f'{self.name} with id {self.id} in dept {self.dept}'

# class teacher(student):
#     def __init__(self, name, id, dept,age):
#         super().__init__(name, id, dept)
#         self.age=age
#     def t_info(self):
#         return f'{self.name} with id {self.id} in dept {self.dept} and age is {self.age}'
    

# t1=teacher('ahmad',69,'cs',22)

# def hinew(self):
#     return f'{self.name} is a good boy'

# teacher.t_info=hinew


# print(t1.t_info())

# class uog():
#     def __init__(self,name,id):
#         self.__name=name
#         self.id=id
#     def info(self):
#         return f'{self.__name} your is is = {self.id}'

# s1 = uog('ahmad',69)

# print(s1.info())


# --------------------what are classes and objects etc 
    
