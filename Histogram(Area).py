import matplotlib.pyplot as plt
import csv

# 将面积保存下来
area = []
with open("After_Processing_Data.csv", "r", newline="") as csv_in_file:
    filereader = csv.reader(csv_in_file, delimiter=",")
    for row_list in filereader:
        # 跳过表头
        if "城市" not in row_list[0]:
            area.append(int(row_list[4]))
# 将面积排序一下
area.sort()
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
n, bins, patches = ax1.hist(area, bins=50, density=False)
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")
# 写入横纵坐标轴的信息
plt.xlabel("Area")
plt.ylabel("Amount")
# 设置大标题
ax1.set_title("Amount And Area")
plt.savefig("Histogram(Area).png", dpi=400, bbox_inches="tight")
plt.show()
