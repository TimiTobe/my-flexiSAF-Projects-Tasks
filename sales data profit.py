#sales  

"""
Company Sales Data - Matplotlib Exercises
Data source: https://pynative.com/wp-content/uploads/2019/01/company_sales_data.csv

Exercise 1: Read Total profit of all months and show it using a line plot.
Exercise 2: Read data for Bathing soap and facewash of all months and
            display it using the Subplot.

Requires: pandas, matplotlib
    pip install pandas matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# Load the data
# ---------------------------------------------------------------------
# If you have internet access, you can read directly from the URL:
#   df = pd.read_csv("https://pynative.com/wp-content/uploads/2019/01/company_sales_data.csv")
# Otherwise, point this at a local copy of the CSV.
CSV_PATH = "company_sales_data.csv"
df = pd.read_csv(CSV_PATH)

months = df["month_number"].tolist()

# ---------------------------------------------------------------------
# Exercise 1: Total profit of all months - Line plot
# ---------------------------------------------------------------------
def plot_total_profit(df):
    profit = df["total_profit"].tolist()

    plt.figure(figsize=(8, 5))
    plt.plot(months, profit, label="Total profit", marker="o", linewidth=2, color="blue")
    plt.xlabel("Month Number")
    plt.ylabel("Total Profit (Rs.)")
    plt.title("Company Total Profit per Month")
    plt.xticks(months)
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("exercise1_total_profit_lineplot.png", dpi=150)
    plt.show()


# ---------------------------------------------------------------------
# Exercise 2: Bathing soap & facewash of all months - Subplots
# ---------------------------------------------------------------------
def plot_bathingsoap_facewash_subplots(df):
    bathing_soap = df["bathingsoap"].tolist()
    facewash = df["facewash"].tolist()

    fig, axes = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

    axes[0].plot(months, bathing_soap, marker="o", color="green", label="Bathing soap")
    axes[0].set_title("Bathing Soap Sales per Month")
    axes[0].set_ylabel("Units Sold")
    axes[0].grid(True)
    axes[0].legend()

    axes[1].plot(months, facewash, marker="o", color="orange", label="Facewash")
    axes[1].set_title("Facewash Sales per Month")
    axes[1].set_xlabel("Month Number")
    axes[1].set_ylabel("Units Sold")
    axes[1].set_xticks(months)
    axes[1].grid(True)
    axes[1].legend()

    plt.tight_layout()
    plt.savefig("exercise2_bathingsoap_facewash_subplots.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    plot_total_profit(df)
    plot_bathingsoap_facewash_subplots(df)
