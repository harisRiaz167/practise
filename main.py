import pandas as pd
import plotly.express as px
import streamlit as st

#streamlit page config
st.set_page_config(page_title='Sales Chart',  layout="wide")

df = pd.read_csv('final.csv')

# dataset for purchase items
purchase_subset = df[df['event_type'] == 'purchase']

# bar graph Top 5 brands dataset
brand_counts = purchase_subset['brand'].value_counts().reset_index()
brand_counts.columns = ['brand', 'count']
brand_counts = brand_counts.head(5)
figure_brands = px.bar(brand_counts, x='brand', y='count', title='Top Brands')

#bar graph for Top 5 Categories
top_categories = purchase_subset['category_code'].value_counts().head(5).reset_index()
top_categories.columns = ['category','count']
categories_figure = px.bar(top_categories, x='category', y='count', color='category', title='Top Category')

st.title('Sales Chart')
st.markdown('visulization for the sales data, important insight provided')

card1, card2, card3, = st.columns(3)
card1.metric("Views", "59685")
card2.metric("Cart", "1085")
card3.metric("Purchase", "1216")

fig1, fig2 = st.columns(2)
with fig1:
    st.plotly_chart(figure_brands)
with fig2:
    st.plotly_chart(categories_figure)

# line graph for apple and huawei sale
apple_purchase = purchase_subset[purchase_subset ['brand']=='apple']
apple_purchase = apple_purchase.drop(['date'],axis=1)
start_date = '06-09-2022'
end_date = pd.to_datetime('today')  
date_range = pd.date_range(start=start_date, end=end_date)
apple_purchase['date'] = date_range[:len(apple_purchase)]
apple_purchase = apple_purchase[['brand','date','price']]

huawei_purchase = purchase_subset[purchase_subset ['brand']=='huawei']
huawei_purchase = huawei_purchase.drop(['date'],axis=1)
start_date = '06-09-2022'
end_date = pd.to_datetime('today') 
date_range = pd.date_range(start=start_date, end=end_date)
huawei_purchase['date'] = date_range[:len(huawei_purchase)]
huawei_purchase = huawei_purchase[['brand','date','price']]
frame = [apple_purchase, huawei_purchase]
result = pd.concat(frame)

result_fig = px.line(result, x="date", y="price", color="brand", title='Brand Sales')
st.plotly_chart(result_fig)

# line graph for sales
sales_data = purchase_subset.drop(['date'],axis=1)
sales_data = sales_data.groupby('brand')['price'].sum()
sales_data = pd.DataFrame({'brand':sales_data.index, 'sales':sales_data.values}) 
start_date = '06-09-2022'
end_date = pd.to_datetime('today')  # Use today's date as the end date
date_range = pd.date_range(start=start_date, end=end_date)
sales_data['date'] = date_range[:len(sales_data)]

fig_sales = px.line(sales_data, x="date", y="sales", title='Sales')
st.plotly_chart(fig_sales)