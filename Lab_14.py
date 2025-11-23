# class Car:
#     # Constructor to initialize the object
#     def __init__(self, brand, model):
#         self.brand = brand  # Attribute
#         self.model = model  # Attribute

#     # Method to describe the car
#     def car_details(self):
#         return f"Car: {self.brand}, Model: {self.model}"

# # Creating an object of the Car class
# my_car = Car("Toyota", "Corolla")
# print(my_car.car_details())  

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     # Method to calculate area
#     def area(self):
#         return self.width * self.height

#     # Method to calculate perimeter
#     def perimeter(self):
#         return 2 * (self.width + self.height)

# # Create an object
# rect = Rectangle(10, 5)

# # Accessing methods
# print(f"Area: {rect.area()}")  # Output: Area: 50
# print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 30

# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds")

#     def get_balance(self):
#         return self.__balance

# # Create an account
# account = BankAccount("John", 1000)
# account.deposit(500)
# print(account.get_balance())  
# account.withdraw(700)
# print(account.get_balance())  

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "I am an animal."

# # Dog class inherits from Animal class
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"

# # Cat class inherits from Animal class
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"

# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# print(dog.speak())  # 
# print(cat.speak())  # 

# class Polygon:
#     # method to render a shape
#     def render(self):
#         print("Rendering Polygon...")

# class Square(Polygon):
#     # renders Square
#     def render(self):
#         print("Rendering Square...")

# class Circle(Polygon):
#     # renders circle
#     def render(self):
#         print("Rendering Circle...")
    
# # create an object of Square
# s1 = Square()
# s1.render()

# # create an object of Circle
# c1 = Circle()
# c1.render()

# from abc import ABC, abstractmethod

# # Abstract class
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# circle = Circle(5)
# print(f"Area of the circle: {circle.area()}")  # 

#-----------POST LABS---------------

#Question 1
# class Circle: 
#     def __init__(self, radius): 
#         self.radius = radius 
 
#     def area(self): 
#         return 3.14 * self.radius * self.radius 
 
#     def perimeter(self): 
#         return 2 * 3.14 * self.radius 
 
# circle1 = Circle(7) 
 
# print("Area of circle:", circle1.area()) 
# print("Perimeter of circle:", circle1.perimeter())

#Question 2 
class Book: 
    def __init__(self, title, author, price): 
        self.title = title 
        self.author = author 
        self.price = price 
 
    def display(self): 
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}") 
 
    def apply_discount(self, percent): 
        discount = self.price * (percent / 100) 
        self.price -= discount 
 
# Create two books 
book1 = Book("Harry Potter and the Order of the Phoenix", "J.K. Rowling", 500) 
book2 = Book("God of Wrath", "Rina Kent", 600) 
 
# Display details 
book1.display() 
book2.display() 
 
# Apply 10% discount to book2
book2.apply_discount(10) 
 
print("\nAfter applying 10% discount:") 
book2.display()





