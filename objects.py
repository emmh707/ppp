# from classes import Employee
from classes import Emobilis_Employee, Developer, Teacher, Commission_Employee

# person1 = Person()
# print(person1.first_name)
# print(person1.last_name)
# print(person1.age)
#
# person2 = Person()
# print(person2.first_name)
# print(person2.last_name)
# print(person2.age)
# print(person2.gender)
#
# employee1 = Employee("John","Male",100000,23, "developer")
# employee2 = Employee("Emma","Female",850000,30, "intern")
# employee3 = Employee("Jennifer","Female",100000,28, "nurse")
#
# print(employee1.basic_salary)
# print(employee2.gender )
# print(employee3.position)
#
# print(employee1.display())
# print(employee2.display())
#
# print(employee1.full_salary())
# print(employee2.full_salary())
# print(employee3.full_salary())
#
# print(employee1.new_salary())
# print(employee2.new_salary())
# print(employee3.new_salary())

# car1 = Car("BMW",2025,"KDR","hotpink")
# car2 = Car("Ferrari",2022,"KCF","green")
# car3 = Car("SUV",2025,"KDS","black")

# print(car1.plate)
# print(car2.colour)
# print(car3.make)

# rectangle1 = Rectangle(24,12)
# rectangle2 = Rectangle(36,9)
# rectangle3 = Rectangle(48,15)
#
# print(rectangle1.display())
# print(rectangle2.perimeter())
# print(rectangle3.area
emobilis_employee1 = Emobilis_Employee("Immaculate","Female",230000,24,"Degree")
emobilis_employee2 = Emobilis_Employee("Shanice","Female",125000,19,"Diploma")
emobilis_employee3 = Emobilis_Employee("James","Male",12000,34,"Masters")


print(emobilis_employee1.qualification)
print(emobilis_employee2.salary)
print(emobilis_employee1.promotion())
print(emobilis_employee3.promotion())
developer1 = Developer("Queen","Female",230000,24,"Degree","Fronted Developer","Python")
developer2 = Developer("Baby","Male",24000,23,"Diploma","Backend","html")
print(developer1.specialization)
print(developer2.prog_language)


teacher1 = Teacher("Imma","Female",20000,32,"Degree","English and Literature",10,6)
teacher2 = Teacher("Stanley","Male",80000,24,"Masters","Biology and Chemistry",4,2)
print(teacher1.subjects)
print(teacher2.no_school_taught)

commission_employee1 = Commission_Employee("Wayne","Male",20000,22,"Masters",1000,12)
print(commission_employee1.commission_salary())