import pandas as pd
import os
filename = r"C:\Users\koush\OneDrive\Desktop\python\m.csv"
data = pd.read_csv(filename).to_excel(filename.replace(".csv",".xlsx"))
#print(data)
column_name='FirstName'
unique_values=data[column_name].unique().sort_values(['FirstName'],ascending=[True])
for unique_value in unique_values:
    data_output=data[data[column_name].str.contains(unique_value)]
    output_path=os.path.join("output",unique_value+'.xlsx')
    data_output.to_excel(output_path,sheet_name=unique_value,index=False)


