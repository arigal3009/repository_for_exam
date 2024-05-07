import time # for the sleep function
from google_maps_info import top_ten_restaurants_info
from flask import Flask
counter = 0 # so i can see if the restaurants are updated

app = Flask(__name__)

# returns the counter
def modify_global():
    global counter
    counter += 1
    return counter

#builds the script for the html file using the info that he gets and the counter function
def generate_html_table(restaurants):
    modify_global()
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

#the spicific route in the local web browser that activate the index function
@app.route('/')
#checks if the info that is needed to create the html file is in the variables and if so it creates the html file(every time i refresh the page this function is called)
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

"""
#unless I press ctrl c this will repeat itself forever and will recreate a html file with the needed info in it every minute
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
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)
    #main()
