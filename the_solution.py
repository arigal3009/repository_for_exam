import time # for the sleep function
from google_maps_info import top_ten_restaurants_info
import requests # for catching errors made by request action(because of bad connection this error repeats itself a lot)
from flask import Flask
counter = 0 # so i can see if the restaurants are updated


app = Flask(__name__)

def generate_html_table(restaurants):
    table_rows = ""
    counter_line = f"<h2> number of restarts is {counter}"
    for restaurant in restaurants:
        name, rating, open_now = restaurant
        table_rows += f"<tr><td>{name}</td><td>{rating}</td><td>{'Open' if open_now else 'Closed'}</td></tr>"
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Top Ten Restaurants</title>
    </head>
    <body>
        <h1>Top Ten Restaurants</h1>
        <table border="1">
            <tr>
                <th>Name</th>
                <th>Rating</th>
                <th>Open</th>
            </tr>
            {table_rows}
            {counter_line}
        </table>
    </body>
    </html>
    """
#unless i press ctrl c this will repeat itself forever and will recreate a html file with the needed info in it every minute

@app.route('/')
def index():
    restaurants_info = top_ten_restaurants_info()
    if restaurants_info is None:
        return "Error: Unable to retrieve restaurant information."
    
    html_content = generate_html_table(restaurants_info)
    if html_content is None:
        return "Error: Unable to generate HTML content."

    with open('restaurants.html', 'w') as file:
        file.write(html_content)

    return html_content

def main():
    while True:
        time.sleep(60)  # Wait for one minute before updating again
        restaurants_info = top_ten_restaurants_info()
        if restaurants_info is None:
            print("Error: Unable to retrieve restaurant information.")
            continue
        
        html_content = generate_html_table(restaurants_info)
        if html_content is None:
            print("Error: Unable to generate HTML content.")
            continue

        with open('restaurants.html', 'w') as file:
            file.write(html_content)

        print("HTML file 'restaurants.html' has been updated.")

if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0', port=4444)