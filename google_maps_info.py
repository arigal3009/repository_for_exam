#perpose is to bring the info needed from the google maps servers with api to transporter.py
import requests
import json
import os
def top_ten_restaurants(restaurants):
        top_ten = []
        for restaurant in restaurants:
            if len(top_ten) < 10:
                top_ten.append(restaurant)
                top_ten.sort(key=lambda x: x['rating'], reverse=True)
            else:
                if restaurant['rating'] > top_ten[-1]['rating']:
                    top_ten.pop()
                    top_ten.append(restaurant)
                    top_ten.sort(key=lambda x: x['rating'], reverse=True)
        return top_ten

def main():
    location = '32.109333,34.855499'  # Latitude, Longitude for Tel Aviv
    query = 'restaurants in Tel Aviv yafo'
    api_key = 'AIzaSyBJuvh0nh_oMc--t6zBvAea5O4wn_TqxQQ'
    url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&location={location}&key={api_key}'
    response = requests.get(url)
    data = response.json()
    restaurants = data['results']
    top = top_ten_restaurants(restaurants)
    for x in top:
        print(x['rating'])
    
    
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

if __name__ == "__main__":
    main()