const search_field = document.querySelector("#search-field");
const search_btn = document.querySelector("#search-btn");
const key = '910f2b176d8e4ba2a51174633240105';
// Key:
// 910f2b176d8e4ba2a51174633240105

// Query Example:
// https://api.weatherapi.com/v1/current.json?key=910f2b176d8e4ba2a51174633240105&q=london

// OUTPUT FRONTEND (F) //
const f_city = document.querySelector("#city");
const f_region = document.querySelector("#region");
const f_country = document.querySelector("#country");
const f_local_time = document.querySelector("#local_time");
const f_condition = document.querySelector("#condition");
const f_temperature = document.querySelector("#temperature");
const frontend = [f_city, f_region, f_country, f_local_time, f_condition, f_temperature];


async function query_weather(key, query) {
    try{
        const response = await fetch(`https:api.weatherapi.com/v1/current.json?key=${key}&q=${query}` , {mode: 'cors'});
        const data = await response.json();
        // Output data
        const city = data.location.name + ',';
        const region = data.location.region;
        const country = data.location.country;
        const local_time = data.location.localtime;
        const condition = data.current.condition.text;
        const temperature = data.current.temp_c + '℃';
        const output_data = [city, region, country, local_time, condition, temperature];

        // Set content
        for (i=0; i<frontend.length; i++){
            if (region != "");
            frontend[i].textContent = output_data[i];
        }
    }
    catch(error){
        // Clear any front end values.
        for (i=0; i < frontend.length; i++){
            frontend[i].textContent = "";
        }

        // Set error message to frontend.
        f_city.innerText = "City not found!";
    }
}

search_btn.addEventListener("click", () => {
    const query = search_field.value;
    console.log(`You searched for ${query}`);
    query_weather(key, query);
})