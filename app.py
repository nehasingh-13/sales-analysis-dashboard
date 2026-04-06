import streamlit as st
import pandas as pd

# Set page configuration for a premium look
st.set_page_config(page_title="Sales Dashboard", page_icon="📈", layout="wide")

# Title and Description
st.title("📊 Superstore Sales Analysis Dashboard")
st.markdown("""
Welcome to the interactive version of our data! 
Use the dropdown menu on the left side to filter the charts.
""")

# Load the data
# We use @st.cache_data so the dashboard doesn't re-read the Excel file every time you click a button
@st.cache_data
def load_data():
    df = pd.read_excel('Sample - Superstore.xls', sheet_name='Orders')
    # Make sure Order Date is treated as a Date, not text
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    return df

# Load it into our virtual spreadsheet
df = load_data()

# Sidebar for interactive filtering
st.sidebar.header("Filter Options 🎯")

# Select a Region
regions = ["All Regions"] + list(df['Region'].unique())
selected_region = st.sidebar.selectbox("Select a Region", regions)

# If they picked a specific region, filter the data
if selected_region != "All Regions":
    filtered_df = df[df['Region'] == selected_region]
else:
    filtered_df = df

# Top Level Metrics (The big numbers!)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Sales", f"${filtered_df['Sales'].sum():,.0f}")
with col2:
    st.metric("Total Profit", f"${filtered_df['Profit'].sum():,.0f}")
with col3:
    st.metric("Total Orders", f"{filtered_df.shape[0]:,}")

st.markdown("---")

# Layout: Two columns for our charts
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("🏆 Sales & Profit by Category")
    # Same groupby logic we learned in the notebook!
    cat_summary = filtered_df.groupby('Category')[['Sales', 'Profit']].sum()
    st.bar_chart(cat_summary)

with chart_col2:
    st.subheader("🔥 Top 10 Products by Sales")
    # Same top 10 logic!
    top_products = filtered_df.groupby('Product Name')['Sales'].sum().nlargest(10)
    st.bar_chart(top_products)

st.markdown("---")

# The Brand New Feature: Line Chart for Sales Over Time
st.subheader("📈 Sales Over Time (Monthly)")

# We group by the Order Date and sum the sales, grouping it by Month ('ME')
time_series = filtered_df.set_index('Order Date').resample('ME')['Sales'].sum()
st.line_chart(time_series)

st.markdown("---")
st.caption("Built with 💙 using Python & Streamlit")
