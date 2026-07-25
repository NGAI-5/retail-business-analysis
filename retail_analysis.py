# retail_analysis.py
# Complete Retail Business Analysis Pipeline
# No warnings, no ambiguous cleaning.

import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

print("=" * 60)
print("🏪 RETAIL BUSINESS ANALYSIS DASHBOARD")
print("=" * 60)

# ============================================================
# 1. LOAD DATA
# ============================================================
print("\n📂 Loading data...")
df = pd.read_csv('shopping_trends.csv')
print(f"   ✅ Loaded {len(df)} rows and {len(df.columns)} columns.")

print("\n📊 First 5 rows:")
print(df.head())

# ============================================================
# 2. CLEAN DATA (PROFESSIONAL - NO WARNINGS)
# ============================================================
print("\n🧹 Checking for missing values...")

# Count missing before cleaning
missing_before = df.isnull().sum().sum()
print(f"   Missing values before cleaning: {missing_before}")

# Check which columns have missing values
print("\n   Columns with missing values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# Since only 1 row is missing data across multiple columns,
# the safest and most honest approach is to drop that row.
initial_len = len(df)
df = df.dropna()
rows_dropped = initial_len - len(df)

if rows_dropped > 0:
    print(f"\n   ✅ Dropped {rows_dropped} row(s) with missing values.")
else:
    print("\n   ✅ No missing values found.")

# Verify after cleaning
missing_after = df.isnull().sum().sum()
print(f"\n   Missing values after cleaning: {missing_after}")

if missing_after == 0:
    print("   ✅ Data is fully clean.")
else:
    print("   ⚠️ Warning: Some missing values remain. Please investigate manually.")

# ============================================================
# 3. KEY METRICS
# ============================================================
print("\n📊 Calculating Key Metrics...")

total_revenue = (df['quantity'] * df['price']).sum()
avg_order_value = (df['quantity'] * df['price']).mean()
total_customers = df['customer_id'].nunique()
total_transactions = df['invoice_no'].nunique()
top_category = df.groupby('category')['quantity'].sum().idxmax()
top_mall = df.groupby('shopping_mall')['quantity'].sum().idxmax()

print(f"   ✅ Total Revenue: ${total_revenue:,.2f}")
print(f"   ✅ Average Order Value: ${avg_order_value:,.2f}")
print(f"   ✅ Total Customers: {total_customers}")
print(f"   ✅ Total Transactions: {total_transactions}")
print(f"   ✅ Top Product Category: {top_category}")
print(f"   ✅ Top Shopping Mall: {top_mall}")

# ============================================================
# 4. GROUPED DATA FOR VISUALIZATION
# ============================================================
# Revenue by category
revenue_by_category = df.groupby('category').apply(
    lambda x: (x['quantity'] * x['price']).sum()
).sort_values(ascending=False)

# Revenue by mall
revenue_by_mall = df.groupby('shopping_mall').apply(
    lambda x: (x['quantity'] * x['price']).sum()
).sort_values(ascending=False)

# Customer age distribution
age_dist = df['age'].value_counts().sort_index()

# ============================================================
# 5. VISUALIZATIONS
# ============================================================
print("\n📊 Generating Charts...")

if not os.path.exists('charts'):
    os.makedirs('charts')

# Chart 1: Revenue by Category
plt.figure(figsize=(10, 6))
revenue_by_category.plot(kind='bar', color='skyblue')
plt.title('Revenue by Product Category')
plt.ylabel('Total Revenue (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/revenue_by_category.png')
plt.close()

# Chart 2: Revenue by Mall
plt.figure(figsize=(10, 6))
revenue_by_mall.plot(kind='bar', color='lightgreen')
plt.title('Revenue by Shopping Mall')
plt.ylabel('Total Revenue (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/revenue_by_mall.png')
plt.close()

# Chart 3: Age Distribution
plt.figure(figsize=(10, 6))
age_dist.plot(kind='bar', color='coral')
plt.title('Customer Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.savefig('charts/age_distribution.png')
plt.close()

print("   ✅ Charts saved in 'charts/' folder.")

# ============================================================
# 6. EXPORT TO EXCEL
# ============================================================
print("\n📂 Exporting to Excel...")

with pd.ExcelWriter('retail_report.xlsx') as writer:
    # Raw data
    df.to_excel(writer, sheet_name='Raw_Data', index=False)

    # Revenue by category
    revenue_by_category.to_excel(writer, sheet_name='Revenue_by_Category')

    # Revenue by mall
    revenue_by_mall.to_excel(writer, sheet_name='Revenue_by_Mall')

    # Summary metrics
    summary = pd.DataFrame({
        'Metric': [
            'Total Revenue', 'Average Order Value', 'Total Customers',
            'Total Transactions', 'Top Category', 'Top Mall'
        ],
        'Value': [
            f"${total_revenue:,.2f}",
            f"${avg_order_value:,.2f}",
            total_customers,
            total_transactions,
            top_category,
            top_mall
        ]
    })
    summary.to_excel(writer, sheet_name='Summary', index=False)

print("   ✅ Excel report saved: retail_report.xlsx")

# ============================================================
# 7. EXPORT TO PDF
# ============================================================
print("\n📂 Generating PDF Report...")

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Retail Business Summary Report', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.add_page()

# Section 1: Summary
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, '1. Key Metrics', 0, 1)
pdf.set_font('Arial', '', 12)
pdf.cell(0, 8, f'Total Revenue: ${total_revenue:,.2f}', 0, 1)
pdf.cell(0, 8, f'Average Order Value: ${avg_order_value:,.2f}', 0, 1)
pdf.cell(0, 8, f'Total Customers: {total_customers}', 0, 1)
pdf.cell(0, 8, f'Total Transactions: {total_transactions}', 0, 1)
pdf.cell(0, 8, f'Top Product Category: {top_category}', 0, 1)
pdf.cell(0, 8, f'Top Shopping Mall: {top_mall}', 0, 1)
pdf.ln(5)

# Section 2: Charts
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, '2. Visual Insights', 0, 1)

pdf.image('charts/revenue_by_category.png', x=10, y=30, w=190)
pdf.image('charts/revenue_by_mall.png', x=10, y=100, w=190)

pdf.add_page()
pdf.image('charts/age_distribution.png', x=10, y=30, w=190)

pdf.output('retail_summary.pdf')
print("   ✅ PDF report saved: retail_summary.pdf")

print("\n" + "=" * 60)
print("🎯 Project Complete!")
print("📂 Files generated:")
print("   - retail_report.xlsx")
print("   - retail_summary.pdf")
print("   - charts/ (folder with PNG images)")
print("=" * 60)
