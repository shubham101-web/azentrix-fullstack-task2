# Load curated Parquet data into PostgreSQL analytics tables

# Import required libraries
import pandas as pd
from sqlalchemy import create_engine

# Create PostgreSQL database connection
engine = create_engine("postgresql://postgres:postgres@localhost:5432/lakehouse")

# Load sales dataset into fact_sales table
pd.read_parquet('data/curated/sales.parquet').to_sql(
    'fact_sales', engine, if_exists='replace', index=False
)

# Load users dataset into dim_users table
pd.read_parquet('data/curated/users.parquet').to_sql(
    'dim_users', engine, if_exists='replace', index=False
)

# Log completion message
print('Loaded')
