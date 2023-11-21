import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.balloons()

# Create a Streamlit app
st.title("E-Commerce Dashboard")

# Load data from GitHub
url = "https://raw.githubusercontent.com/fulazz/911-dashboard/main/shopping_new.csv"
df = pd.read_csv(url, low_memory=False)  # Add low_memory=False to handle DtypeWarning

# Visualize product category distribution
st.write("### Product Category Distribution:")
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='product_category_name', order=df['product_category_name'].value_counts().index)
plt.xlabel('Count')
plt.ylabel('Product Category')

# Disable the PyplotGlobalUseWarning
st.set_option('deprecation.showPyplotGlobalUse', False)

# Display the plot
st.pyplot()


# Display the raw data (optional)
if st.checkbox("Show Raw Data"):
    st.write("### Raw Data:")
    st.dataframe(df)

# Convert 'order_estimated_delivery_date' to datetime
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])

# Bar chart comparing seller_state and customer_state
fig1 = px.bar(df, x=['seller_state', 'customer_state'], title='Seller State vs Customer State')
st.plotly_chart(fig1)

# Line graph showing trend order purchase by month
df['month_year'] = pd.to_datetime(df['month_year'])
fig2 = px.line(df.groupby('month_year').size().reset_index(name='order_count'), x='month_year', y='order_count', title='Order Purchase Trend by Month')
st.plotly_chart(fig2)

# Bar chart showing top 5 product sells
top_products = df['product_category_name'].value_counts().head(5)
fig3 = px.bar(top_products, x=top_products.index, y=top_products.values, title='Top 5 Product Sells')
st.plotly_chart(fig3)

# Monthly income from variable price and order_estimated_delivery_date
monthly_income = df.groupby('month_year')['price'].sum().reset_index()
fig4 = px.bar(monthly_income, x='month_year', y='price', title='Monthly Income')
st.plotly_chart(fig4)

# Run the Streamlit app
st.pyplot()