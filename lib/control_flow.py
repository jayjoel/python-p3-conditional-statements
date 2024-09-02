#!/usr/bin/env python3


def admin_login(username, password):
    # your code here
    if (username.lower() == "admin") and password == "12345":
        return "Access granted"
    else: 
        return "Access denied"
    
print(admin_login("admin", "12345"))


def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature <=65 and temperature >=40:
        return "It's a little chilly out there!"
    elif temperature >= 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
print(hows_the_weather(33))
    

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else: 
        return num
    
print(fizzbuzz(3))
    

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "/":
        #Handle division by zero
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    elif operation == "*":
        return num1 * num2
    else:
        # Output an error message for invalid operations
        print("Invalid operation!")
        return None
print(calculator("/", 10, 5))