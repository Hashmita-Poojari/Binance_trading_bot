from client import client
from logging_config import logger


def place_market_order(symbol, side, quantity):

    try:

        logger.info(
            f"Placing MARKET order: {side} {quantity} {symbol}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logger.info(f"Order Success: {order}")

        print("\nMarket order placed successfully")
        print(f"Symbol: {order['symbol']}")
        print(f"Side: {order['side']}")
        print(f"Quantity: {order['origQty']}")
        print(f"Order ID: {order['orderId']}")
        print(f"Status: {order['status']}")

    except Exception as error:

        logger.error(f"Market Order Failed: {error}")

        print("\nOrder failed")
        print(f"Reason: {error}")


def place_limit_order(symbol, side, quantity, price):

    try:

        logger.info(
            f"Placing LIMIT order: {side} {quantity} {symbol} at {price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(f"Order Success: {order}")

        print("\nLimit order placed successfully")
        print(f"Symbol: {order['symbol']}")
        print(f"Side: {order['side']}")
        print(f"Quantity: {order['origQty']}")
        print(f"Price: {order['price']}")
        print(f"Order ID: {order['orderId']}")
        print(f"Status: {order['status']}")

    except Exception as error:

        logger.error(f"Limit Order Failed: {error}")

        print("\nOrder failed")
        print(f"Reason: {error}")