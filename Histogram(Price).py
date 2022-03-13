import matplotlib.pyplot as plt
import csv

# 将月租的信息保存下来
price = []
with open("After_Processing_Data.csv", "r", newline="") as csv_in_file:
    filereader = csv.reader(csv_in_file, delimiter=",")
    for row_list in filereader:
        if "城市" not in row_list[0]:
            price.append(int(row_list[7]))
# 月租信息排序
price.sort()
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
n, bins, patches = ax1.hist(price, bins=50, density=False)
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")
# 写入横纵坐标的标题
plt.xlabel("Price")
plt.ylabel("Amount")
# 写入大标题
ax1.set_title("Amount And Price")
# 保存
plt.savefig("Histogram(Price).png", dpi=400, bbox_inches="tight")
plt.show()
