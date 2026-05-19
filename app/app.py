import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import sys

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="ZeptoIQ",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv(
    "data/synthetic/orders_data.csv"
)

# -----------------------------
# TITLE
# -----------------------------

st.title("ZeptoIQ")
st.subheader(
    "Profitability & IPO Readiness Intelligence Platform"
)

# -----------------------------
# KPI SECTION
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Orders",
        len(df)
    )

with col2:
    st.metric(
        "Average Order Value",
        f"₹{round(df['order_value'].mean(),2)}"
    )

with col3:
    st.metric(
        "Avg Contribution Margin",
        f"₹{round(df['contribution_margin'].mean(),2)}"
    )

with col4:
    st.metric(
        "Avg Delivery Time",
        f"{round(df['delivery_time'].mean(),2)} mins"
    )

# -----------------------------
# CITY PROFITABILITY
# -----------------------------

st.header("City Profitability Analysis")

city_profit = (

    df.groupby("city")
    ["contribution_margin"]
    .mean()
    .reset_index()

)

fig_city = px.bar(

    city_profit,

    x="city",

    y="contribution_margin",

    color="contribution_margin",

    title="Average Contribution Margin by City"

)

st.plotly_chart(fig_city, use_container_width=True)

# -----------------------------
# AOV VS PROFITABILITY
# -----------------------------

st.header("Order Value vs Profitability")

fig_scatter = px.scatter(

    df,

    x="order_value",

    y="contribution_margin",

    color="customer_type",

    opacity=0.6,

    title="Order Value vs Contribution Margin"

)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)

# -----------------------------
# PROFITABILITY SIMULATOR
# -----------------------------

st.header("Profitability Simulator")

aov = st.slider(
    "Average Order Value",
    100,
    1000,
    500
)

delivery_fee = st.slider(
    "Delivery Fee",
    10,
    100,
    30
)

rider_cost = st.slider(
    "Rider Cost",
    10,
    100,
    40
)

discount = st.slider(
    "Discount",
    0,
    100,
    20
)

gross_margin = aov * 0.20

estimated_profit = (

    gross_margin
    + delivery_fee
    - rider_cost
    - 30
    - discount

)

st.metric(
    "Estimated Contribution Margin",
    f"₹{round(estimated_profit,2)}"
)

# -----------------------------
# IPO READINESS SCORE
# -----------------------------

st.header("IPO Readiness Score")

margin_stability = (

    len(df[df["contribution_margin"] > 0])
    / len(df)

) * 100

score = 0

if margin_stability > 70:
    score += 30
elif margin_stability > 50:
    score += 20
else:
    score += 10

if df["order_value"].mean() > 500:
    score += 25
else:
    score += 15

if df["contribution_margin"].mean() > 20:
    score += 25
else:
    score += 15

if df["delivery_time"].mean() < 20:
    score += 20
else:
    score += 10

st.metric(
    "IPO Readiness Score",
    f"{score}/100"
)

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("---")

st.caption(
    "ZeptoIQ • Quick-Commerce Profitability Intelligence Platform"
)