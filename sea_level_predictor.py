import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit (1880–present) using numpy.polyfit
    slope1, intercept1 = np.polyfit(df["Year"], df["CSIRO Adjusted Sea Level"], 1)
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, intercept1 + slope1 * years_extended, 'r', label='Best fit (1880–2014)')

    # Create second line of best fit (2000–present) using numpy.polyfit
    df_recent = df[df["Year"] >= 2000]
    slope2, intercept2 = np.polyfit(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"], 1)
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, intercept2 + slope2 * years_recent, 'g', label='Best fit (2000–2014)')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return for testing
    plt.savefig("sea_level_plot.png")
    return plt.gca()
