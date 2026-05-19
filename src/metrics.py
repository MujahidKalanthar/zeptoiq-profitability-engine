import pandas as pd

def calculate_kpis(df):

    kpis = {
        "Total Orders": len(df),

        "Average Order Value":
        round(df["order_value"].mean(), 2),

        "Average Contribution Margin":
        round(df["contribution_margin"].mean(), 2),

        "Average Rider Cost":
        round(df["rider_cost"].mean(), 2),

        "Total Contribution Profit":
        round(df["contribution_margin"].sum(), 2)
    }

    return kpis