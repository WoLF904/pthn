numList = []
inputVal = ""
sumValue, minValue, maxValue, meanValue = 0, 0, 0, 0

while True:
    try:
        inputVal = input("enter a number or enter to finish: ")
        if not inputVal:
            break
        else:
            numList.append(int(inputVal))
    except ValueError:
        print("input must be a number! or empty to finish")
if len(numList) == 0:
    print("Empty Num List")
else:
    print("numbers: ", numList)
    print("count = ", len(numList), " sum = ", sum(numList), " lowest = ", min(numList), " highest = ", max(numList), " mean = ", sum(numList) / len(numList))
