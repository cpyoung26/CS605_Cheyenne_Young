# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:06:53 2026

@author: Cheyenne
"""

print("Welcome to Simple Calculator. Your best calculator friend!")

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y != 0:
        return x / y
    else: 
        return "Error: Cannot divide by zero"

while True: 
    print("Select an operation: \n"
          "1. Add \n"
          "2. Subtract \n"
          "3. Multiply \n"
          "4. Divide \n"
          )
    choice = input("Enter preferred operation number: ")
    if choice in ('1' , '2' , '3' , '4'):
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
        except ValueError: 
            print("Invalid input. Please enter a number.")
            continue 
        
        if choice == '1': 
            print (n1, "+", n2, "=", add(n1 , n2))
            
        elif choice == '2': 
            print (n1, "-", n2, "=", sub(n1 , n2))
            
        elif choice == '3': 
            print (n1, "*", n2, "=", mul(n1 , n2))
            
        elif choice == '4': 
            print (n1, "/", n2, "=", div(n1 , n2))
            
        while True:
            next_calc = input("Would you like to perform another calculation? (yes/no): ")
            if next_calc == "yes": 
               break
            if next_calc == "no":
               break
            else:
               print("Invalid Input")
        if next_calc == "no":
            break
        
print("Thank you for choosing Simple Calculator!")


