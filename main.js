//send an AJAX request to the server every 1 second
function updateData(){{
    //create a new XMLHttpRequest object
    var xhttp = new XMLHttpRequest();
    //set the onreadystatechange to a function that will handle the response
    xhttp.onreadystatechange = function(){{
        if(this.readyState == 4 && this.status == 200){{
            //parse the responseText
            var data = JSON.parse(this.responseText);
           
            //update DOM
            document.getElementById("state").textContent = data.state;
            document.getElementById("temperature").textContent = data.temperature;
            document.getElementById("he_sensor_value").textContent = data.he_sensor_value;
        }}
    }}
    xhttp.open("GET", "/data", true);
    xhttp.send();
    }}
    setInterval(updateData, 1000);