class Person:
    first_name = "Alex"
    last_name = "Kama"
    gender = "Female"
    age = 19
class Employee:
    def __init__(self,name,gender,basic_salary,age,position):
        self.name = name
        self.gender = gender
        self.basic_salary = basic_salary
        self.age = age
        self.position = position

    def display(self):
        return f"Name: {self.name} , Gender: {self.gender}"
    def full_salary(self):
        full_salary = self.basic_salary + 25000
        return full_salary
    def new_salary(self):
        new_salary = self.basic_salary + (0.27* self.basic_salary)
        return new_salary

class Car:
    def __init__(self,make,year,plate,colour,):
        self.make = make
        self.year = year
        self.plate = plate
        self.colour = colour

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def perimeter(self):
        perimeter = self.length * self.width
        return perimeter
    def area(self):
        area = self.length * self.width
        return area
    def display(self):
        return f"Length: {self.length} , Width: {self.width}"
class Emobilis_Employee:
    def __init__(self,name,gender,salary,age,qualification):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.age = age
        self.qualification = qualification
    def promotion(self):
        if self.qualification == "Degree" or self.qualification == "Masters":
            return "You are promoted"
        else:
            return "You are not promoted"
class Developer(Emobilis_Employee):
    def __init__(self,name,gender,salary,age,qualification,specialization,prog_language):
        super().__init__(name,gender,salary,age,qualification)
        self.specialization = specialization
        self.prog_language = prog_language
class Teacher(Emobilis_Employee):
    def __init__(self,name,gender,salary,age,qualification,subjects,experience,no_school_taught):
        super().__init__(name,gender,salary,age,qualification)
        self.subjects = subjects
        self.experience = experience
        self.no_school_taught = no_school_taught

class Commission_Employee(Emobilis_Employee):
    def __init__(self,name,gender,salary,age,qualification,commission_rate,hours_worked):
        super().__init__(name,gender,salary,age,qualification)
        self.commission_rate = commission_rate
        self.hours_worked = hours_worked
    def commission_salary(self):
        commission_salary = (self.commission_rate * self.hours_worked) + self.salary
        return commission_salary


