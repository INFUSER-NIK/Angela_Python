def is_palindrome(value):
    value = str(value)
    return value == value[::-1]

user_input = input("Enter a value to check if it's a palindrome: ")
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
