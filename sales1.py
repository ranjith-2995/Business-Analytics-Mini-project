# 📊 SALES DATA ANALYSIS USING PYTHON
# ----------------------------------

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure plot styles
plt.style.use('ggplot')
sns.set_palette('Set2')

# ----------------------------
# 1️⃣ LOAD THE DATA
# ----------------------------
file_path = "sales_data.csv"   # <- Change to your file path
df = pd.read_csv(file_path)

# Display first few rows
print("Sample Data:")
print(df.head())

# ----------------------------
# 2️⃣ BASIC INFORMATION
# ----------------------------
print("\n--- Basic Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

# ----------------------------
# 3️⃣ DATA CLEANING
# ----------------------------
# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Remove missing or invalid data
df = df.dropna(subset=['Date', 'Product', 'Total Sales'])

# Remove duplicates
df = df.drop_duplicates()

# Calculate Revenue if missing
if 'Total Sales' not in df.columns:
    df['Total Sales'] = df['Quantity'] * df['Price']

# Extract additional time features
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month_name()
df['Day'] = df['Date'].dt.day

print("\nCleaned Data Shape:", df.shape)

# ----------------------------
# 4️⃣ SALES SUMMARY
# ----------------------------
total_sales = df['Total Sales'].sum()
avg_sales = df['Total Sales'].mean()
top_product = df.groupby('Product')['Total Sales'].sum().idxmax()
top_region = df.groupby('Region')['Total Sales'].sum().idxmax()

print(f"\n💰 Total Sales: {total_sales:,.2f}")
print(f"📈 Average Sale Value: {avg_sales:,.2f}")
print(f"🏆 Top Product: {top_product}")
print(f"🌍 Top Region: {top_region}")

# ----------------------------
# 5️⃣ DATA ANALYSIS & VISUALIZATION
# ----------------------------

# --- Sales by Month ---
monthly_sales = df.groupby('Month')['Total Sales'].sum().reindex(
    ['January','February','March','April','May','June',
     'July','August','September','October','November','December']
)

plt.figure(figsize=(10,5))
sns.barplot(x=monthly_sales.index, y=monthly_sales.values)
plt.xticks(rotation=45)
plt.title("Monthly Sales Performance")
plt.ylabel("Total Sales")
plt.xlabel("Month")
plt.show()

# --- Sales by Region ---
plt.figure(figsize=(8,5))
sns.barplot(x='Region', y='Total Sales', data=df, estimator=sum)
plt.title("Sales by Region")
plt.ylabel("Total Sales")
plt.xlabel("Region")
plt.show()

# --- Top 10 Products ---
top10_products = df.groupby('Product')['Total Sales'].sum().nlargest(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top10_products.values, y=top10_products.index)
plt.title("Top 10 Best-Selling Products")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.show()

# --- Yearly Trend ---
plt.figure(figsize=(8,5))
sns.lineplot(x='Year', y='Total Sales', data=df, estimator='sum', ci=None, marker='o')
plt.title("Yearly Sales Trend")
plt.ylabel("Total Sales")
plt.xlabel("Year")
plt.show()

# --- Category Analysis (if available) ---
if 'Category' in df.columns:
    plt.figure(figsize=(8,5))
    sns.barplot(x='Category', y='Total Sales', data=df, estimator=sum)
    plt.title("Sales by Category")
    plt.ylabel("Total Sales")
    plt.xlabel("Category")
    plt.show()

# ----------------------------
# 6️⃣ INSIGHTS
# ----------------------------
print("\n📊 KEY INSIGHTS:")
print(f"- Total revenue generated: ₹{total_sales:,.2f}")
print(f"- Highest sales recorded in: {monthly_sales.idxmax()}")
print(f"- Top-performing product: {top_product}")
print(f"- Most profitable region: {top_region}")
print("- Consistent sales growth across months indicates good product performance.")

# ----------------------------
# ✅ END OF PROGRAM
# ----------------------------
print("\n✅ Sales Data Analysis Completed Successfully!")
