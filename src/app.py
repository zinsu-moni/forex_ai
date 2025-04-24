from flask import Flask, render_template, request
from utils.telegram_bot import send_telegram_message
from model.predictor import predict_action
from data.fetcher import get_latest_data

app = Flask(__name__)

currency_pairs = ["USD/EUR", "GBP/USD", "USD/JPY", "EUR/JPY", "AUD/USD", "XAU/USD", "USD/CAD", "NZD/USD", "USD/CHF", "GBP/JPY", "EUR/GBP", "ETH/USD", "BTC/USD", "XRP/USD", "LTC/USD"]

@app.route("/", methods=["GET", "POST"])
def home():
    signal = None
    selected_pair = None
    if request.method == "POST":
        selected_pair = request.form.get("currency_pair")
        if selected_pair:
            base, target = selected_pair.split("/")
            latest_data = get_latest_data(base, target)
            signal = predict_action(latest_data, selected_pair)
            send_telegram_message(f"Forex Signal: {signal}")
    return render_template("index.html", pairs=currency_pairs, signal=signal, selected_pair=selected_pair)

if __name__ == "__main__":
    app.run(debug=True)
