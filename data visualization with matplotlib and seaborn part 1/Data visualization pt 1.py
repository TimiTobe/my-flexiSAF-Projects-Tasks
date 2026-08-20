"""
Company Sales Data - Basic Matplotlib Line Plot and Scatter Plot
Data source: https://pynative.com/wp-content/uploads/2019/01/company_sales_data.csv

Requires: pandas, matplotlib
    pip install pandas matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
CSV_PATH = "company_sales_data.csv"
df = pd.read_csv(CSV_PATH)

months = df["month_number"].tolist()

# Basic Line Plot: Total profit over the months
def line_plot(df):
    plt.figure(figsize=(8, 5))
    plt.plot(months, df["total_profit"], marker="o", color="blue", linewidth=2)
    plt.title("Total Profit per Month")
    plt.xlabel("Month Number")
    plt.ylabel("Total Profit (Rs.)")
    plt.xticks(months)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("basic_line_plot.png", dpi=150)
    plt.show()


# Basic Scatter Plot: Total units sold vs. Total profit
def scatter_plot(df):
    plt.figure(figsize=(8, 5))
    plt.scatter(df["total_units"], df["total_profit"], color="crimson", s=80)
    plt.title("Total Units Sold vs. Total Profit")
    plt.xlabel("Total Units Sold")
    plt.ylabel("Total Profit (Rs.)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("basic_scatter_plot.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    line_plot(df)
    scatter_plot(df)