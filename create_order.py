def handler(body):
    # Check if 'order_items' key exists before accessing
    if 'order_items' in body:
        order_items = body['order_items']
        print(order_items)
    else:
        print('No order items found')

# Sample body dictionary without 'order_items' key
body = {
    'customer_name': 'John Doe',
    'order_id': 123456
}

# Call the function, which will no longer raise KeyError
handler(body)
