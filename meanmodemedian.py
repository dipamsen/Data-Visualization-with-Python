# Mean Mode and Median

import csv
from collections import Counter


def main():
    csvfile = open("./data/SOCR-HeightWeight.csv")
    heightweights = list(csv.reader(csvfile))
    heightweights.pop(0)
    length = len(heightweights)
    totalweight = 0
    weights = []
    for index, height, weight in heightweights:
        totalweight += float(weight)
        weights.append(weight)
    sorted_weights = sorted(weights)
    mean_val = mean(totalweight, length)
    median_val = median(sorted_weights, length)
    mode_val = mode(sorted_weights)
    print("Mean of weights is " + str(mean_val))
    print("Median of weights is " + str(median_val))
    print("Mode of weights is " + str(mode_val))


def mean(total, length):
    return total/length


def median(sorted_weights, len):
    # [10, 203, 1245, 128]
    #  0   1    2     3
    if len % 2 == 0:
        first_element = float(sorted_weights[len//2])
        second_element = float(sorted_weights[len//2 - 1])
        return (first_element+second_element)/2
    else:
        element = float(sorted_weights[len//2])
        return element


def mode(data):
    dict = {
        "75-85": 0,
        "85-95": 0,
        "95-105": 0,
        "105-115": 0,
        "115-125": 0,
        "125-135": 0,
        "135-145": 0,
        "145-155": 0,
        "155-165": 0,
        "165-175": 0,
    }
    for weight in data:
        if 75 < float(weight) < 85:
            dict["75-85"] += 1
        if 85 < float(weight) < 95:
            dict["85-95"] += 1
        if 95 < float(weight) < 105:
            dict["95-105"] += 1
        if 105 < float(weight) < 115:
            dict["105-115"] += 1
        if 115 < float(weight) < 125:
            dict["115-125"] += 1
        if 125 < float(weight) < 135:
            dict["125-135"] += 1
        if 135 < float(weight) < 145:
            dict["135-145"] += 1
        if 145 < float(weight) < 155:
            dict["145-155"] += 1
        if 155 < float(weight) < 165:
            dict["155-165"] += 1
        if 165 < float(weight) < 175:
            dict["165-175"] += 1
    highest_key = ''
    highest_value = 0
    for key, value in dict.items():
        if(value > highest_value):
            highest_value = value
            highest_key = key
    indices = highest_key.split("-")
    return (int(indices[0]) + int(indices[1]))/2


main()
