def print_customer_address(order_record):
    if 'address' in order_record:
        address = order_record['address']
        print('Customer address:', address)
    else:
        print('Address not provided')

order_record = {
    'customer_name': 'Samantha Green',
    'order_id': 7890
}

if __name__ == '__main__':
    print_customer_address(order_record)
