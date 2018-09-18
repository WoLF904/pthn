import sys

Zero = ["*******",
        "*     *",
        "*     *",
        "*     *",
        "*     *",
        "*     *",
        "*******"]
One = ["      *",
       "   *  *",
       "*     *",
       "      *",
       "      *",
       "      *",
       "      *"]
Two = ["*******",
       "      *",
       "      *",
       "*******",
       "*      ",
       "*      ",
       "*******"]
Three = ["*******",
         "      *",
         "      *",
         "*******",
         "      *",
         "      *",
         "*******"]
Four = ["*     *",
        "*     *",
        "*     *",
        "*******",
        "      *",
        "      *",
        "      *"]
Five = ["*******",
        "*      ",
        "*      ",
        "*******",
        "      *",
        "      *",
        "*******"]
Six = ["*******",
       "*      ",
       "*      ",
       "*******",
       "*     *",
       "*     *",
       "*******"]
Seven = ["*******",
         "      *",
         "      *",
         "      *",
         "      *",
         "      *",
         "      *"]
Eight = ["*******",
         "*     *",
         "*     *",
         "*******",
         "*     *",
         "*     *",
         "*******"]
Nine = ["*******",
        "*     *",
        "*     *",
        "*******",
        "      *",
        "      *",
        "*******"]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    inDigits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        col = 0
        while col < len(inDigits):
            number = int(inDigits[col])
            digit = Digits[number]
            line += str(digit[row]).replace("*", str(number)) + "   "
            col += 1
        print(line)
        row += 1
except IndexError:
    print("Пример вызова: printDigits.py <число>")
except ValueError:
    print("требуется воодить только числа!")
