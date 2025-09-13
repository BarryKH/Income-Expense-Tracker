import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Income & Expense")
st.subheader("Data")
#data
totalMonths = st.number_input("Total Months", min_value=1, max_value=12, value=3)
data = []
currentMonth = 0
for eachMonth in range(totalMonths):
    st.write(f"### Month {currentMonth+1}")
    month = st.text_input(f"Month {currentMonth+1} (e.g., Jan)", key=f"m{currentMonth}")
    income = st.number_input(f"Income for {month}", key = f"inc{currentMonth}", step = 100.0)
    expense = st.number_input(f"Expense for {month}", key = f"exp{currentMonth}", step = 100.0)
    if month:
        data.append({"Month":month, "Income":income, "Expense":expense, "Savings":income - expense})
    currentMonth += 1
if data:
    df = pd.DataFrame(data)
    st.write("### Data")
    st.dataframe(df)

    df["Total Savings"] = df["Savings"].cumsum()
#income&expend
    fig = px.line(df, x="Month", y=["Income","Expense"], markers=True,
                  title="Income vs. Expense")
    st.plotly_chart(fig)
#total savings
    fig2 = px.line(df, x="Month", y=["Total Savings"], markers=True,
                  title="Savings")
    st.plotly_chart(fig2)
