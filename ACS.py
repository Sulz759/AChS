from math import cos, pi, sin
from dataread import data_read
import time
start_time = time.time()

def sum_1(N, mass_tmi, local, k):
    summa_1 = []
    for n in range(len(mass_tmi)):
        summa_1.append(mass_tmi[n] * cos(local * k * n))
    a = 2/N * sum(summa_1)
    return a

def sum_2(N, mass_tmi, local, k):
    summa_2 = []
    for n in range(len(mass_tmi)):
        summa_2.append(mass_tmi[n] * sin(local * k * n))
    b = 2/N * sum(summa_2)
    return b


def calc_A(file_path):
    mass_tmi = data_read(file_path)
    T = mass_tmi[0][-1] - mass_tmi[0][0]
    t = [0]
    dt = 2
    N = round(T/dt)
    f0 = 1/T
    fds = 1/dt
    K = round(fds/f0)
    A = []
    local = 2*pi*f0*dt
    for k in range(K):
        t.append(t[k]+2)
        a = sum_1(N, mass_tmi[1], local, k)
        b = sum_2(N, mass_tmi[1], local, k)
        A.append((a**2 + b**2) ** (1/2))
    t.remove(t[0])
    # print("--- %s seconds ---" % (time.time() - start_time))
    return t,A






