# Q2 - Flight Itinerary Printer

flight_route = [
    ("New Orleans", "Atlanta"),
    ("Atlanta", "Chicago"),
    ("Chicago", "New York"),
    ("New York", "Boston")
]


def print_itinerary(route_list):
    """Print a structured flight schedule from a list of tuples."""
    print("Flight Itinerary")
    print("----------------")

    for departure_city, arrival_city in route_list:
        print(f"{departure_city} -> {arrival_city}")


if __name__ == "__main__":
    print_itinerary(flight_route)
