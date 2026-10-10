function updateTimer(){
    fetch("/timer")
    .then(response=>response.json())
    .then(data=>{
        for(let i=0;i<6;i++)
{

document.getElementById("timer"+(i+1))
.innerHTML=data.values[i];

}
    });
}


setInterval(updateTimer,1000);