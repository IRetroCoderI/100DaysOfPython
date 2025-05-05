capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },

    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

print(travel_log["France"]["total_visits"]) 
print(travel_log["Germany"]["cities_visited"][2])


my_dict = {"a": 1, "b": 2}
my_dict["c"] = 3
print(my_dict)
# Expected output: {'a': 1, 'b': 2, 'c': 3}