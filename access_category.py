def access_category(product_info):
    try:
        category = product_info['category']
    except KeyError:
        category = None
    print('Product category:', category)

product_info = {
    'product_name': 'Table Lamp',
    'price': 45.99
}

if __name__ == '__main__':
    access_category(product_info)
