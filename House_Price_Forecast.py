import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# 读入数据
data = pd.read_csv("After_Processing_Data.csv", engine="python")

# 划分测试集，训练集
X_train, X_test, y_train, y_test = train_test_split(data.drop("月租", axis=1), data["月租"],
                                                    test_size=0.2, random_state=21)
# 随机森林
model = RandomForestRegressor(n_estimators=200, max_features=None)
model.fit(X_train, y_train)
predicted = model.predict(X_test)
# 将数据存入列表中，方便处理
predicted_list = []
y_test_list = []
for i in predicted:
    predicted_list.append(i)
for i in y_test:
    y_test_list.append(i)
accuracy = []
for i in range(0, 300):
    accuracy.append(abs((1 - abs(predicted_list[i] - y_test_list[i]) / y_test_list[i])))
# 计算准确率
data_sum = 0
for i in accuracy:
    data_sum += i
# 打印出准确率
print(data_sum / 300)
