# def my_function():
#     print("Hello World")
#     print("Hello World")
# my_function()
# my_function()
# my_function()
#
# def my_function2():
#     salute = "Commonwealth Nations"
#     print(salute)
# my_function2()
#
# def customers(salute):
#     print(salute)
# customers("Commonwealth Nations")
# customers("Damn it")
# customers("Bonjour Emma")
#
# def employees(first_name, last_name,age ):
#     print(f'My name is {first_name} {last_name} and i am {age} years old')
# employees("Hillary", "Smith", 22)
# employees("Stanley","Locke", 18)
# employees("Gloria","Amollo", 27)
# employees("Immaculate", "Adhiambo",12)

# def text_it(first_number,second_number):
#       print(f'First number= {first_number} and Second number = {second_number}')
#       summation = first_number + second_number
#       print(f'Summation = {summation}')
#       subtraction = first_number - second_number
#       print(f'Subtraction = {subtraction}')
# text_it(29,6)
# text_it(999,200)
#
# def arithmetic(num1,num2):
#     total = num1 + num2
#     subtraction = num1 - num2
#     return(f'The total of {num1} and {num2} is: {total} and subtraction is :{subtraction}')
# print(arithmetic(29,6))
#
# def age_calculator(curret_age):
#     new_age = curret_age + 36
#     return new_age
# print(age_calculator(18))
#
# def bet_bonus(name,correct_score):
#     if correct_score >= 9 and correct_score >= 13:
#         return f'{name} your bonus is 9000'
#     elif correct_score >=6 and correct_score <9:
#      return f'{name} your bonus is 5000'
#     elif correct_score >=4 and correct_score <6:
#      return f'{name} your bonus is 2000'
#     else:
#         return f'{name} your bonus is 0'


# bet_bonus('Imma',14)
# print(bet_bonus('Imma',14))

def greet(name):
    if name == "Alice" or name == "Bob":
        return f'Hello {name}!'
    else:
        return "Good Morning!"
print(greet("Emma"))
print(greet("Bob"))