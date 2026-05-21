def validate_side(side):

    if side not in ["BUY", "SELL"]:
        return False

    return True


def validate_order_type(order_type):

    if order_type not in ["MARKET", "LIMIT"]:
        return False

    return True


def validate_quantity(quantity):

    if quantity <= 0:
        return False

    return True


def validate_price(price):

    if price is None or price <= 0:
        return False

    return True