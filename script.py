def get_vehicle_detail(vehicle_data):
    model_year = vehicle_data["model_year"]
    print("Vehicle model year:", model_year)

vehicle_data = {
    "make": "Toyota",
    "model": "Camry"
}

if __name__ == "__main__":
    get_vehicle_detail(vehicle_data)