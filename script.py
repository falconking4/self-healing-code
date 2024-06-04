def get_vehicle_detail(vehicle_data):
    try:
        model_year = vehicle_data['model_year']
    except KeyError:
        model_year = None
    print('Vehicle model year:', model_year)

vehicle_data = {
    'make': 'Toyota',
    'model': 'Camry'
}

if __name__ == '__main__':
    get_vehicle_detail(vehicle_data)
