import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

days_avg = 7
# total_days = 100

Buyer_ID = ['B00', 'B01','B02','B03','B04','B05','B06','B07','B08','B09','B10','B11','B12','B13','B14']
Seller_ID = ['S00','S01','S02','S03','S04','S05','S06','S07','S08','S09','S10','S11','S12','S13','S14']

def pps(file):
    data = pd.read_csv(file, header=None)
    time_id = 1
    prof_id = 8
    buyer_sum = []
    seller_sum = []
    timeall = []
    row = 0

    while row < len(data):
        timeall.append(data.iloc[row, time_id])
        buyer_id = 3
        seller_id = 3
        buy_prof = 8
        seller_prof = 8
        buy_sum = 0.0
        sell_sum = 0.0
        while buyer_id < 212:
            if (data.iloc[row, buyer_id]) in Buyer_ID:
                # print(data.iloc[a,trader_id])
                buy_sum += data.iloc[row,buy_prof]
                # print(data.iloc[a,prof_id])
            buyer_id = buyer_id + 7
            prof_id = prof_id + 7
        buyer_sum.append(buy_sum)

        while seller_id < 212:
            if (data.iloc[row, seller_id]) in Seller_ID:
                # print(data.iloc[0,trader_id])
                sell_sum+= data.iloc[row,seller_prof]
                # print(data.iloc[0,prof_id])
            seller_id = seller_id + 7
            seller_prof = seller_prof + 7
        seller_sum.append(sell_sum)
        row += 1

    buy_avg = moving_average(buyer_sum,len(data))
    sell_avg = moving_average(seller_sum, len(data))
    t = gen_time(len(data))

    print (len(t))
    print (len(buy_avg))
    print (len(sell_avg))


    fig, ax = plt.subplots()
    ax.plot(t, sell_avg, 'r-', label='sell')
    ax.plot(t, buy_avg, 'g-', label='buy')

    ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()




# pps('15PRDE4K.2F1_strats.csv')
# pps('15PRDE4K.8F1_strats.csv')


# def pps_buy(file):
#     x = 8
#     sum1 = [0]
#
#     while x < 110:
#         pps1 = data.iloc[:, x].values
#         # print('pps'+str(x), pps)
#         sum1 = sum1 + pps1
#         x = x + 7
#     # print(sum1)
#     # print(len(sum1))
#
#
def moving_average(sum0,leng):
    a = 0
    c = 0
    d = 0
    b = 0
    total = 0
    avg = []
    hours = 24 * days_avg
    day_interval = round(leng / hours)
    # print(day_interval)
    while c < day_interval:
        while a < hours:
            if d < leng:
                total += sum0[d]
                d += 1
            a += 1
        c += 1
        a = 0
        avg.append(total/7)
        total = 0
    return avg
#

#
#
# avg_buy = moving_average(sum1)
#
# y = 120
# sum12 = [0]
# sum22 = [0]
# sum32 = [0]
# sum42 = [0]
#
# while y < 212:
#     pps1 = data.iloc[:, y].values
#     # print('value' + str(y), pps)
#     sum12 = sum12 + pps1
#     y = y + 7
# # print(sum12)
# # print(len(sum12))
#
# avg_sell = moving_average(sum12)
# sum_total = sum1 + sum12
#
#
# avg_total = moving_average(sum_total)
#
def gen_time(leng):
    time = []
    a = 0
    hours = 24 * days_avg
    day_interval = round(leng / hours)
    t = days_avg
    while a < day_interval:
        time.append(t)
        t += days_avg
        a +=1
    return time
#
# # print(avg_buy)
# # print(avg_sell)
# # print(len(avg_buy))
# # print(len(avg_sell))
# # print(avg_total)
# # print(len(avg_total))
# # time1 = gen_time()
# # print(time1)
#
# def plot_pps(avg_buy,avg_sell, avg_total):
#     time = gen_time()
#     # print(time)
#     fig, ax = plt.subplots()
#     ax.plot(time, avg_sell, 'k-', label='sell')
#     ax.plot(time, avg_buy, 'k-', label='buy')
#     ax.plot(time, avg_total, 'b-', label='total')
#
#     ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#     plt.show()
#
#
# # plot_pps(avg_buy,avg_sell,avg_total)

# pps('15PRDE4K.8F1_strats.csv')
# pps('15PRDE4K.2F1_strats.csv')
