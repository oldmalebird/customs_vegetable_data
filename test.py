#观察数据集
import pandas as pd
#python D:\Github\customs_vegetable_data\test.py
docAddress = r"D:\Data\种植业司\全国蔬菜面积产量.xlsx"
df = pd.read_excel(docAddress, sheet_name='全国蔬菜面积与产量')
print(df.head())
print()
print(df.tail())

print()
df.info()
print()
print(df.describe())
print()
#检查重复数据
print('重复行数：', sum(df.duplicated()))
print("各列唯一值数量：")
print()
print(df.nunique())
print()
ncolumns = df.columns.size
for col in range(2):
    print(df.ix[:, col].unique())
    print()

#python D:\Github\customs_vegetable_data\test.py
