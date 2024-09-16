#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd

# Tax brackets 
tax_brackets = pd.DataFrame({
    'Lower_Limit': [0, 100001, 150001, 350001, 550001, 850001, 1550001],
    'Fixed_Tax': [0, 0, 9000, 59000, 115000, 205000, 429000],
    'Percentage': [0, 0.18, 0.25, 0.28, 0.30, 0.32, 0.37]
})

# Streamlit app interface
st.title("Monthly Tax Calculator")

# Input for monthly taxable income
monthly_income = st.number_input("Enter your monthly taxable income (N$)", min_value=0.0, step=100.0)

# Calculate annual taxable income
annual_income = monthly_income * 12

# Function to calculate the tax based on the Excel formula logic
def calculate_tax(annual_income, tax_brackets):
    # If annual income is less than 1, tax is 0
    if annual_income < 1:
        return 0

    # Find the relevant tax bracket
    for i in range(len(tax_brackets)-1, -1, -1):
        if annual_income > tax_brackets['Lower_Limit'][i]:
            fixed_tax = tax_brackets['Fixed_Tax'][i]
            percentage = tax_brackets['Percentage'][i]
            taxable_amount = annual_income - tax_brackets['Lower_Limit'][i]
            tax = (fixed_tax + (taxable_amount * percentage)) / 12  # Monthly tax
            return round(tax, 2)

# Calculate tax based on input
monthly_tax = calculate_tax(annual_income, tax_brackets)

# Display the calculated tax
st.write(f"Your monthly tax is: N${monthly_tax:.2f}")


# In[ ]:




