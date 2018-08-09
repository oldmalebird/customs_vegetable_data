#提取海关进出口数据
import pandas as pd
#python D:\Github\customs_vegetable_data\提取国家进出口数据.py

#读取原始数据
docAddress = r'D:\Data\信息中心进出口\原始数据\2018\蔬菜水果_国201801-201803.xls'
df_origin = pd.read_excel(
    docAddress,
    sheet_name='分国别',
    header=None,
    names=[
        "国家（数据源所用名称）", "当期出口数量（吨）", "出口数量比同期（吨）", "当期出口金额（万美元）",
        "出口金额比同期（万美元）", "当期进口数量（吨）", "进口数量比同期（吨）", "当期进口金额（万美元）",
        "进口金额比同期（万美元）", "净出口金额（万美元）"
    ],
    skiprows=8)
#出口金额比同期（美元）和进口金额比同期（美元）单位是不是错了？
'''
print(df_origin.head(10))
print(df_origin.tail(10))
print('读取的df：', len(df_origin.index))
'''
#新建一个dataframe，存放读取的dataframe
df = pd.DataFrame(columns=[
    "国家（数据源所用名称）", "截至时间", "时间", "当期出口数量（吨）", "出口数量比同期（吨）", "当期出口金额（万美元）",
    "出口金额比同期（万美元）", "当期进口数量（吨）", "进口数量比同期（吨）", "当期进口金额（万美元）", "进口金额比同期（万美元）",
    "净出口金额（万美元）"
])
df['国家（数据源所用名称）'] = df_origin['国家（数据源所用名称）']
df['当期出口数量（吨）'] = df_origin['当期出口数量（吨）']
df['出口数量比同期（吨）'] = df_origin['出口数量比同期（吨）']
df['当期出口金额（万美元）'] = df_origin['当期出口金额（万美元）']
df['出口金额比同期（万美元）'] = df_origin['出口金额比同期（万美元）']
df['当期进口数量'] = df_origin['当期进口数量']
df['进口数量比同期（吨）'] = df_origin['进口数量比同期（吨）']
df['当期进口金额（万美元）'] = df_origin['当期进口金额（万美元）']
df['进口金额比同期（万美元）'] = df_origin['进口金额比同期（万美元）']
df['净出口金额（万美元）'] = df_origin['净出口金额（万美元）']

print(df.head(5))
print('新df的行数：', len(df.index))
print(type(df['产品'][0]) == str)
print(df['产品'][0].startswith('月'))

#如果‘国家（数据源所用名称）’列在i行有月份信息，则’截至时间'列的i行数据为该月份信息
for i in range(0, len(df.index)):
    if type(df['产品'][i]) == str:
        if df['产品'][i].startswith('月'):
            df['截至时间'][i] = df['产品'][i]
            print('有时间信息的行数为：', i)
    i += 1
'''
#填补国家（数据源所用名称）列的空白
tempStr = ''
for i in range(0, len(df.index)):
    if type(df['产品'][i]) == str:
        tempStr = df['产品'][i]
        i += 1
    else:
        df['产品'][i] = tempStr
        i += 1
'''
#填补截至时间列的空白
tempMonth = ''
for i in range(0, len(df.index)):
    if type(df['截至时间'][i]) == str:
        tempMonth = df['截至时间'][i]
        i += 1
    else:
        df['截至时间'][i] = tempMonth
        i += 1

#填补时间列并删除时间列的空格
df['时间'] = df['截至时间'].str.slice(10)
df['时间'] = df['时间'].str.replace('年', '-')
df['时间'] = df['时间'].str.replace(' ', '')
df['时间'] = df['时间'].str.replace('月', '-1')
#转成时间格式
df['时间'] = pd.to_datetime(df['时间']).dt.date

#删除无意义行
df.dropna(subset=['国家（数据源所用名称）'], inplace=True)
print('删除无意义行后的行数：', len(df.index))

#删除重复项
df.drop_duplicates(keep='first', inplace=True)
print('删除重复项后的行数：', len(df.index))

#删除国家列中的截止时间所在行
for i in range(0, len(df.index)):
    if df['国家（数据源所用名称）'][i].startswith('月'):
        df.drop([i])
        print('删除的有时间信息的行数为：', i)
    i += 1

#填补国家标准名称
vlookupAddress = r"D:\Data\信息中心进出口\数据处理\vlookup.xlsx"
countryName = pd.read_excel(
    vlookupAddress, sheet_name='国家标准名称', usecols=[0, 1])
print(countryName.head())
print(countryName.tail())
df_merge = pd.merge(df, countryName, how='left')
print(df_merge.head())

#将国家标准名称移到第四列
cols = list(df_merge)
cols.insert(3, cols.pop(cols.index('国家标准名称')))
df_merge = df_merge2ix[:, cols]
print('填补国家标准名称后的行数', len(df_merge.index))

#添加不含合计的数据
df_no_sum = df_merge.loc[df_merge2['国家标准名称'] != '国家合计']
print('不含合计数的行数：', len(df_no_sum.index))

writer = pd.ExcelWriter(r"C:\Users\cva_b\Desktop\test.xlsx")
df_no_sum.to_excel(writer, sheet_name='Cleaned', index=False)
df_merge.to_excel(writer, sheet_name='Cleaned含国家合计', index=False)

#python D:\Github\customs_vegetable_data\提取国家进出口数据.py
