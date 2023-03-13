import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
data=pd.read_csv("final_assi_python.csv")
df=pd.DataFrame(data)
df.dropna()
g1=df.groupby(["zip_code","store_name"], as_index=False).agg(Total_sales_per_store=("sale_dollars","sum"))
g2=df.groupby(["zip_code","item_description", "store_name"], as_index=False).agg({"bottles_sold": "sum", "sale_dollars": "sum"})
g3=g1.merge(g2, on=['zip_code', "store_name"], how='outer')
g3["Percentage_of_sales"]=g3["sale_dollars"]/g3["Total_sales_per_store"]*100
f=g3.groupby(["zip_code"], as_index=False).agg('max')
plt.title("Most Bottles Sold per Zip Code")
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")
plt.scatter(f.zip_code,f.bottles_sold,c=np.random.rand(len(f.zip_code)))
plt.show()
