# Transform raw data into curated Parquet datasets

# Import required libraries
import pandas as pd, os, json

# Create curated data directory
os.makedirs('data/curated', exist_ok=True)

# Read sales CSV data
sales = pd.read_csv('data/raw/csv/sales.csv')

# Calculate revenue for each order
sales['revenue'] = sales['quantity'] * sales['price']

# Save transformed sales data as Parquet
sales.to_parquet('data/curated/sales.parquet', index=False)

# Read user data from JSON file
users = pd.read_json('data/raw/api/users.json')

# Keep only required user columns and save as Parquet
users[['id', 'name', 'email']].to_parquet('data/curated/users.parquet', index=False)
