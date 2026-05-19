def calculate_z_score(
    demand_intensity,
    delivery_distance,
    customer_priority,
    inventory_pressure,
    basket_value
):

    # Weight configuration
    demand_weight = 0.30
    distance_weight = 0.25
    customer_weight = 0.20
    inventory_weight = 0.15
    basket_weight = 0.10

    z_score = (
        (demand_intensity * demand_weight)
        +
        (delivery_distance * distance_weight)
        +
        (customer_priority * customer_weight)
        +
        (inventory_pressure * inventory_weight)
        +
        (basket_value * basket_weight)
    )

    return round(z_score, 2)


def recommend_delivery_fee(z_score):

    base_fee = 20

    dynamic_fee = base_fee + (z_score * 5)

    return round(dynamic_fee, 2)


def estimate_profitability(
    order_value,
    delivery_fee,
    rider_cost,
    dark_store_cost,
    discount
):

    gross_margin = order_value * 0.20

    contribution_margin = (
        gross_margin
        + delivery_fee
        - rider_cost
        - dark_store_cost
        - discount
    )

    return round(contribution_margin, 2)