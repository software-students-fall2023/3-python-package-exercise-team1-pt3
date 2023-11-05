import pytest
from src.weather import Weather
import pandas as pd

class Tests:
    
    def test_get_temperature():
        print("Testing get_temperature")
        weather = Weather()
        temperature = weather.get_temperature("London, UK")
        assert temperature['dataframe'].shape[0] > 0
        assert temperature['dataframe'].shape[1] == 2
