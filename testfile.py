import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

days_avg = 2
total_days = 10

data = pd.read_csv('exp3_strats.csv', header=None)
leng = len(data)
# print(leng)


def moving_average(sum0, leng):
    a = 0
    c = 0
    d = 0
    total = 0
    avg = []
    hours = 24 * days_avg
    day_interval = round(leng / hours)
    print(day_interval)
    while c < day_interval:
        while a < hours:
            if d < leng:
                total += sum0[d]
                d += 1
            a += 1
        c += 1
        a = 0
        avg.append(total)
        total = 0

    return avg


x = 8
sum1 = [0]

while x < 114:
    pps = data.iloc[:, x].values
    # print('pps'+str(x), pps)
    sum1 = sum1 + pps
    x = x + 7

# print(len(sum1))

avg_buy = moving_average(sum1, leng)

y = 120
sum2 = [0]

while y < 212:
    pps = data.iloc[:, y].values
    # print('value' + str(y), pps)
    sum2 = sum2 + pps
    y = y + 7

# print(len(sum2))

avg_sell = moving_average(sum2, leng)


def gen_time(days_avg, total_days):
    time = [0]
    t = days_avg
    while t < total_days:
        time.append(t)
        t += days_avg
    return time

print(avg_buy)
print(avg_sell)


def plot_pps(avg_buy, avg_sell, days_avg, total_days):
    time = gen_time(days_avg, total_days)
    # print(time)
    fig, ax = plt.subplots()
    ax.plot(time, avg_sell, 'r-', label='sell')
    ax.plot(time, avg_buy, 'g-', label='buy')
    ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()


plot_pps(avg_buy, avg_sell, days_avg, total_days)
