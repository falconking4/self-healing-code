def fetch_date(event_details):
    date = event_details["date"]
    print("Event date:", date)

event_details = {
    "event_name": "Annual Conference",
    "location": "New York City"
}
if __name__ == "__main__":
    fetch_date(event_details)