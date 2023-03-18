movie_list = {
    1: {"name": "The Princess", "rating": 26},
    2: {"name": "Spider-Man: No Way Home", "rating": 81},
    3: {"name": "Morbius", "rating": 64},
    4: {"name": "The Northman", "rating": 72},
    5: {"name": "Troll", "rating": 67},
    6: {"name": "Avatar", "rating": 76},
    7: {"name": "The Woman King", "rating": 79}
}

def get_rating(movie_id):
    return movie_list[movie_id]["rating"]

result_1 = sorted(movie_list, key=get_rating, reverse=True)
for id in result_1:
    print(movie_list[id])

print("-"*50)
result_2 = sorted(movie_list, key=lambda id: movie_list[id]["rating"], reverse=True)
for id in result_2:
    print(movie_list[id])