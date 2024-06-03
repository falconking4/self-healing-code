def check_availability(data):
    stock_quantity = data["stock_quantity"]
    print("Available stock:", stock_quantity)

data = {
    "product_name": "Laptop",
    "price": 999
}

if __name__ == "__main__":
    check_availability(data)
