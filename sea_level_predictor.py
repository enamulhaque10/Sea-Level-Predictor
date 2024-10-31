
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

#1 Load Data set
df = pd.read_csv('epa-sea-level.csv')

# 2. Function to create the sea level predictor plot

def draw_plot():
    plt.figure(figsize=(10, 5))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Original data')

    # Perform linear regression on the entire dataset

    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_pred_all = res_all.slope * years_extended + res_all.intercept
    plt.plot(years_extended, sea_level_pred_all, 'r', label='Fitted line (1880-2050)')

    # Perform linear regression on the data from 2000 onwards

    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_level_pred_recent = res_recent.slope * years_recent + res_recent.intercept
    plt.plot(years_recent, sea_level_pred_recent, 'g', label='Fitted line (2000-2050)')


    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level (inches)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig('sea_level_plot.png')
    plt.show()

draw_plot()
