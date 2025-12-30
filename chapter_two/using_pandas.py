import pandas as pd

df = pd.read_csv("new.csv")

# print(df)
# print(type(df))

df.info()

#view the data from the head  (default 5 ota dekhauxa)
df.head()
#view from the bottom 
df.tail()
#view a ranodm sample
df.sample()
#check for missing values
df.isnull().sum()
#adding a column
df["Provience"] = "koshi"
#write a csv file (yesle k garxa)
df.to_csv("new.csv", index=False)


