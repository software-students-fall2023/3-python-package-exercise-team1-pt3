from PyOMWeather.weather import Weather 

weather_instance = Weather()

location = "Manhattan, New York"

temperature_data = weather_instance.get_temperature("location")
dataframe_temperature = temperature_data['dataframe']
apparent_temperature_data = weather_instance.get_apparent_temperature("location")
dataframe_apparent_temperature = apparent_temperature_data['dataframe']
humidity_data = weather_instance.get_relative_humidity("location")
dataframe_humidity = humidity_data['dataframe']
rain_data = weather_instance.get_rain_probability("location")
dataframe_rain = rain_data['dataframe']

print(f"Temperature data for {location}:")
print(dataframe_temperature)
print(f"Apparent Temperature data for {location}:")
print(dataframe_apparent_temperature)
print(f"Relative Humidity data for {location}:")
print(dataframe_humidity)
print(f"Rain Probability data for {location}:")
print(dataframe_rain)