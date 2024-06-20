def print_color(item_details):
    color = item_details["color"]
    print("Color of the item:", color)

item_details = {
    "item_name": "Notebook",
    "item_id": 3245
}

if __name__ == "__main__":
    print_color(item_details)