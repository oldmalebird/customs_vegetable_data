#提取贸易方式进出口数据
import pandas as pd
#python D:\Github\customs_vegetable_data\test.py

docAddress = r'D:\Data\信息中心进出口\原始数据\2018\蔬菜水果_贸201801-201803.xls'
df_origin = pd.read_excel(docAddress,sheet_name='Report', header = None, names = ["产品","贸易方式","当期出口金额（万美元）","当期进口金额（万美元）","当期出口数量（吨）","当期进口数量（吨）","一至当月出口金额（万美元）","一至当月进口金额（万美元）","一至当月出口数量（吨）","一至当月进口数量（吨）"], skiprows = 8)

print(df_origin.head(10))

df = pd.DataFrame(columns = ["产品","类别","贸易方式","截至时间","时间","当期出口金额（万美元）","当期进口金额（万美元）","当期出口数量（吨）","当期进口数量（吨）","一至当月出口金额（万美元）","一至当月进口金额（万美元）","一至当月出口数量（吨）","一至当月进口数量（吨）"])

print(df.head())

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

df['截至时间']=1





























#python D:\Github\customs_vegetable_data\test.py
