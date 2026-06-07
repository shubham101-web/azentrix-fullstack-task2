# Streamlit analytics dashboard

# Import required libraries
import streamlit as st, pandas as pd
from sqlalchemy import create_engine

# Dashboard title
st.title('Mini Data Lakehouse Dashboard')

# Create database connection
engine = create_engine('postgresql://postgres:postgres@db:5432/lakehouse')

# Read sales data from database
df = pd.read_sql('select * from fact_sales', engine)

# Display KPI metrics
st.metric('Total Revenue', float(df['revenue'].sum()))
st.metric('Orders', int(len(df)))

# Revenue trend visualization
st.subheader('Revenue Trend')
trend = df.groupby('order_date')['revenue'].sum()
st.line_chart(trend)

# Product-wise revenue visualization
st.subheader('Top Products')
st.bar_chart(df.groupby('product')['revenue'].sum())
