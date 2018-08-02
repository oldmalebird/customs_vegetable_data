#提取贸易方式进出口数据
import pandas as pd
#python D:\Github\customs_vegetable_data\test.py

docAddress = r'D:\Data\信息中心进出口\原始数据\2018\蔬菜水果_贸201801-201803.xls'
df_origin = pd.read_excel(docAddress,sheet_name='Report', header = None, names = ["产品","贸易方式","当期出口金额（万美元）","当期进口金额（万美元）","当期出口数量（吨）","当期进口数量（吨）","一至当月出口金额（万美元）","一至当月进口金额（万美元）","一至当月出口数量（吨）","一至当月进口数量（吨）"], skiprows = 8)
'''
print(df_origin.head(10))
print(df_origin.tail(10))
print('读取的df：', len(df_origin.index))
'''
#新建一个dataframe，存放读取的dataframe
df = pd.DataFrame(columns = ["产品","类别","贸易方式","截至时间","时间","当期出口金额（万美元）","当期进口金额（万美元）","当期出口数量（吨）","当期进口数量（吨）","一至当月出口金额（万美元）","一至当月进口金额（万美元）","一至当月出口数量（吨）","一至当月进口数量（吨）"])
df['产品'] = df_origin['产品']
df['贸易方式'] = df_origin['贸易方式']
df['当期出口金额（万美元）'] = df_origin['当期出口金额（万美元）']
df['当期进口金额（万美元）'] = df_origin['当期进口金额（万美元）']
df['当期出口数量（吨）'] = df_origin['当期出口数量（吨）']
df['当期进口数量（吨）'] = df_origin['当期进口数量（吨）']
df['一至当月出口金额（万美元）'] = df_origin['一至当月出口金额（万美元）']
df['一至当月进口金额（万美元）'] = df_origin['一至当月进口金额（万美元）']
df['一至当月出口数量（吨）'] = df_origin['一至当月出口数量（吨）']
df['一至当月进口数量（吨）'] = df_origin['一至当月进口数量（吨）']
print(df.head(10))


print('新df：', len(df.index))
print(type(df['产品'][0]))
print(type(df['产品'][0]) == str)
print(df['产品'][0].startswith('月'))

#如果‘产品’列在i行有月份信息，则’截至时间'列的i行数据为该月份信息
for i in range(0, len(df.index)-1):
    if type(df['产品'][i]) == str:
        print("df['产品'][i]为str, i=", i)
        print(df['产品'][i])
        if df['产品'][i].startswith('月'):
            print(df['产品'][i])
            df['截至时间'][i] = df['产品'][i]
            print('有时间信息的行数为：', i)
    i += 1
    print('i+1=', i)

#填补产品列的空白
tempStr =''
for i in range(0, len(df.index)-1):
    if df['产品'][i] :
        print(i, 'not none', df['产品'][i])
        tempStr = df['产品'][i]
        i += 1
    else:
        df['产品'][i] = tempStr
        i += 1


print(df.head())
print(df.tail())
print(df.nunique())










#python D:\Github\customs_vegetable_data\test.py


















#python D:\Github\customs_vegetable_data\test.py
