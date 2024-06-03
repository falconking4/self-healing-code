def process_payment(info):
    try:
        payment_method = info['payment_method']
    except KeyError:
        print('Payment method not provided')
        return
    
    print('Processing payment using:', payment_method)

info = {
    'customer_name': 'Alice Smith',
    'total_amount': 200
}

process_payment(info)
