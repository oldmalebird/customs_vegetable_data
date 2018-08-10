#提取海关进出口数据
import pandas as pd
#python D:\Github\customs_vegetable_data\提取国家进出口数据（2000-2011）.py

#读取原始数据
docAddress = r"D:\Data\from zzh\入世10年蔬菜进出口贸易情况（总表）.xlsx"
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
    '产品', '类别', "国家（数据源所用名称）", "截至时间", "时间", "当期出口数量（吨）", "出口数量比同期（吨）",
    "当期出口金额（万美元）", "出口金额比同期（万美元）", "当期进口数量（吨）", "进口数量比同期（吨）", "当期进口金额（万美元）",
    "进口金额比同期（万美元）", "净出口金额（万美元）"
])
df['国家（数据源所用名称）'] = df_origin['国家（数据源所用名称）']
df['当期出口数量（吨）'] = df_origin['当期出口数量（吨）']
df['出口数量比同期（吨）'] = df_origin['出口数量比同期（吨）']
df['当期出口金额（万美元）'] = df_origin['当期出口金额（万美元）']
df['出口金额比同期（万美元）'] = df_origin['出口金额比同期（万美元）']
df['当期进口数量（吨）'] = df_origin['当期进口数量（吨）']
df['进口数量比同期（吨）'] = df_origin['进口数量比同期（吨）']
df['当期进口金额（万美元）'] = df_origin['当期进口金额（万美元）']
df['进口金额比同期（万美元）'] = df_origin['进口金额比同期（万美元）']
df['净出口金额（万美元）'] = df_origin['净出口金额（万美元）']
df['产品'] = df['产品'].fillna('蔬菜')
df['类别'] = df['类别'].fillna('产品大类')

print(df.head(5))
print('新df的行数：', len(df.index))
print(type(df['国家（数据源所用名称）'][3]))
print(df['国家（数据源所用名称）'][2].startswith('年'))

#如果‘国家（数据源所用名称）’列在i行有月份信息，则’截至时间'列的i行数据为该月份信息
for i in range(0, len(df.index)):
    if type(df['国家（数据源所用名称）'][i]) == str:
        if df['国家（数据源所用名称）'][i].startswith('年'):
            df['截至时间'][i] = df['国家（数据源所用名称）'][i]
            print('有时间信息的行数为：', i)
    i += 1
'''
#填补国家（数据源所用名称）列的空白
tempStr = ''
for i in range(0, len(df.index)):
    if type(df['国家（数据源所用名称）'][i]) == str:
        tempStr = df['国家（数据源所用名称）'][i]
        i += 1
    else:
        df['国家（数据源所用名称）'][i] = tempStr
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

#删除国家列中的含年、吨、蔬菜的所在行
toDelete = []
for i in range(0, len(df.index)):
    if type(df['国家（数据源所用名称）'][i]) == str:
        if df['国家（数据源所用名称）'][i].startswith(
                '年') or df['国家（数据源所用名称）'][i].startswith(
                    '吨') or df['国家（数据源所用名称）'][i].startswith('蔬菜'):
            print('删除的有时间信息的行数为：', i)
            #print(df.loc[[i]])
            toDelete.append(i)
            i += 1
print('删除年、吨、蔬菜行前的行数：', len(df.index))
print(len(toDelete), toDelete)
df = df.drop(toDelete)
#删除无意义行
print('删除年、吨、蔬菜行后的行数：', len(df.index))
df.dropna(subset=['国家（数据源所用名称）'], inplace=True)
print('删除无意义行后的行数：', len(df.index))
#删除重复项
df.drop_duplicates(keep='first', inplace=True)
print('删除重复项后的行数：', len(df.index))
print()

#填补国家标准名称
vlookupAddress = r"D:\Data\信息中心进出口\数据处理\vlookup.xlsx"
countryName = pd.read_excel(
    vlookupAddress, sheet_name='国家标准名称', usecols=[0, 1])
print(countryName.head())
print(countryName.tail())
df_merge = pd.merge(df, countryName, how='left')
print(df_merge.head(50))
print(df_merge.tail(50))

#将国家标准名称移到第四列
cols = list(df_merge)
cols.insert(3, cols.pop(cols.index('国家标准名称')))
df_merge = df_merge.ix[:, cols]
print('填补国家标准名称后的行数', len(df_merge.index))

#添加不含合计的数据
df_no_sum = df_merge.loc[df_merge['国家标准名称'] != '国家合计']
print('不含合计数的行数：', len(df_no_sum.index))

writer = pd.ExcelWriter(r"D:\Data\信息中心进出口\数据处理\汇总\国_2000-2001.xlsx")
df_no_sum.to_excel(writer, sheet_name='Cleaned', index=False)
df_merge.to_excel(writer, sheet_name='Cleaned含国家合计', index=False)

#python D:\Github\customs_vegetable_data\提取国家进出口数据（2000-2011）.py
