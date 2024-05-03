function updaterestaurants(){
    let arr = [];
    fetch('http://127.0.0.1:5000/get_google_maps_info')
        .then(response => response.json())
        .then(data => {
            arr = JSON.parse(data); 
        })
        .catch(error => console.error('Error:', error));
        for(i = 0; i < 10; i++){
            document.getElementsById("n${i}").textContect = arr[i][0]
            document.getElementsById("r${i}").textContect = arr[i][1]
            document.getElementsById("b${i}").textContect = arr[i][1]
        }
    }
    let time = 60000
    setInterval(updaterestaurants, time)
