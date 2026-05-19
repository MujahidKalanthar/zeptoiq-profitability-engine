import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# -----------------------------
# CONFIG
# -----------------------------

NUM_ORDERS = 20000

cities = [
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Chennai",
    "Pune"
]

categories = [
    "Groceries",
    "Cafe",
    "Beauty",
    "Electronics"
]

customer_types = [
    "Premium",
    "Regular",
    "Discount-Seeker"
]

# -----------------------------
# GENERATE DATA
# -----------------------------

data = []

start_date = datetime(2025, 1, 1)

for order_id in range(1, NUM_ORDERS + 1):

    city = random.choice(cities)

    category = random.choices(
        categories,
        weights=[60, 20, 15, 5]
    )[0]

    customer_type = random.choices(
        customer_types,
        weights=[25, 50, 25]
    )[0]

    order_time = start_date + timedelta(
        minutes=random.randint(0, 180*24*60)
    )

    distance_km = round(np.random.uniform(0.5, 6.0), 2)

    order_value = round(np.random.normal(450, 120), 2)
    order_value = max(order_value, 100)

    delivery_fee = round(np.random.uniform(15, 45), 2)

    rider_cost = round(
        25 + (distance_km * 6) + np.random.uniform(5, 20),
        2
    )

    dark_store_cost = round(np.random.uniform(20, 50), 2)

    discount = round(np.random.uniform(0, 80), 2)

    delivery_time = round(
        8 + (distance_km * 2) + np.random.uniform(0, 10),
        2
    )

    gross_margin = order_value * np.random.uniform(0.15, 0.25)

    contribution_margin = round(
        gross_margin
        + delivery_fee
        - rider_cost
        - dark_store_cost
        - discount,
        2
    )

    peak_hour = 1 if order_time.hour in [12,13,14,19,20,21] else 0

    data.append([
        order_id,
        city,
        category,
        customer_type,
        order_time,
        distance_km,
        order_value,
        delivery_fee,
        rider_cost,
        dark_store_cost,
        discount,
        delivery_time,
        gross_margin,
        contribution_margin,
        peak_hour
    ])

# -----------------------------
# CREATE DATAFRAME
# -----------------------------

columns = [
    "order_id",
    "city",
    "category",
    "customer_type",
    "order_time",
    "distance_km",
    "order_value",
    "delivery_fee",
    "rider_cost",
    "dark_store_cost",
    "discount",
    "delivery_time",
    "gross_margin",
    "contribution_margin",
    "peak_hour"
]

df = pd.DataFrame(data, columns=columns)

# -----------------------------
# SAVE DATA
# -----------------------------

output_path = "data/synthetic/orders_data.csv"

df.to_csv(output_path, index=False)

print(f"Dataset generated successfully!")
print(f"Saved to: {output_path}")
print(df.head())