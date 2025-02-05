# list
employees = ['John','Smith','Andrew','Jane']
print(employees)
print(employees[2])
print(employees[1:4])
employees[3] = 'Reuben'
print(employees)
employees.append('Stephen')
print(employees)
employees.insert(2,'Julianna')
print(employees)
employees.extend(['Paul','Erick','Allan'])
print(employees)
# tuple
products = ('apple', 'banana', 'orange','cherry')
print(products)
print(products[2])
print(products[1:3])
# products[0] = 'Mango'
print(products)
# set
students = {'Peter','Esther','Andrew','Emma'}
students.add('Dennis')
print(students)
students.update(['Kimberly'])
print(students)
students.remove('Esther')
print(students)


# dictionary
book = {
    'title':'Book Title',
    'author':'Ali',
    'publisher':'Turkey',
}
print(book)
book['year of publication'] = 2020
print(book)
print(book['author'])
print(book['publisher'])
print(book['title'])

if 'author' in book:
    print('Author is in book')
else:
    print('Author is not in present')

kenya = {
    'city':'Nairobi',
    'counties': 'Forty Seven',
    'tribes':'Many',
    'language':'English',
    'presidents': 'Four',
    'neighbours': 'Six'
}
print(kenya)
if 'city' in kenya:
    print('city is present')
else:
    print('city is not present')
