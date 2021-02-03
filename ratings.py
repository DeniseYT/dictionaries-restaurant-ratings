
def get_rating(file):
    """Restaurant rating lister."""

    ratings = open(file)
    restaurant_rating = {}

    for line in ratings:
        line = line.rstrip()
        restaurant, score = line.split(":")
        restaurant_rating[restaurant] = int(score)
    
    for key, value in sorted(restaurant_rating.items()):
        print(f"{key} is rated at {value}")
        
    return restaurant_rating
  
get_rating("scores.txt")


def add_rating(restaurant_rating):

    new_restaurant = input("Which restaurant you'd like to rate? > ")
    new_restaurant = new_restaurant.title()
    new_score = input("What's the rating? > ")

    restaurant_rating[new_restaurant] = int(new_score)

    for key, value in sorted(restaurant_rating.items()):
        print(f"{key} is rated at {value}")

    return restaurant_rating

add_rating(get_rating("scores.txt"))




