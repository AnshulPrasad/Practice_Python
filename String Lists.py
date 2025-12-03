# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
s = input("Enter string: ")
if s == s[::-1]:
    print("Is a palindrome.")
else:
    print("Not a palindrome.")
