import argparse
from orders import place_market_order, place_limit_order
from validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

parser = argparse.ArgumentParser()

parser.add_argument("--symbol")
parser.add_argument("--side")
parser.add_argument("--type")
parser.add_argument("--quantity", type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

if not validate_side(args.side):
    print("Invalid side")
    exit()

if not validate_order_type(args.type):
    print("Invalid order type")
    exit()

if not validate_quantity(args.quantity):
    print("Invalid quantity")
    exit()

if args.type == "LIMIT":

    if not validate_price(args.price):
        print("Invalid price")
        exit()

if args.type == "MARKET":

    place_market_order(
        args.symbol,
        args.side,
        args.quantity
    )

elif args.type == "LIMIT":

    place_limit_order(
        args.symbol,
        args.side,
        args.quantity,
        args.price
    )

else:
    print("Invalid order type")