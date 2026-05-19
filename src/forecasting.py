from prophet import Prophet


def build_forecast_model(dataframe):

    model = Prophet()

    model.fit(dataframe)

    return model


def generate_forecast(model, periods=30):

    future = model.make_future_dataframe(
        periods=periods
    )

    forecast = model.predict(future)

    return forecast