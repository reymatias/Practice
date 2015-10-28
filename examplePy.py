# Chapter 1: Installation
print('Hello world!')

# Chapter 2: Print and Strings
print("Double quotes")
print('concatena' + 'tion')
print('hello', 'there')
print('I am',5)
print('I\'m 5')
print("I'm 5")

# Chapter 3: Math
print(1+3)
print(1-3)
print(1*3)
print(1/3)
print(1.5/3.6)
print(4**2)

# Chapter 4: Variables
exVar = 100
print(exVar)
opVar = exVar / 5.3
print(opVar)

# Chapter 5: While Loops
condition = 1
while condition < 10 :
    print(condition)
    ''' Multiple line comments '''
    # condition = condition + 1
    condition += 1

# Chapter 6: For Loops
exampleList = [1, 6, 7, 3, 6, 9, 0]
for x in exampleList:
    print(x)
for x in range (1,11):
    ''' Generates numbers from 1 to x<11 '''
    print(x)

# Chapter 7: If Statements
x = 2
y = 7
z = 10
if x < y:
    print(x, 'is less than', y)
if z > y > x <= z > y:
    print(z, 'is greater than', y, 'which is greater than', x)

# Chapter 8: If Else Statements
x = 3
y = 6
if x < y:
    print(x, 'is less than', y)
else:
    print(x, 'is not less than', y)

# Chapter 9: If Elif Else Statements
x = 3
y = 7
z = 10
if x > y or x < z:
    print(x,'is greater than', y)
elif x < z:
    print(x, 'is less than', z)
elif y < z:
    print(y, 'is greater than', z)
else:
    print('nothing was the case')

# Chapter 10: Functions
def example():
    x = 1
    y = 3
    print(x + y)

    if x < y:
        print(x, 'is less than', y)
    
example()

# Chapter 11: Function Parameters
def website(font = 'TNR',
            background_color = 'white',
            font_size = 11,
            font_color = 'black'):
    print('font: ', font)
    print('bg: ', background_color)
    print('font size: ', font_size)
    print('font color: ', font_color)

# website('TNR', 'white', '11', 'black')
# website(font_color = 'black',
#         font = 'TNR',
#         background_color = 'white',
#         font_size = '11')
website(background_color = 'grey')

def addition(num1, num2):
    answer = num1 + num2
    return answer

x = addition(5, 6)
print(x)

# Chapter 12: Global and Local Variables
x = 6
def example2():
    z = 5
    print(z)

example2()

# cannot do this
# print(z)

def example3():
    z = 7
    print(z)
    print(x)

    # cannot do this
    # x += 1
    y = x + 1
    print(y)
    return y

example3()

x = example3()
print(x)

def example4():
    global x
    x += 1
    print(x)


# Chapter 13: Common Python Errors
