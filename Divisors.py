import sys

try:
    number = int(input("Enter a number:"))
except:
    print("Enter a number.")
    sys.exit(1)

print(f"Divisors of {number} are: {[i for i in range(1, number+1) if number%i==0]}")
