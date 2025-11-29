import sys

try:
    number = int(input("Enter a number: "))
except:
    print("Enter a number.")
    sys.exit(1)

if number % 2 == 1:
    print("The number is odd.")
else:
    print("The number is even.")

if number % 4 == 0:
    print("The number is a multiple of 4.")


try:
    num, check = int(input("Enter a number to check: ")), int(
        input("Enter a number to divide by: ")
    )
except:
    print("Enter a number.")
    sys.exit(1)

if num % check == 0:
    print(f"{num} divides evenly by {check}.")
else:
    print(f"{num} does not divides evenly by {check}.")
