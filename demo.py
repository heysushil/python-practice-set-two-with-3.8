import matplotlib.pyplot as plt
import pandas as pd

filename = 'Var_plot.xlsx'
data = pd.read_excel(filename, sheet_name=0, index_col=0)
getExcelData = data.head().plot()

# getExcelData = data.head().plot(kind="barh")

# print(getExcelData)
# print(getExcelData.shape)

# columns = getExcelData[['Gene', 'Unique Variants']]

# print(columns)
# print(getExcelData)
# plt.plot()
plt.show()