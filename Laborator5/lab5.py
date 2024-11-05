import math

#Exercitiul 1
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        semiperimeter = (self.a + self.b + self.c) / 2
        return math.sqrt(semiperimeter * (semiperimeter - self.a) * (semiperimeter - self.b) * (semiperimeter - self.c))

    def perimeter(self):
        return self.a + self.b + self.c
    
s=Shape()
c=Circle(3)
r=Rectangle(3,4)
t=Triangle(3,4,5)
print(c.area())
print(c.perimeter())
print(r.area())
print(r.perimeter())
print(t.area())
print(t.perimeter())
print("-------------------------------------------------")

#Exercitiul 2
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
        return self.balance

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate
        return self.balance

class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance) 
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("insufficient funds")
        self.balance -= amount
        return self.balance

a=Account("Ion", 100)
print(a.deposit(50))
print(a.withdraw(30))
sa=SavingsAccount("Ion", 100)
print(sa.add_interest())
ca=CheckingAccount("Ion", 100)
print(ca.withdraw(50))
print("-------------------------------------------------")

    
#Exercitiul 3
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self):
        return f"Mileage: {self.mileage} km"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self):
        return f"Mileage: {self.mileage} km"

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return f"Towing capacity: {self.towing_capacity} kg"

v=Vehicle("Ford", "Fiesta", 2019)
print(v.display_info())
c=Car("Ford", "Fiesta", 2019, 30)
print(c.calculate_mileage())
m=Motorcycle("Honda", "CBR", 2020, 50)
print(m.calculate_mileage())
t=Truck("Ford", "F-150", 2021, 10000)
print(t.calculate_towing_capacity())
print("-------------------------------------------------")


#Exercitiul 4
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        return f"Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_total_compensation(self):
        return self.salary + self.bonus

class Engineer(Employee):
    def __init__(self, name, salary, project_count):
        super().__init__(name, salary)
        self.project_count = project_count

    def display_project_count(self):
        return f"Projects handled: {self.project_count}"

class Salesperson(Employee):
    def __init__(self, name, salary, commission_rate): 
        super().__init__(name, salary)
        self.commission_rate = commission_rate

    def calculate_commission(self, sales_amount):
        return sales_amount * self.commission_rate 

e=Employee("Ion", 1000)
print(e.display_salary())
m=Manager("Ion", 1000, 100)
print(m.calculate_total_compensation())
en=Engineer("Ion", 1000, 5)
print(en.display_project_count())
s=Salesperson("Ion", 1000, 0.1)
print(s.calculate_commission(1000))
print("-------------------------------------------------")


#Exercitiul 5
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("implement the sound method")

class Mammal(Animal):
    def __init__(self, name, has_fur):
        super().__init__(name)
        self.has_fur = has_fur

    def sound(self):
        return "Mammal sound is playing"

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def sound(self):
        return "Bird sound is playing"

class Fish(Animal):
    def __init__(self, name, lives_in_water):
        super().__init__(name)
        self.lives_in_water = lives_in_water

    def sound(self):
        return "Fish sound is playing"

m=Mammal("Dog", True)
print(m.sound())
b=Bird("Parrot", True)
print(b.sound())
f=Fish("Shark", True)
print(f.sound())
print("-------------------------------------------------")


#Exercitiul 6
class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if self.checked_out:
            raise Exception("item is already checked out")
        self.checked_out = True

    def return_item(self):
        if not self.checked_out:
            raise Exception("item is not checked out")
        self.checked_out = False

    def display_info(self):
        return f"Title: {self.title}, ID: {self.item_id}"

class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def display_info(self):
        return f"{super().display_info()}, Author: {self.author}"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director):
        super().__init__(title, item_id)
        self.director = director

    def display_info(self):
        return f"{super().display_info()}, Director: {self.director}"

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue):
        super().__init__(title, item_id)
        self.issue = issue

    def display_info(self):
        return f"{super().display_info()}, Issue: {self.issue}"

b=Book("Anna Karenina", 1, "Lev Tolstoy")
b.check_out()
print(b.display_info())
b.return_item()
print(b.display_info())
d=DVD("Spider Man", 2, "Craig Webb")
d.check_out()
print(d.display_info())
d.return_item()
print(d.display_info())
m=Magazine("Vogue", 3, "June 2021")
m.check_out()
print(m.display_info())
m.return_item()
print(m.display_info())