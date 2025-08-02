# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Part 1: Setup & Load Data
st.title("🏡 Housing Data Analysis")

df = pd.read_csv("Housing.csv")

# Part 2: Explore & Clean Data
st.subheader("🔍 Data Preview")
st.dataframe(df.head(20))

st.subheader("📊 Summary Statistics")
st.dataframe(df.describe())

# Missing values
st.subheader("🚨 Missing Values")
null_sum = df.isnull().sum()
st.dataframe(null_sum.rename("Value").to_frame())

# Part 3: Compute Statistics
st.subheader("📈 Descriptive Statistics")

numerical_cols = ['price', 'area', 'bedrooms']
mean_values = df[numerical_cols].mean()
median_values = df[numerical_cols].median()
mode_values = df[numerical_cols].mode().iloc[0]
vars_values = df[numerical_cols].var()
std_values = df[numerical_cols].std()
skew_values = df[numerical_cols].skew()
kurtosis_values = df[numerical_cols].kurt()
min_values = df[numerical_cols].min()
max_values = df[numerical_cols].max()

st.write("**Mean:**")
st.dataframe(mean_values.rename("Value").to_frame())
st.write("**Median:**")
st.dataframe(median_values.rename("Value").to_frame())
st.write("**Mode:**")
st.dataframe(mode_values.rename("Value").to_frame())
st.write("**Variance:**")
st.dataframe(vars_values.rename("Value").to_frame())
st.write("**Standard Deviation:**")
st.dataframe(std_values.rename("Value").to_frame())
st.write("**Skewness:**")
st.dataframe(skew_values.rename("Value").to_frame())
st.write("**Kurtosis:**")
st.dataframe(kurtosis_values.rename("Value").to_frame())
st.write("**Min Values:**",)
st.dataframe(min_values.rename("Value").to_frame())
st.write("**Max Values:**",)
st.dataframe(max_values.rename("Value").to_frame())

# Part 4: Visualizations
st.subheader("📉 Visualizations")

# Histogram: Price
st.markdown("**Histogram of Price**")
fig1, ax1 = plt.subplots()
ax1.hist(df['price'], bins=30, color='skyblue', edgecolor='black')
ax1.set_xlabel("Price")
ax1.set_ylabel("Frequency")
ax1.set_title("Histogram of Price")
st.pyplot(fig1)

# Histogram: Area
st.markdown("**Histogram of Area**")
fig2, ax2 = plt.subplots()
ax2.hist(df['area'], bins=30, color='salmon', edgecolor='black')
ax2.set_xlabel("Area")
ax2.set_ylabel("Frequency")
ax2.set_title("Histogram of Area")
st.pyplot(fig2)

# Box plot: Price
st.markdown("**Box Plot of Price**")
fig3, ax3 = plt.subplots()
ax3.boxplot(df['price'], vert=False)
ax3.set_xlabel("Price")
ax3.set_title("Box Plot of Price")
st.pyplot(fig3)

# Box plot: Area
st.markdown("**Box Plot of Area**")
fig4, ax4 = plt.subplots()
ax4.boxplot(df['area'], vert=False)
ax4.set_xlabel("Area")
ax4.set_title("Box Plot of Area")
st.pyplot(fig4)

# Scatter plot: Price vs Area
st.markdown("**Scatter Plot: Price vs Area**")
fig5, ax5 = plt.subplots()
ax5.scatter(df['area'], df['price'], alpha=0.6, color='green')
ax5.set_xlabel("Area")
ax5.set_ylabel("Price")
ax5.set_title("Price vs Area")
ax5.ticklabel_format(style='plain', axis='y')  # Disable scientific notation
ax5.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
st.pyplot(fig5)

# Part 5: Storytelling
st.subheader("📚 Data Storytelling")

if st.toggle("Show/Hide Housing Market Insights"):
    st.markdown("""
- The housing data shows high average prices with a wide range, indicating significant variation in housing costs.
- Outliers exist, with some properties priced well above the typical range.
- Prices tend to rise with area, but the relationship is not strictly linear.
- Other factors—such as location, amenities, and furnishing—also influence price.
- Skewness and kurtosis suggest the market leans toward higher-end or premium properties.
- Buyers should carefully compare similar homes due to wide price variation.
- Sellers of larger homes may benefit if they price competitively.
    """)

