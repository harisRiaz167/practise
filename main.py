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
figure_brands = px.bar(brand_counts, x='brand', y='count')

#bar graph for Top 5 Categories
top_categories = purchase_subset['category_code'].value_counts().head(5).reset_index()
top_categories.columns = ['category','count']
categories_figure = px.bar(top_categories, x='category', y='count', color='category')

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
end_date = pd.to_datetime('today')  # Use today's date as the end date
date_range = pd.date_range(start=start_date, end=end_date)

# Assign the date range to the 'date' column in the DataFrame
apple_purchase['date'] = date_range[:len(apple_purchase)]
apple_purchase = apple_purchase[['brand','date','price']]
huawei_purchase = purchase_subset[purchase_subset ['brand']=='huawei']
huawei_purchase = huawei_purchase.drop(['date'],axis=1)
start_date = '06-09-2022'
end_date = pd.to_datetime('today')  # Use today's date as the end date
date_range = pd.date_range(start=start_date, end=end_date)

# Assign the date range to the 'date' column in the DataFrame
huawei_purchase['date'] = date_range[:len(huawei_purchase)]
huawei_purchase = huawei_purchase[['brand','date','price']]
# fig_applesale = px.line(apple_purchase, x="date", y="price")
# fig_huaweisale = px.line(huawei_purchase, x="date", y="price")
farme = [apple_purchase, huawei_purchase]
result = pd.concat(farme)
resultfig = px.line(result, x="date", y="price", color="brand")
st.plotly_chart(resultfig)
