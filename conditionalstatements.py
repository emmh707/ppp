# if...else..
#loops
votes = 10001
if votes >10000:
    print(f'You got {votes} and therefore you win!')
else:
    print(f'You got {votes} and therefore you fail!')

# input in user
age = int(input("How old are you?"))
print(age)
if age >= 18:
    print(f'You are eligible to vote.')
else:
    print(f'You are not eligible to vote.')

number = int(input("Enter a number!"))
print(number)
if number >0 :
    print(f'The number {number} is positive.')
if number == 0 :
    print(f'The number {number} is zero.')
else:
    print(f'The number {number} is negative.')
