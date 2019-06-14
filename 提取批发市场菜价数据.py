#提取批发市场菜价信息
import pandas as pd

#读取原始数据
docAddress = r"D:\Desktop\测试批发市场原始文件.xls"
df = pd.read_excel(
    docAddress,
    sheet_name='Report',
    header=None,
    names=["蔬菜", "省", "市", "批发市场", "日期", "大宗价", "最高价", "最低价", "交易量"],
    skiprows=11,
    usecols='A:I')

#如果‘产品’列在i行有月份信息，则’截至时间'列的i行数据为该月份信息
for i in range(0, len(df.index)):

    df['日期'] = df['日期'].str.slice(start=1)
    i += 1

#转成时间格式
#df['日期'] = pd.to_datetime(df['日期']).dt.date

writer = pd.ExcelWriter(r"D:\Desktop\测试批发市场.xlsx")
df.to_excel(writer, sheet_name='Cleaned', index=False)

writer.save()
writer.close()
