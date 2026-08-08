import sys

import requests

API_KEY = "YourApiKey"  # Replace with your own CoinCap API key


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    price = get_price()
    total = n * price
    print(f"${total:,.4f}")


def get_price():
    try:
        response = requests.get(
            f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"
        )
        response.raise_for_status()
        data = response.json()
        return float(data["data"]["priceUsd"])
    except (requests.RequestException, KeyError, TypeError, ValueError):
        sys.exit("Error fetching price data")


if __name__ == "__main__":
    main()
