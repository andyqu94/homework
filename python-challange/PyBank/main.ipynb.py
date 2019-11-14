import pandas as pd 
import sys

filepath = "Resources/budget_data.csv"

df = pd.read_csv(filepath)

total_month = len(df["Date"].unique())

total = df["Profit/Losses"].sum()

df2 = df["Profit/Losses"].diff()

average_change = df2.mean()

greatest_increase = df2.max()

greatest_decrease = df2.min()

df3 = df2.sort_values(ascending=True)

df4 = pd.concat([df,df3],axis=1)

greatest_month = df4.iloc[44]["Date"]
lowest_month = df4.iloc[25]["Date"]

filename  = open("analysis",'w')
sys.stdout = filename

print("Financial Analysis")
print("-------------------------")
print("Total Month:",total_month)
print("Total: $",total)
print("Average Change: $", average_change)
print("Greatest Increase in Profits:" +str(greatest_month)+"($"+str(greatest_increase)+")")
print("Greatest Decrease in Profits:" +str(lowest_month)+"($"+str(greatest_decrease)+")")