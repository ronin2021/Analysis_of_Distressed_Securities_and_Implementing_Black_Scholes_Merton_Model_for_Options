# Sector Analysis Throughout the Pandemic: Airline, Hospitality, Cruiseship, and Restaurant Industries and Implementing Black-Scholes-Merton Model for Options

## Team: Indrajith Senevirathne, Jamel Harvey, Matthew Willson, Malkebu Moore, and Nicholas DePalma

## Project Description: 

Sector analysis of airline, hospitality, cruiseship, and restaurant stocks before, during, and after the Covid-19 pandemic. Determine and visualize which stocks performed best throughout the period 1/1/18 to 6/30/21. Performance will be measured against the S&P 500.

    *   Airline Stocks: Delta, American Airlines
    *   Hospitality Stocks: Hilton, Marriott
    *   Cruiseship Stocks: Carnival, Royal Caribbean 
    *   Restaurant Stocks: Dine Brands Global, Mcdonalds 

## Research Questions to be Answered:

    * What sector had the largest economic impact due to the instability of the market?
    * What sector performed the best/worst throughout the pandemic?
    * How did each sector perform compared to the S&P 500?

## Datasets 

    * Daily closing prices of each stock from January 2018 to June 2021. 

## Breakdown of Tasks

    1)  Create and clean price data within google sheets using the google finance function; convert spreadsheets into CSV files. 
    2)  Read CSV files into Python and create individual Pandas dataframes for each stock. 
    3)  Create Pandas dataframes showing daily returns of each stock using the pct_change function. 
    4)  Concatenate daily returns dataframes into one dataframe; visualize the performance of all stocks on one graph. 
    5)  Create cumulative returns for each stock for the cumulative returns dataframe.
    6)  Visualize cumulative returns dataframe and conduct analysis.
    7)  Calculate and visualize the standard deviation of each stock. 
    5)  Calculate beta for each stock on a rolling basis throughout the pandemic.
    6)  Calculate Sharpe ratios for each stock on a rolling basis throughout the pandemic. 
    7)  Calculate and visualize reward to risk ratios for each stock.
    8)  Incorporate SciPy and Mibian libraries to utilize the Black Scholes formula for options and implied volatility analysis
    9)  Run time series analysis of Nifty 50 index fund call options and implied volatility to better understand investor's outlook on the market during the pandemic. 

## Data Visualization
 ![Cumulative Returns Visualization](https://user-images.githubusercontent.com/83780964/126245902-be1ca41a-d591-4257-b44f-552008c8912b.png)
