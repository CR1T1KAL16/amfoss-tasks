document.addEventListener('DOMContentLoaded', function () {
    const locationInput = document.getElementById('locationInput');
    const searchButton = document.getElementById('searchButton');
    const weatherInfo = document.getElementById('weatherInfo');
    const body = document.body;
    
    searchButton.addEventListener('click', () => {
      const location = locationInput.value;
      if (location) {
        fetch(`https://api.openweathermap.org/data/2.5/weather?q=${location}&appid=9dc4673421356e048d8aa80306ecc942`)
          .then(response => response.json())
          .then(data => {
            const weatherDescription = data.weather[0].description;
            const temperature = (data.main.temp - 273.15).toFixed(2); 
            weatherInfo.textContent = `Weather in ${location}: ${weatherDescription}, Temperature: ${temperature}°C`;

            if (weatherDescription.includes("clouds")) {
              body.style.backgroundImage = 'url("cloudy.jpg")';
            } else if (weatherDescription.includes("clear")) {
              body.style.backgroundImage = 'url("clear.jpeg")';
            } else if (weatherDescription.includes("rain")) {
              body.style.backgroundImage = 'url("rain.jpg")';
            } else {
              body.style.backgroundImage = 'none';
           }
           
            
            
          })
          .catch(error => {
            console.error('Error fetching weather data:', error);
            weatherInfo.textContent = 'Invalid City/Country name!';
            body.style.backgroundImage = 'none';
          });
      }
    });
  });