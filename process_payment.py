def process_payment(info):
    payment_method = info["payment_method"]
    print("Processing payment using:", payment_method)

info = {
    "customer_name": "Alice Smith",
    "total_amount": 200
}

process_payment(info)