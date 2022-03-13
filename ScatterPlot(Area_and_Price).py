import matplotlib.pyplot as plt
import csv

# 将面积和月租全保存下来
area = []
# x
price = []
# y
plt.style.use("ggplot")
with open("After_Processing_Data.csv", "r", newline="") as csv_in_file:
    filereader = csv.reader(csv_in_file, delimiter=",")
    for row_list in filereader:
        if "城市" not in row_list[0]:
            area.append(int(row_list[4]))
            price.append(int(row_list[7]))
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
# 画散点图
plt.scatter(area, price, c="b", alpha=0.6)
# 设置大标题
ax1.set_title("Area and Price")
# 设置横纵坐标的标题
plt.xlabel("Area")
plt.ylabel("Price")
# 保存
plt.savefig("ScatterPlot(Area_and_Price).png", dpi=400, bbox_inches="tight")
plt.show()
