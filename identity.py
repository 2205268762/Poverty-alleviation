import importlib
import sys
importlib.reload(sys)
import requests
from lxml import etree
from bs4 import BeautifulSoup
import pandas as pd

# 先将存有身份证号码信息的txt文件读取进来
df = pd.read_csv('id_number.csv', dtype=str, na_filter=False)

# 定义'身份证号', '性别', '户口'3个list
idcard = []
sex1 = []
address1 = []

# 看一下读取进来的一共有多少个身份证号码
length = len(df)
print('一共有', length, '个身份证号')

# 通过循环，依次将每个身份证号对应的信息获取
for i in range(0, length):

    # 多一个try，防止某个号码出差自己中止代码执行
    try:
        # 查看身份证查询网页的网址，发现规律，按照规律组成url
        url = "http://qq.ip138.com/idsearch/index.asp?userid=" + df.iloc[i, 0] + "&action=idcard"

        # 解析网页
        res = requests.get(url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'lxml')

        # 将网页中需要的信息所有在的模块切出来
        mainpart = soup.select('div[class="bd"] tbody tr')

        # 将信息取出并存入list中
        if len(mainpart) > 4:
            sex = mainpart[1].text.split('性别')[1]
            address = mainpart[4].text.split('发证地')[1]

            idcard.append(df.iloc[i, 0])
            sex1.append(sex)
            address1.append(address)
        else:
            continue
    except Exception as e:
        print(Exception, ":", e)

# 打包数据
data = pd.DataFrame({'idcard': idcard, 'sex': sex1, 'address': address1})
print(data)  # 打印出来

# 将数据输出成一个文件
pd.DataFrame.to_excel(data, "identity.csv", index=0, header='身份证号\t性别\t户口\n', encoding='gbk')
