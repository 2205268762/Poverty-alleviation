import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 显示所有列
from sklearn.preprocessing import MinMaxScaler
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

# 从文件读取数据
data = pd.read_csv('C:/PycharmProjects/sy/generation.csv', sep='\t', encoding='gbk')

# 数据的行列数
print('数据的行列数为:', data.shape)

# 统计数据的非空值
print('\n',  '数据的非空值', '\n',  data.count())

# 查看有缺失数据的数量和占比
total = data.isnull().sum().sort_values(ascending=False)
percent = (data.isnull().sum()/data.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['缺失数', '占比'])
print('\n', missing_data)

# 统计各项数据分布情况
print('\n', '数据的分布情况', '\n', data.describe())

# 查看存在缺失值的列
print('\n', '存在缺失值的字段', '\n', data.isnull().any())

# 查看均为缺失值的列
print('\n', '均为缺失值的字段', '\n', data.isnull().all())

# 查看存在缺失值的行
nan_lines = data.isnull().any(1)

# 统计有多少条数据存在缺失值
print('\n', '有', nan_lines.sum(), '条数据存在缺失值')

# 查看存在缺失值的行信息
print('\n', '以下为存在缺失值的数据', '\n', data[nan_lines])

# 重复数据查看
print('\n', '重复数据查看', '\n', data['身份证号'].duplicated())

# 编号去重
data['编号'] = data['编号'].drop_duplicates()
# 按身份证号去重
data['身份证号'] = data['身份证号'].drop_duplicates()

# 删除缺失身份证号的数据
data['身份证号'] = data['身份证号'].dropna()

data['身份证号'].to_csv("id_number.csv", index=False, header="身份证号", encoding="utf-8")
# '姓名', '性别', '邮政编号', '户口'根据'身份证号'提取信息填充
# '编号', '婚姻状况', '贫困原因', '年收入', '脱贫时间'根据实际情况填充

# 删除信息完全缺失的数据
data = data.dropna(how='all')


nsr = data["年收入"]
nsr = np.array([nsr])
# 数据无量纲化，区间缩放
MinMaxScaler().fit_transform(nsr)
# 离差标准化(最小-最大标准化)
zbh = (nsr-nsr.min())/(nsr.max()-nsr.min())
pd.DataFrame(zbh).T.to_csv("c.csv", index=False, header=False)

# 写入数据到文件
data.to_csv("generation0.csv", sep='\t', index=False, header="编号\t身份证号\t姓名\t性别\t邮政编号\t户口\t婚姻状况\t年收入\t贫困原因\t脱贫时间\n", encoding="utf-8")