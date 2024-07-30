# reverse the digits of a number

def reverse_digits(number: int):
    number = int(input("Please enter the number you want to reverse: "))
    reverse_number = 0
    while (number > 0):
        rem = number % 10
        reverse_number = rem + (10 * reverse_number)
        number = int(number / 10)
       # print(reverse_number)
    print(reverse_number)

reverse_digits()