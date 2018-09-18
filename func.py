import sys
import random

def get_int(input_data):
    while True:
        try:
            i = int(input(input_data))
            return i
        except ValueError as err:
            print(err)

x = random.randint(1, 6)
print(x)
y = random.choice(["a", "b", "c"])
print(y)
