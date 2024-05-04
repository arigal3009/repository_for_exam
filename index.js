console.log(`hey`);
function bring_arrey_from_transporter(){
    let arr = [];
    fetch(`http://127.0.0.1:5000/top_ten_restaurants_info`)
        .then(response => response.json())
        .then(data => {
            arr = JSON.parse(data); 
            console.log(arr);
        })
        .catch(error => console.error('Error:', error));
        return arr;
}
function updaterestaurants(){
    let arrey = bring_arrey_from_transporter();
    let g;
    for(i = 0; i < 10; i++){
        g = i + 1; /* for variables in html */
        document.getElementsById(`n${g}`).textContect = arrey[i][0];
        document.getElementsById(`r${g}`).textContect = arrey[i][1];
        document.getElementsById(`b${g}`).textContect = arrey[i][2];
    }
}
    updaterestaurants();
    let time = 60000;
    setInterval(updaterestaurants, time);
