#! /usr/bin/env python3

print("Вводите целые числа и нажмите Enter: ")
total = 0
count = 0
while True:
    try:
        line = input()
        if line:
            number = int(line)
            total += number
            count += 1
    except ValueError as err:
        print(err)
        continue
    except EOFError:
        break
    total += number
    count += 1
if count:
    print("count = ", count, "total = ", total, "mean = ", total / count)
