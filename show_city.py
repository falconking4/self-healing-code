def show_city(info):
    try:
        city = info['city']
    except KeyError:
        print('City: Unknown')
        return
    print('City:', city)

info = {
    'name': 'Jessica Lee',
    'country': 'Canada'
}

if __name__ == '__main__':
    show_city(info)
