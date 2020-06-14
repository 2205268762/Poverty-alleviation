import pandas as pd
import numpy as np
from pandas import Index, DataFrame
from sklearn.preprocessing import MinMaxScaler
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# 从文件读取数据
data = pd.read_csv('C:/PycharmProjects/sy/generation0.csv', sep='\t')
# 显示所有列
from sklearn.preprocessing import MinMaxScaler
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置之后在图表中可以显示中文字符
plt.rcParams['font.sans-serif'] = ['SimHei']    # 设置字体为中文雅黑
plt.rcParams['axes.unicode_minus'] = False  # 乱码的错误信息不再显示

# 区间统计
classdata = data["年收入"]
classdata = np.array(classdata)

# 划分成3组
a = pd.cut(classdata, 3)
print('\n', a)
print(a.codes)
pd.DataFrame(a, a.codes).to_csv("classa.csv", index=False)

# 按指定区间划分
b = pd.cut(classdata, [0, 1000, 2000, 3000, 4000, 5000])
print('\n', b)
print(b.codes)
pd.DataFrame(b, b.codes).to_csv("classb.csv", index=False)
# 按指定区间划分的各个区间的年收入数量
bv = b.value_counts()
print('\n', bv)
# 绘制年收入饼图
x = bv.index
y = bv.values

plt.figure(figsize=(10, 10))
plt.title('年收入各区间占比', fontsize=25, color='r')

patches, l_text, p_text = plt.pie(y, labels=x, autopct='%.2f%%')
for l in l_text:
    l.set_size(20)
    l.set_color('r')
for p in p_text:
    p.set_size(20)
    p.set_color('w')
plt.show()

# 绘制各种贫困原因致贫的人数数量条形图
pkyy = data. groupby('贫困原因'). size(). sort_values(ascending=False)
print(pkyy)

x = pkyy.index
y = pkyy.values

plt.figure(figsize=(15, 6))
plt.title('各贫困原因致贫人数', fontsize=30, color='black')
plt.xticks(rotation=45, fontsize=15, color='g')
plt.xlabel('贫困原因', rotation=0, fontsize=15, color='g')
plt.yticks(fontsize=15, color='g')
plt.ylabel('人数', rotation=90, fontsize=15, color='g')
for a, b in zip(x, y):
    plt.text(a, b+100, b, horizontalalignment='center', fontsize=15)
plt.bar(x, y)
plt.savefig('a.png')
plt.show()