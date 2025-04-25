def predict_action(data, pair, pct_threshold=0.001, sl_pct=0.005, tp_pct=0.01):
    open_price = data['open']
    close_price = data['close']
    pct_change = (close_price - open_price) / open_price

    if pct_change > pct_threshold:
        # BUY
        entry = close_price
        sl = entry * (1 - sl_pct)
        tp = entry * (1 + tp_pct)
        return {
            "action": f"BUY {pair}",
            "entry": round(entry, 5),
            "stop_loss": round(sl, 5),
            "take_profit": round(tp, 5)
        }
    elif pct_change < -pct_threshold:
        # SELL
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
        return {
            "action": f"HOLD {pair}",
            "entry": round(close_price, 5),
            "stop_loss": None,
            "take_profit": None
        }
