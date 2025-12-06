"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""

import random

CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^&*()-_=+[]{}:;'\",.<>?/\\|"

pass_len = {"weak": 10, "medium": 20, "strong": 30}
stren = input("Enter stregth of the password: ")
print(
    f"pasword: {''.join([CHARACTERS[i] for i in random.sample(range(len(CHARACTERS)),pass_len[stren])])}"
)
