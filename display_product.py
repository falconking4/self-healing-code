def display_product_price(product_details):
    if 'price' in product_details:
        price = product_details['price']
        print('Product price:', price)
    else:
        print('Price not found')

product_details = {
    'product_name': 'Wireless Mouse',
    'product_id': 4567
}

if __name__ == '__main__':
    display_product_price(product_details)
