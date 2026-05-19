import pandas as pd
import numpy as np


def segment_customers(customer_metrics):

    conditions = [

        (customer_metrics["total_orders"] >= 10)
        &
        (customer_metrics["avg_order_value"] >= 500),

        (customer_metrics["total_orders"] >= 5),

        (customer_metrics["total_orders"] < 5)

    ]

    segments = [
        "Premium Loyalists",
        "Regular Users",
        "Low Engagement"
    ]

    customer_metrics["segment"] = np.select(
        conditions,
        segments,
        default="Others"
    )

    return customer_metrics