#perpose is to transport the info from the api file to frontend in a readable way and updating the frontend every minute
from google_maps_info import *
import schedule
import time
def main():
    restaurants = top_ten_restaurants_info()
    print(restaurants['rating'])



















if __name__ == "__main__":
    main()