import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Total Sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# Highest sales day
highest_day = df.loc[df["Sales"].idxmax()]
print("\nHighest Sales Day:\n", highest_day)

# Sales Trend (Date-wise)
sales_trend = df.groupby("Date")["Sales"].sum()

# Visualization - Line Chart
plt.figure()
sales_trend.plot(kind="line", marker='o')
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.savefig("line_chart.png")

# Visualization - Bar Chart (Region-wise)
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure()
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.savefig("bar_chart.png")

print("\nCharts saved successfully!")
