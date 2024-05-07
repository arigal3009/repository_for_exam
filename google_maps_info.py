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
