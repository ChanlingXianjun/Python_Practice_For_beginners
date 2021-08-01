# New learn how to get input from users and store the prompt as a variable.
name = input('Enter your name: ')
age = input('Enter your age')
print('Hello ' + name +'! You are ' + age + ' year old.')

# Bulid a simple calculater which adding two input together.
num1 = input('Entwr the first number: ')
num2 = input('Enter the second number: ')
result = num1 + num2
print(result)
#By defult, Python is gong to combine those two varibles as string together, not a math operation.
result2 = int(num1) + int(num2)
print(result2)
#int function turn whatever inside thr parenthesis into integers
result3 = float(num1) + float(num2)
print(result3)
#float function is going to allow us to input decimal numbers.
