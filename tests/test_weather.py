import pytest
from src.weather import Weather
import pandas as pd

class Tests:

    def test_get_temperature(self):
        print("\nTesting get_temperature with London, UK")
        weather = Weather()
        temperature = weather.get_temperature("London, UK")
        print("Temperature: ", temperature)
        assert temperature['dataframe'].shape[0] > 0
        assert temperature['dataframe'].shape[1] == 2

    def test_get_temperature_with_invalid_city(self):
        print("\nTesting get_temperature with invalid city")
        weather = Weather() 
        with pytest.raises(Exception) as e:
            weather.get_temperature("LTOJOGHJ")
    
    def test_get_apparent_temperature(self):
        print("\nTesting get_apparent_temperature with London, UK")
        weather = Weather()
        temperature = weather.get_apparent_temperature("London, UK")
        print("Temperature: ", temperature)
        assert temperature['dataframe'].shape[0] > 0
        assert temperature['dataframe'].shape[1] == 2
    
    def test_get_apparent_temperature_with_invalid_city(self):
        print("\nTesting get_apparent_temperature with invalid city")
        weather = Weather() 
        with pytest.raises(Exception) as e:
            weather.get_apparent_temperature("LTOJOGHJ")
    
    def test_get_relative_humidity(self):
        print("\nTesting get_relative_humidity with London, UK")
        weather = Weather()
        humidity = weather.get_relative_humidity("London, UK")
        print("Humidity: ", humidity)
        assert humidity['dataframe'].shape[0] > 0
        assert humidity['dataframe'].shape[1] == 2