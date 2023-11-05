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
