import random


def get_temperatures():
    temperatures = []

    for i in range(7):
        temp = {}
        temp.clear()
        temp['x'] = i + 1
        temp['y'] = random.randint(15, 19)
        temperatures.append(temp)

    return temperatures