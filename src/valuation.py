def calculate_gmv_valuation(
    gmv,
    multiple
):

    return round(gmv * multiple, 2)


def calculate_ipo_readiness(
    margin_stability,
    avg_aov,
    avg_margin,
    avg_delivery_time
):

    score = 0

    if margin_stability > 70:
        score += 30
    elif margin_stability > 50:
        score += 20
    else:
        score += 10

    if avg_aov > 500:
        score += 25
    elif avg_aov > 400:
        score += 15
    else:
        score += 10

    if avg_margin > 20:
        score += 25
    elif avg_margin > 10:
        score += 15
    else:
        score += 10

    if avg_delivery_time < 20:
        score += 20
    else:
        score += 10

    return score