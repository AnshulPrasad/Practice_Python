a = map(lambda x: int(x), input("Enter numbers in list a: ").split())
b = map(lambda x: int(x), input("Enter numbers in list b: ").split())

print(f"common elements: {list(set(a) & set(b))}")

import random

a = [random.randint(1, 10) for _ in range(random.randint(1, 10))]
b = [random.randint(1, 10) for _ in range(random.randint(1, 10))]
print(f"a: {sorted(a)}")
print(f"b: {sorted(b)}")
print(f"common elements: {list(set(a) & set(b))}")
