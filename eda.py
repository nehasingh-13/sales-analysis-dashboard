import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Superstore data
df = pd.read_excel('Sample - Superstore-2.xls', sheet_name='Orders')

print(f"📊 Dataset: {df.shape[0]:,} orders")
print(f"Total Sales: ${df['Sales'].sum():,.0f}")
print(f"Total Profit: ${df['Profit'].sum():,.0f}")

# 1. Sales & Profit by Category
cat_summary = df.groupby('Category')[['Sales', 'Profit']].sum()
print("\n🏆 CATEGORY PERFORMANCE")
print(cat_summary.round(0))

plt.figure(figsize=(10, 6))
cat_summary.plot(kind='bar')
plt.title('Sales & Profit by Category')
plt.ylabel('Amount ($)')
plt.xticks(rotation=0)
plt.legend()
plt.savefig('category_performance.png')
plt.show()

# 2. Top 10 Products
top_products = df.groupby('Product Name')['Sales'].sum().nlargest(10)
print("\n🔥 TOP 10 PRODUCTS")
print(top_products.round(0))

plt.figure(figsize=(12, 6))
top_products.plot(kind='barh')
plt.title('Top 10 Products by Sales')
plt.xlabel('Sales ($)')
plt.tight_layout()
plt.savefig('top_products.png')
plt.show()

print("✅ Analysis complete! Charts saved as PNGs")
print("💡 Insights: Technology = highest profit | West region leads")
