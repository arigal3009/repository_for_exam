#perpose is to bring the info needed from the google maps servers with api to the_solution
import json
import os
import requests
location = '32.109333,34.855499'  # Latitude, Longitude for Tel Aviv
query = 'restaurants in Tel Aviv yafo' # parameter for spicific info
api_key = 'AIzaSyDOMTBBc_iW-Jbui8GJO9eUFA_PMqEG45Q' # the key to acsess info in the servers of google maps
url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&location={location}&key={api_key}'

#gets all the restaurants and returns the top 10 restaurants in a sorted list
def top_ten_restaurants(restaurants):
        NUM_OF_RESTERAUNTS = 10
        top_ten = []
        for restaurant in restaurants:
            if len(top_ten) < NUM_OF_RESTERAUNTS:
                top_ten.append(restaurant)
                top_ten.sort(key=lambda x: x['rating'], reverse=True)
            else:
                lowest_restaurant_rating = top_ten[-1]['rating']
                if restaurant['rating'] > lowest_restaurant_rating:
                    top_ten.pop()
                    top_ten.append(restaurant)
                    top_ten.sort(key=lambda restaurant: restaurant['rating'], reverse=True)
        return top_ten

# makes the request from google maps and returns a list of the 10 best restaurants with only the data of them that is needed
def top_ten_restaurants_info():
    response = requests.get(url)
    data = response.json()
    restaurants = data['results']
    top = top_ten_restaurants(restaurants)
    top_ten_table = []
    top_ten_list = []

    for restaurant in top:
          top_ten_list = [restaurant['name'], restaurant['rating'],restaurant['opening_hours']['open_now']]
          top_ten_table.append(top_ten_list)

    return top_ten_table

# this to check ci process
# also part of the test
# believe it or not this is also part of the test
"""
# Print the name and address of each restaurant
for result in data['results']:
    name = result['name']
    print(f'{name}')
results = top_ten_restaurants_info(data)

def top_ten_restaurants_info(data):
    top_ten = []
    for result in data:
        if len(top_ten) < 10:
            top_ten.append(result)
            top_ten.sort(key=lambda x: x["rating"], reverse=True)
        else:
            if result["rating"] > top_ten[-1]["rating"]:
                top_ten.pop()
                top_ten.append(result)
                top_ten.sort(key=lambda x: x["rating"], reverse=True)
    return top_ten
"""
"""api_key = 'AIzaSyBJuvh0nh_oMc--t6zBvAea5O4wn_TqxQQ'
restaurants = [
    "אפטר תשע",
    "benny's restaurant",
    "etzlenu",
    "la fruiteria",
    "flame tlv",
    "joker",
    "tandoori lands end tlv",
    "bakerem",
    "yala knafeh",
    "jasmino",
]
def info_on_restaurants():
    list_of_info_on_restaurants = []
    list_of_info_on_restaurant = []
    for restaurant in restaurants:
        name = f'{restaurant} Tel Aviv'
        url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={name}&key={api_key}'
        response = requests.get(url)
        data = response.json()


"""