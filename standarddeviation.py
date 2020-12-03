import math
import csv


def mean(data):
    l = len(data)
    total = 0
    for num in data:
        total += int(num)
    mn = total/l
    return mn


def deviation(data):
    mn = sum(data) / len(data)
    sum_of_squared = 0
    for val in data:
        sum_of_squared += (mn - val) ** 2
    return math.sqrt(sum_of_squared / (len(data) - 1))


with open("data/values.csv") as file:
    rdr = csv.reader(file)
    marks = list(rdr)
    data = marks[0]

    intData = []
    for i in data:
        intData.append(int(i))

    print("Deviation is : " + str(deviation(intData)))

    # # Subtract from mean and square the Values
    # squared = []

    # for score in data:
    #     num = int(score) - mean(data)
    #     num = num ** 2
    #     squared.append(num)

    # sum_of_squared = 0
    # for val in squared:
    #     sum_of_squared += val

    # res = sum_of_squared / (len(data) - 1)
    # deviation = math.sqrt(res)
    # print("Deviation is " + str(deviation))
