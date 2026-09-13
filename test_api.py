import requests

try:
    currency = input("Enter the base currency: ").upper()
    amount = float(input("Enter the amount: "))

    url = f"https://api.frankfurter.dev/v2/rate/{currency}/INR"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rate"]
        converted_amount = amount * rate
        print(f"{amount} {currency} = ₹{converted_amount:.2f} INR")

    else:
        print("Invalid currency or unable to get exchange rate.")

except ValueError:
    print("Please enter a valid number for the amount")

except requests.exceptions.RequestException:
    print("Unable to connect to the currency API")