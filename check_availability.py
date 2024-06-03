def check_availability(data):
    try:
        stock_quantity = data['stock_quantity']
    except KeyError:
        stock_quantity = 0

    # Rest of function
