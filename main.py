import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('final.csv')

# dataset for purchase items
purchase_subset = df[df['event_type'] == 'purchase']

# bar graph Top 5 brands dataset
brand_counts = purchase_subset['brand'].value_counts().reset_index()
brand_counts.columns = ['brand', 'count']
brand_counts = brand_counts.head(5)
figure_brands = px.bar(brand_counts, x='brand', y='count')

st.title('Sales Chart')

fig1, fig2 = st.columns(2)

with fig1:
    st.plotly_chart(figure_brands)