let aliveSeconds = 0;
let heartbeatRate = 5000;

function time() {
    let d = new Date();
    let currentSecond = d.getTime();
    if(currentSecond - aliveSeconds > heartbeatRate + 1000)
    {
        document.getElementById("connection_id").innerHTML = "Offline";
       
    }
    else{
        document.getElementById("connection_id").innerHTML = "Online";

    }
    setTimeout(time, 1000);
}

function keepAlive()
{
    fetch(/keep_alive/).then(response => {
        if(response.ok){
            let date = new Date();
            aliveSeconds = date.getTime();
            return response.json();
        }
        throw new Error('Request failed.');
    })
    .then(responseJson => console.log(responseJson))
    .catch(error => console.log(error));
    setTimeout('keepAlive()', heartbeatRate);
}