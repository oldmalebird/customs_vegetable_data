#提取海关进出口数据
import pandas as pd
#python D:\Github\customs_vegetable_data\提取海关进出口数据.py

#读取原始数据
docAddress = r'D:\Data\信息中心进出口\原始数据\2018\蔬菜水果_关201801-201803.xls'
df_origin = pd.read_excel(
    docAddress,
    sheet_name='Report',
    header=None,
    names=[
        "产品", "海关", "当期出口金额（万美元）", "当期进口金额（万美元）", "当期出口数量（吨）", "当期进口数量（吨）",
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
    "产品", "海关", "海关地点", "截至时间", "时间", "当期出口金额（万美元）", "当期进口金额（万美元）",
    "当期出口数量（吨）", "当期进口数量（吨）", "一至当月出口金额（万美元）", "一至当月进口金额（万美元）", "一至当月出口数量（吨）",
    "一至当月进口数量（吨）"
])
df['产品'] = df_origin['产品']
df['海关'] = df_origin['海关']
df['海关地点'] = df_origin['海关']
df['当期出口金额（万美元）'] = df_origin['当期出口金额（万美元）']
df['当期进口金额（万美元）'] = df_origin['当期进口金额（万美元）']
df['当期出口数量（吨）'] = df_origin['当期出口数量（吨）']
df['当期进口数量（吨）'] = df_origin['当期进口数量（吨）']
df['一至当月出口金额（万美元）'] = df_origin['一至当月出口金额（万美元）']
df['一至当月进口金额（万美元）'] = df_origin['一至当月进口金额（万美元）']
df['一至当月出口数量（吨）'] = df_origin['一至当月出口数量（吨）']
df['一至当月进口数量（吨）'] = df_origin['一至当月进口数量（吨）']
print(df.head(5))

print('新df的行数：', len(df.index))
print(type(df['产品'][0]) == str)
print(df['产品'][0].startswith('月'))

#如果‘产品’列在i行有月份信息，则’截至时间'列的i行数据为该月份信息
for i in range(0, len(df.index)):
    if type(df['产品'][i]) == str:
        if df['产品'][i].startswith('月'):
            df['截至时间'][i] = df['产品'][i]
            print('有时间信息的行数为：', i)
    i += 1

#填补产品列的空白
tempStr = ''
for i in range(0, len(df.index)):
    if type(df['产品'][i]) == str:
        tempStr = df['产品'][i]
        i += 1
    else:
        df['产品'][i] = tempStr
        i += 1

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
df.dropna(subset=['海关'], inplace=True)
print('删除无意义行后的行数：', len(df.index))

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
print('填补类别信息后的行数', len(df_merge.index))

#删除“蔬菜种子.”
df_merge = df_merge.loc[df_merge['产品'] != '蔬菜种子.']
print('删除‘蔬菜种子.’的行数：', len(df_merge.index))

#删除重复项
df_merge.drop_duplicates(keep='first', inplace=True)
print('删除重复项后的行数：', len(df_merge.index))

#删除海关地点中的“海关”、“关区”字样
df_merge['海关地点'] = df_merge['海关地点'].str.replace('海关', '')
df_merge['海关地点'] = df_merge['海关地点'].str.replace('关区', '')

#海关地点替换：“拱北”改为“珠海”，“黄埔”改为“广州”，“海口”改为“海口市”，以便数据可视化软件对该地点进行识别
df_merge['海关地点'] = df_merge['海关地点'].str.replace('拱北', '珠海')
df_merge['海关地点'] = df_merge['海关地点'].str.replace('海口', '海口市')
df_merge['海关地点'] = df_merge['海关地点'].str.replace('黄埔', '广州')

#添加不含合计的数据
df_no_sum = df_merge.loc[df_merge['海关地点'] != '关口合计']
print('不含合计数的行数：', len(df_no_sum.index))

writer = pd.ExcelWriter(r"C:\Users\cva_b\Desktop\test.xlsx")
df_no_sum.to_excel(writer, sheet_name='Cleaned', index=False)
df_merge.to_excel(writer, sheet_name='Cleaned含关口合计', index=False)

#python D:\Github\customs_vegetable_data\提取海关进出口数据.py
