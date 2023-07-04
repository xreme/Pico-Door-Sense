//send an AJAX request to the server
function updateData(){{
    //create a new XMLHttpRequest object
    var xhttp = new XMLHttpRequest();
    //set the onreadystatechange to a function that will handle the response
    xhttp.onreadystatechange = function(){{
        if(this.readyState == 4 && this.status == 200){{
            //parse the responseText
            var data = JSON.parse(this.responseText);
           
            //update DOM
            document.getElementById("temperature").textContent = data.temperature;
            document.getElementById("he_sensor_value").textContent = data.he_sensor_value;

            //update the ascii art
            document.body.style.background = data.he_sensor_value == "OPEN" ? "RED" : "GREEN";

            //display timestamp which the information was last updated
            displayDateTime();
        }}
    }}
    //open & send the request
    xhttp.open("GET", "/data", true);
    xhttp.send();
    }}

//display the current date and time
function displayDateTime(){{
    var currentdate = new Date();
    var date = currentdate.toLocaleDateString();
    var time = currentdate.toLocaleTimeString();
    document.getElementById("current-date").textContent = date;
    document.getElementById("current-time").textContent = time;
}}

//call the updateData function every second
setInterval(updateData, 1000);