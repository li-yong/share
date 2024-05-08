import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('stock_data.csv')

# Create a new column to indicate whether the price is rising or falling
df['Price Change'] = df['Close'].diff()
df['Price Change'] = df['Price Change'].apply(lambda x: 'Rising' if x > 0 else 'Falling')

# Create a line plot of the closing prices
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], label='Close', color='black')

# Create a thicker line plot of the high and low prices
plt.fill_between(df['Date'], df['High'], df['Low'], alpha=0.3)

# Create a line plot of the closing prices with different colors based on price change
for index, row in df.iterrows():
    if row['Price Change'] == 'Rising':
        color = 'green'
    else:
        color = 'red'
    plt.plot([row['Date'], row['Date']], [row['Close'], row['Close']], color=color, linewidth=2)

# Add a legend and labels
plt.legend(['Close', 'High-Low', 'Rising Price', 'Falling Price'])
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Prices')

# Show the plot
plt.show()
