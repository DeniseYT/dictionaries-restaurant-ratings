def get_rating(file):
    """Restaurant rating lister."""

    ratings = open(file)
    restaurant_rating = {}

    for line in ratings:
        line = line.rstrip()
        restaurant, score = line.split(":")
        restaurant_rating[restaurant] = int(score)
    print(restaurant_rating)
    
    for key, value in restaurant_rating.items():
        print(f"{key} is rated at {value}")
        
    return restaurant_rating
    
get_rating("scores.txt")


