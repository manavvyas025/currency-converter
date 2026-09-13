from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert_currency():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Please provide currency and amount"
        }), 400

    currency = data.get("currency")
    amount = data.get("amount")

    if not currency or amount is None:
        return jsonify({
            "error": "Please enter currency and amount"
        }), 400

    try:
        currency = currency.upper()
        amount = float(amount)

    except ValueError:
        return jsonify({
            "error": "amount must be valid"
        }), 400

    url = f"https://api.frankfurter.dev/v2/rate/{currency}/INR"

    try:
        response = requests.get(url)

    except requests.exceptions.RequestException:
        return jsonify({
            "error": "Unable to connect to the currency API."
        }), 500

    if response.status_code == 200:

        exchange_rate = response.json()
        rate = exchange_rate["rate"]
        converted_amount = rate * amount

        return jsonify({
            "currency": currency,
            "amount": amount,
            "rate": rate,
            "converted_amount": round(converted_amount, 2)
        })

    else:
        return jsonify({
            "error": "Invalid currency or unable to get exchange rate."
        }), 400

if __name__ == "__main__":
    app.run(debug=True)