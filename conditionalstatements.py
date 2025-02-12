# if...else..
#loops
# votes = 10001
# if votes >10000:
#     print(f'You got {votes} and therefore you win!')
# else:
#     print(f'You got {votes} and therefore you fail!')
# marks = 54
# if marks > 80 and marks <= 100:
#     print(f"You got {marks} and you have grade A")
# elif marks > 70 and marks <= 80:
#     print(f"You got {marks} and you have grade B")
# elif marks > 60 and marks <= 70:
#     print(f"You got {marks} and you have grade C")
# elif marks > 40 and marks <= 60:
#     print(f"You got {marks} and you have grade D")
# elif marks < 40 and marks >= 0:
#     print(f"You got {marks} and you have grade E")
# else:
#     print('Please enter a number between 0 and 100')

# input in user
# age = int(input('Enter your age: '))
# print(age)
# if age <= 2 :
#     print('You are a baby')
# elif age >= 2 and age <= 3 :
#     print('You are a toddler')
# elif age >= 4 and age <= 12 :
#     print('You are a child')
# elif age >=13  and age <= 19 :
#     print('You are a teenager')
# elif age >= 20 and age <= 34 :
#     print('You are a young adult')
# elif age >= 35 and age <= 59 :
#     print('You are a middle-age adult ')
# else:
#      print('You are a senior citizen')
# print('Age is just a number, enjoy life')
#
# temperature = float(input("Enter the temperature in Fahrenheit: "))
# print(temperature)
# if temperature > 30:
#     print('It is a hot day')
# elif temperature < 20 and temperature >= 30:
#     print('It is a warm day')
# else:
#     print('It is a cold day')

amount_withdrawn = float(input("How much do you want to withdraw? "))
if amount_withdrawn >10000:
    amount_withdrawn = amount_withdrawn + (amount_withdrawn*0.1)
    print(f'amount withdrawn: {amount_withdrawn}')
elif amount_withdrawn > 5000 and amount_withdrawn <=10000:
    amount_withdrawn = amount_withdrawn + (amount_withdrawn*0.05)
    print(f'amount withdrawn: {amount_withdrawn}')
else:
    print(amount_withdrawn)






# # input in user
# age = int(input("How old are you?"))
# print(age)
# if age >= 18:
#     print(f'You are eligible to vote.')
# else:
#     print(f'You are not eligible to vote.')
#
# number = int(input("Enter a number!"))
# print(number)
# if number >0 :
#     print(f'The number {number} is positive.')
# if number == 0 :
#     print(f'The number {number} is zero.')
# else:
#     print(f'The number {number} is negative.')
