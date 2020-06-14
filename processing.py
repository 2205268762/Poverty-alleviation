import numpy as np
import pandas as pd
# 从文件读取数据

data = pd.read_csv('C:/PycharmProjects/sy/generation.csv', sep='\t', encoding='gbk')
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
print(data.head())
