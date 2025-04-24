def predict_action(data, pair, threshold=0.001, sl_pct=0.005, tp_pct=0.01):
    """
    Predicts the trading action (BUY, SELL, HOLD) based on price difference.

    Parameters:
        data (dict): A dictionary containing 'open' and 'close' prices.
        pair (str): The currency pair being traded.
        threshold (float): The minimum price difference to trigger a BUY or SELL.
        sl_pct (float): Stop-loss percentage.
        tp_pct (float): Take-profit percentage.

    Returns:
        dict: A dictionary containing the action, entry price, stop-loss, and take-profit.
    """
    open_price = data['open']
    close_price = data['close']
    diff = close_price - open_price

    if diff > threshold:
        # BUY action
        entry = close_price
        sl = entry * (1 - sl_pct)
        tp = entry * (1 + tp_pct)
        return {
            "action": f"BUY {pair}",
            "entry": round(entry, 5),
            "stop_loss": round(sl, 5),
            "take_profit": round(tp, 5)
        }
    elif diff < -threshold:
        # SELL action
        entry = close_price
        sl = entry * (1 + sl_pct)
        tp = entry * (1 - tp_pct)
        return {
            "action": f"SELL {pair}",
            "entry": round(entry, 5),
            "stop_loss": round(sl, 5),
            "take_profit": round(tp, 5)
        }
    else:
        # HOLD action
        return {
            "action": f"HOLD {pair}",
            "entry": round(close_price, 5),
            "stop_loss": None,
            "take_profit": None
        }

