import pandas as pd
import numpy as np

data=pd.read_csv('data.csv')

Obama=data[data.cand_nm.str.contains('Obama, Barack')]
McCain=data[data.cand_nm.str.contains('McCain')]

print (Obama.describe())
print (McCain.describe())

pd.merge(Obama, McCain, on='contb_receipt_dt')

ObamaCity=Obama.groupby('contbr_city').sum()
print (ObamaCity.describe())
