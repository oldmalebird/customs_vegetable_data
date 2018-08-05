#提取贸易方式进出口数据
import pandas as pd
#python D:\Github\customs_vegetable_data\test.py

#读取原始数据
docAddress = r'D:\Data\信息中心进出口\原始数据\2018\蔬菜水果_贸201801-201803.xls'
df_origin = pd.read_excel(
    docAddress,
    sheet_name='Report',
    header=None,
    names=[
        "产品", "贸易方式", "当期出口金额（万美元）", "当期进口金额（万美元）", "当期出口数量（吨）", "当期进口数量（吨）",
        "一至当月出口金额（万美元）", "一至当月进口金额（万美元）", "一至当月出口数量（吨）", "一至当月进口数量（吨）"
    ],
    skiprows=8)
'''
print(df_origin.head(10))
print(df_origin.tail(10))
print('读取的df：', len(df_origin.index))
'''
#新建一个dataframe，存放读取的dataframe
df = pd.DataFrame(columns=[
    "产品", "贸易方式", "截至时间", "时间", "当期出口金额（万美元）", "当期进口金额（万美元）", "当期出口数量（吨）",
    "当期进口数量（吨）", "一至当月出口金额（万美元）", "一至当月进口金额（万美元）", "一至当月出口数量（吨）", "一至当月进口数量（吨）"
])
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
for i in range(0, len(df.index)):
    if type(df['产品'][i]) == str:
        #print("df['产品'][i]为str, i=", i)
        #print(df['产品'][i])
        if df['产品'][i].startswith('月'):
            #print(df['产品'][i])
            df['截至时间'][i] = df['产品'][i]
            print('有时间信息的行数为：', i)
    i += 1
    #print('i+1=', i)

#填补产品列的空白
#这种改变列的方法不行
#df['产品'] = df['产品'].astype(string)
tempStr = ''
for i in range(0, len(df.index)):
    if type(df['产品'][i]) == str:
        #print(type(len(df['产品'][i])))
        tempStr = df['产品'][i]
        #print('tempStr新赋值为：', tempStr)
        i += 1
    else:
        df['产品'][i] = tempStr
        #print("测试df['产品'][i] = tempStr是否赋值成功", df['产品'][i] )
        i += 1

#填补截至时间列的空白
tempMonth = ''
for i in range(0, len(df.index)):
    if type(df['截至时间'][i]) == str:
        #print(type(len(df['产品'][i])))
        tempMonth = df['截至时间'][i]
        #print('tempStr新赋值为：', tempMonth)
        i += 1
    else:
        df['截至时间'][i] = tempMonth
        #print("测试df['截至时间'][i] = tempStr是否赋值成功", df['截至时间'][i] )
        i += 1

#填补时间列并删除时间列的空格
df['时间'] = df['截至时间'].str.slice(10)
df['时间'] = df['时间'].str.replace('年', '-')
df['时间'] = df['时间'].str.replace(' ', '')
df['时间'] = df['时间'].str.replace('月', '-1')

#转成时间格式不成功
df['时间'] = pd.to_datetime(df['时间']).dt.date

#删除无意义行
df.dropna(subset=['贸易方式'], inplace=True)

#填补类别信息
vegCatAddress = r"D:\Data\信息中心进出口\数据处理\vlookup.xlsx"
vegCat = pd.read_excel(vegCatAddress, sheet_name='产品分类')
print(vegCat.head())
print(vegCat.tail())
df_merge = pd.merge(df, vegCat, how='left')

#将类别移到第二列
cols = list(df_merge)
cols.insert(1, cols.pop(cols.index('类别')))
df_merge = df_merge.ix[:, cols]
'''
print('以下是df的情况：')
print(df.head())
print(df.tail())
print(df.describe())
#print(df.nunique())

print('以下是df_merge的情况：')
print(df_merge.head())
print(df_merge.tail())
print(df_merge.describe())
'''
print(df_merge.head())
writer = r"C:\Users\cva_b\Desktop\test.xlsx"
df_merge.to_excel(writer, sheet_name='Cleaned含贸易方式合计')

#python D:\Github\customs_vegetable_data\test.py
