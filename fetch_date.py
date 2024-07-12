def fetch_date(event_details):
    try:
        date = event_details['date']
    except KeyError:
        date = None
    print('Event date:', date)

if __name__ == '__main__':
    event_details = {
        'event_name': 'Annual Conference',
        'location': 'New York City'
    }
    fetch_date(event_details)
