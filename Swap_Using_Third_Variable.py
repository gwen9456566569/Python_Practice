# Program to swap two numbers using third variable

def swap_using_third_variable():
    num1 = int(input("Please enter 1st number"))
    num2 = int(input("Please enter 2nd number"))
    num3 = num1
    num1 = str(num2)
    num2 = str(num3)
    print("Swapped numbers are " + num1 + " " + num2)


swap_using_third_variable()