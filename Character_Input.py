import datetime

current_datetime = datetime.datetime.now()
current_year = current_datetime.year

# inputs are like:-
# anshul prasad 22
text = input("Enter your name and age: ").strip().split()

try:
    name, age = " ".join(text[:-1]), int(text[-1])
    message = f"{name} will be 100 years old in the year {current_year+(100-age)}\n"
    print(message, end="")
except:
    print("Input the correct information and in order(name age).")

number = int(input("Enter a number: "))
print(message * number)
