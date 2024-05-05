import time
from google_maps_info import top_ten_restaurants_info

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
    restaurants_info = top_ten_restaurants_info()
    html_content = generate_html_table(restaurants_info)

    with open('restaurants.html', 'w') as f:
        f.write(html_content)

    print("HTML file 'restaurants.html' has been updated.")
    time.sleep(60)  # Wait for one minute before updating again