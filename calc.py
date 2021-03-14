import math
from dataread import data_read

def average_calc(file):
    mass = data_read(file)
    return sum(mass[1])/len(mass[1])

def module_calc(file):
    mass = data_read(file)
    for i in range(len(mass[1])):
        mass[1][i] = abs(mass[1][i])
    return sum(mass[1]) / len(mass[1])


def disp_calc(file):
    mass = data_read(file)
    aver = average_calc(file)
    mass_2 = []
    for i in range(len(mass[1])):
        mass_2.append((mass[1][i] - aver)**2)
    return sum((mass_2)) / (len(mass_2)-1)

def sko_calc(disp):
    return math.sqrt(disp)

def max_calc(file):
    mass = data_read(file)
    aver = average_calc(file)
    for i in range(len(mass[1])):
        mass[1][i] = abs(mass[1][i] - aver)
    return max(mass[1])

def apparent_frequency_calc(file):
    mass = data_read(file)
    return len(mass[0])/(2*(mass[0][-1] - mass[0][0]))
