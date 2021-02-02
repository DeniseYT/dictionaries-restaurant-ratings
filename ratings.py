def get_rating(file):
    """Restaurant rating lister."""

    ratings = open(file)
    restaurant_rating = {}

    for line in ratings:
        line = line.rstrip()
        items = line.split(" ")

        for item in items:
            restaurant_rating[item] += 1
    
    for key, value in restaurant_rating.items():
        print(f"{key} is rated at {value}")
        print(key, value)
    
    return restaurant_rating
    
print(get_rating("scores.txt"))


