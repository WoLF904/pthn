import random

def get_int(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print("должно быть больше либо равно ", minimum)
            else:
                return i
        except ValueError as err:
            print(err)

rows = get_int("число строк:", 1, None)
columns = get_int("число столбцов:", 1, None)
minimum = get_int("минимальное значение (или нажмите Enter для 0)", -1000000, 0)
default = 1000
if default < minimum:
    default = 2 * minimum
maximum = get_int("максимальное значение (или нажмите Enter для " + str(default) + "):", minimum, default)

row = 0
while row < rows:
    line = ""
    column = 0
    while column < columns:
        i = random.randint(minimum, maximum)
        s = str(i)
        while len(s) < 10:
            s = " " + s
        line += s
        column += 1
    print(line)
    row += 1
