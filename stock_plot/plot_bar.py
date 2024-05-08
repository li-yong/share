import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('stock_data.csv')

# Calculate the change in price (up/down) for each row
df['Change'] = df['Close'] - df['Open']

# Create a new column for the middle price
df['Middle'] = (df['High'] + df['Low']) / 2

# Plot the date on the x-axis and the close price on the y-axis
plt.plot(df['Date'], df['Close'], color='black', linewidth=2)

# Plot the upper and lower price boundaries
plt.plot(df['Date'], df['High'], color='red', linewidth=1)
plt.plot(df['Date'], df['Low'], color='green', linewidth=1)

# Plot the middle price as a thicker line
plt.plot(df['Date'], df['Middle'], color='black', linewidth=4)

# Add labels and formatting
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price Chart')
plt.grid(True)

# Set the y-axis range to auto-adjust
plt.ylim(ymin=df['Low'].min(), ymax=df['High'].max())

# Show the plot
plt.show()