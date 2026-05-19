def simulate_demand_spike(
    base_profit,
    multiplier=1.15
):

    return round(
        base_profit * multiplier,
        2
    )


def simulate_discount_war(
    base_profit,
    impact=0.80
):

    return round(
        base_profit * impact,
        2
    )


def simulate_labor_regulation(
    base_profit,
    impact=0.85
):

    return round(
        base_profit * impact,
        2
    )