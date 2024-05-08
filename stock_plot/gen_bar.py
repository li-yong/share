import csv
import random
from datetime import datetime, timedelta

# Function to generate random stock data
def generate_stock_data():
    date = datetime.now() - timedelta(days=random.randint(1, 365))
    open_price = round(random.uniform(100, 500), 2)
    high = open_price + round(random.uniform(0, 10), 2)
    low = open_price - round(random.uniform(0, 10), 2)
    close = round(random.uniform(low, high), 2)
    volume = random.randint(100000, 1000000)
    dividends = round(random.uniform(0, 5), 2)
    stock_splits = random.randint(0, 2)
    return [date.strftime('%Y-%m-%d'), open_price, high, low, close, volume, dividends, stock_splits]

# Generate 20 entries of stock data
stock_data = [generate_stock_data() for _ in range(20)]

# Write the data to a CSV file
csv_file = 'stock_data.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits'])  # Write header
    writer.writerows(stock_data)  # Write stock data entries

print(f"Stock data has been generated and saved to '{csv_file}'.")
