#观察数据集
import pandas as pd
#python D:\Github\customs_vegetable_data\test.py
docAddress = r"D:\Data\种植业司\全国蔬菜面积产量.xlsx"
df = pd.read_excel(docAddress, sheet_name='全国蔬菜面积与产量')
print(df.head())
print()
print(df.tail())
df["节目"] = "节目"
print(df.head())
