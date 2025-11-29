def less_than_ten(list):
    temp_list = []
    for i in list:
        if i < 10:
            temp_list.append(i)
    return temp_list


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(less_than_ten(a))

print([i for i in a if i < 10])

try:
    number = int(input("Enter a number: "))
except:
    print("Enter a number")

print([i for i in a if i < number])
