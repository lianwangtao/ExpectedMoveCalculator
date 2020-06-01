import os
import sys
import argparse
import math
import requests
import yfinance as yf
from datetime import datetime

def parse_args():
    help_message = """
    Arguments:
    -s, --stock: Stock Symbol
        (e.g. TSLA)
    -d, --days: How many days are the option expiration date from today
        (e.g. 7 (days))

    Usage:

    To get an expected price for a stock for a certain period, e.g. TSLA in 7 days:
        python expected_price.py -s TSLA -d 7
            Last close price: 835.0
            TSLA IV: 55.6
            TSLA expected move is +/- 64.2930242535785
            High: 899.2930242535786, Low: 770.7069757464214

    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s',
        '--stock',
        help="Stock Symbol")
    parser.add_argument(
        '-d',
        '--days',
        help="How many days are the option expiration date from today")

    args = parser.parse_args()

    if not args.stock and not args.days:
        print(help_message)
        sys.exit(1)

    return args.stock, args.days

def get_expected_move(stock_name, days):
    stock = yf.Ticker(stock_name)

    hist = stock.history(period="1d")
    pre_close = float(hist.Close[0])
    print(f"Last close price: {pre_close}")

    response_content = str(requests.get(f'https://marketchameleon.com/Overview/{stock_name}/IV/').content)
    iv_str = response_content.split(f"{stock_name} IV Percentile Rank</h3>\\r\\n        <p>\\r\\n            ")[1].split("which is in the <strong>")[0]

    iv = float(iv_str.split("is ")[1].split(",")[0])
    print(f"{stock_name} IV: {iv}")

    expected_move = pre_close * (iv / 100) * math.sqrt(days / 365)
    print(f"{stock_name} expected move is +/- {expected_move}")
    print(f"High: {pre_close + expected_move}, Low: {pre_close - expected_move}")

def main():
    stock_name, days = parse_args()
    get_expected_move(stock_name, int(days))

if __name__ == '__main__':
    main()