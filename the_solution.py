import time
from google_maps_info import top_ten_restaurants_info
import requests

def generate_html_table(restaurants):
    table_rows = ""
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
        </table>
    </body>
    </html>
    """

while True:
    try:
        restaurants_info = top_ten_restaurants_info()
        if restaurants_info is None:
            print("Error: Unable to retrieve restaurants.")
            time.sleep(60)
            continue
        
        html_content = generate_html_table(restaurants_info)
        if html_content is None:
            print("Error: Unable to generate HTML.")
            time.sleep(60)
            continue

        with open('restaurants.html', 'w') as f:
            f.write(html_content)

        print("HTML file 'restaurants.html' has been updated.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print("Retrying in 60 seconds...")
        time.sleep(60)

    time.sleep(60)  # Wait for one minute before updating again