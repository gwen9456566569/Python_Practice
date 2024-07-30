# to check if string is pallindrome or not

def check_if_string_is_pallindrome():
    word = input("Please enter the string to check for pallindrome: ")
    reversed_word = word[::-1]
   # print(reversed_word)
    if word.lower() == reversed_word.lower():
        print("String is pallindrome :)")
    else:
        print("String is not pallindrome :(")

check_if_string_is_pallindrome()