#perpose is to transport the info from the api file to frontend in a readable way and updating the frontend every minute
from google_maps_info import *
import schedule
import time
import argparse
def main():
    top_ten = top_ten_restaurants_info()
    top_ten_table = []
    top_ten_list = []
    for restaurant in top_ten:
          top_ten_list = [restaurant['name'], restaurant['rating'],restaurant['open now']]
          top_ten_table += top_ten_list
    print(top_ten_table)  #need to export to presenter









if __name__ == "__main__":
        main()