# Swap two numbers without using third variable

def swap_without_third_variable():
    num1 = int("Please enter 1st number: ")
    num2 = int("Please enter 2nd number: ")
    num1 += num2
    num2 = num1 - num2
    num1 -= num2
    print("Swapped numbers are "+ str(num1) + " "+ str(num2))

swap_without_third_variable()