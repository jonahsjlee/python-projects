'''
Name: Jonah Lee
Computing ID: wkx9ff
'''

def get_name(movie):
    return movie[0]

def get_gross(movie):
    return movie[1]

def get_rating(movie):
    return movie[3]

def get_num_ratings(movie):
    return movie[4]

def better_movies(movie_name, movies_list):
    better_movies_lst = []
    movie_rating = 0
    for movie in movies_list:
        if movie_name in movie:
            movie_rating = get_rating(movie)
    for movie in movies_list:
        if movie_rating < get_rating(movie):
            better_movies_lst.append(movie)
    return better_movies_lst

def average(category, movies_list):
    if category == "rating":
        total_ratings = 0
        for movie in movies_list:
            total_ratings += get_rating(movie)
        return total_ratings / len(movies_list)
    if category == "gross":
        total_gross = 0
        for movie in movies_list:
            total_gross += get_gross(movie)
        return total_gross / len(movies_list)
    if category == "number of ratings":
        total_num_ratings = 0
        for movie in movies_list:
            total_num_ratings += get_num_ratings(movie)
        return total_num_ratings / len(movies_list)




