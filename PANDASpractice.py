
import pandas as pd
import csv
df=pd.read_csv('digital_behaviour.csv') 
print(df.head())
print(df.tail())
print(df.describe())
print(df[["Instagram_Minutes","Date"]])
print(df["Instagram_Minutes"])
print("for Sum of Instagram Minutes")
print(df["Instagram_Minutes"].sum())
print(df["Instagram_Minutes"].mean())
print(df["YouTube_Minutes"].max())
print(df[df["Instagram_Minutes"]>100])
print(df[df["Study_Minutes"]>180])
print(df[df["Instagram_Minutes"]>df["Study_Minutes"]])
count=df[df["Instagram_Minutes"]>df["Study_Minutes"]]
print(count)

print("for sorting the data")
sorted_df=df.sort_values(by='Instagram_Minutes',ascending=False)
print(sorted_df.head())
print(df.sort_values(by='Study_Minutes',ascending=False).head())

print("for adding new columns")
df['Total_Screen_Time']=df['Instagram_Minutes']+df['YouTube_Minutes']+df['WhatsApp_Minutes']+df['LinkedIn_Minutes']
df['Screen_Hours']=df['Total_Screen_Time']/60
df['Digital_Balance']=df['Study_Minutes']/df['Total_Screen_Time']
def day_type(total_screen_time):
    if total_screen_time > 300:
       return 'Heavy'
    else:
       return 'Normal'
df['Day_Type']=df['Total_Screen_Time'].apply(day_type)
df['app_total']=df['Instagram_Minutes']+df['YouTube_Minutes']+df['WhatsApp_Minutes']+df['LinkedIn_Minutes']
print(df['app_total'])
print("Most time spent is:", df['Total_Screen_Time'].max())
print(df[df['Day_Type'] == 'Heavy'].count())
print(df['Study_Minutes'].idxmax())
print(df.loc[df['Day_Type']=='Heavy', 'Study_Minutes'])
print(df['Digital_Balance'].mean())
print(df['Digital_Balance'].max())

df.to_csv("Project1.csv")







