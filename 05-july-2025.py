#Write a function to find the sum of digits of a number.
def sum_numbers():
    num = int(input("Enter Your Number: "))
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    print("Sum of digits is:", total)

sum_numbers()
#-------------------------------
#Write a function to count the number of vowels in a string.
def count_vowels():
    text = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    print("Number of vowels:", count)

count_vowels()
#-------------------------
#Write a function to calculate the area of a circle given the radius.
def area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    pi = 3.14159
    area = pi * radius ** 2
    print("Area of the circle is:", area)
area_of_circle()
#-----------------------
#Write a function ;
# to determine whether a year is a leap year.
def is_leap_year():
    year = int(input("Enter a year: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a Leap Year.")
    else:
        print(year, "is Not a Leap Year.")
is_leap_year()
#--------------------------
#Write a function to find the greatest among three numbers.
def find_greatest():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    if num1 >= num2 and num1 >= num3:
        greatest = num1
    elif num2 >= num1 and num2 >= num3:
        greatest = num2
    else:
        greatest = num3

    print("The greatest number is:", greatest)
find_greatest()
#-------------------------------
#Write a function to reverse a string.
def reverse_string():
    text = input("Enter a string: ")
    reversed_text = text[::-1]
    print("Reversed string is:", reversed_text)
reverse_string()
#----------------------
#Write a function to act as a simple calculator (add, subtract, multiply, divide).
def calculator():
    print("Simple Calculator")
    print("Choose operation: +, -, *, /")
    operation = input("Enter operation: ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '+':
        result = num1 + num2
        print("Result:", result)
    elif operation == '-':
        result = num1 - num2
        print("Result:", result)
    elif operation == '*':
        result = num1 * num2
        print("Result:", result)
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation.")
calculator()
#--------------------------------------
#Write a function to convert temperature from Celsius to Fahrenheit.
def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
celsius_to_fahrenheit()
#-----------------------------
#Write a function to check if a number is positive, negative, or zero.
def check_number():
    num = float(input("Enter a number: "))
    
    if num > 0:
        print("The number is Positive.")
    elif num < 0:
        print("The number is Negative.")
    else:
        print("The number is Zero.")
check_number()
#-----------------------
# Write a function to check whether a character is a vowel or a consonant.
def check_vowel_or_consonant():
    char = input("Enter a single alphabet character: ")

    if len(char) != 1 or not char.isalpha():
        print("Invalid input. Please enter a single alphabet letter.")
    else:
        vowels = "aeiouAEIOU"
        if char in vowels:
            print(char, "is a Vowel.")
        else:
            print(char, "is a Consonant.")
check_vowel_or_consonant()
#----------------------------