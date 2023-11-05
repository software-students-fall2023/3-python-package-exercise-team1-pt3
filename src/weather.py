import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
from optparse import OptionParser
from geopy.geocoders import Nominatim

class Weather:
    def __init__(self):
        self.client = openmeteo_requests.Client(session=retry(requests_cache.CachedSession('.cache', expire_after = 3600), retries = 5, backoff_factor = 0.2))
        self.geolocator = Nominatim(user_agent="weather_package")
        self.url = "https://api.open-meteo.com/v1/forecast"

    def get_temperature(self, location_string):
        # Geocode the location
        location = self.geolocator.geocode(location_string)
        if location is None:
            raise ValueError("Could not geocode the location.")

        # Prepare request parameters
        params = {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "hourly": "temperature_2m"
        }

        # Make the API call
        responses = self.client.weather_api(self.url, params=params)

        # Assuming the response is a single object and not a list
        response = responses[0]

        # Process hourly data
        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

        hourly_data = {
            "date": pd.date_range(
                start=pd.to_datetime(hourly.Time(), unit="s"),
                end=pd.to_datetime(hourly.TimeEnd(), unit="s"),
                freq=pd.Timedelta(seconds=hourly.Interval()),
                inclusive="left"
            ),
			"values": hourly_temperature_2m
        }

        hourly_dataframe = pd.DataFrame(data=hourly_data)

        return {
            'dataframe': hourly_dataframe
        }
    
    def get_apparent_temperature(self, location_string):
        # Geocode the location
        location = self.geolocator.geocode(location_string)
        if location is None:
            raise ValueError("Could not geocode the location.")

        # Prepare request parameters
        params = {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "hourly": "apparent_temperature"
        }

        # Make the API call
        responses = self.client.weather_api(self.url, params=params)

        # Assuming the response is a single object and not a list
        response = responses[0]

        # Process hourly data
        hourly = response.Hourly()
        hourly_apparent_temperature = hourly.Variables(0).ValuesAsNumpy()

        hourly_data = {
            "date": pd.date_range(
                start=pd.to_datetime(hourly.Time(), unit="s"),
                end=pd.to_datetime(hourly.TimeEnd(), unit="s"),
                freq=pd.Timedelta(seconds=hourly.Interval()),
                inclusive="left"
            ),
			"values": hourly_apparent_temperature
        }

        hourly_dataframe = pd.DataFrame(data=hourly_data)

        return {
            'dataframe': hourly_dataframe
        }
    
    def get_relative_humidity(self, location_string):
        # Geocode the location
        location = self.geolocator.geocode(location_string)
        if location is None:
            raise ValueError("Could not geocode the location.")

        # Prepare request parameters
        params = {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "hourly": "relative_humidity_2m"
        }

        # Make the API call
        responses = self.client.weather_api(self.url, params=params)

        # Assuming the response is a single object and not a list
        response = responses[0]

        # Process hourly data
        hourly = response.Hourly()
        hourly_relative_humidity = hourly.Variables(0).ValuesAsNumpy()

        hourly_data = {
            "date": pd.date_range(
                start=pd.to_datetime(hourly.Time(), unit="s"),
                end=pd.to_datetime(hourly.TimeEnd(), unit="s"),
                freq=pd.Timedelta(seconds=hourly.Interval()),
                inclusive="left"
            ),
			"values": hourly_relative_humidity
        }

        hourly_dataframe = pd.DataFrame(data=hourly_data)

        return {
            'dataframe': hourly_dataframe
        }
    
    def get_rain_probability(self, location_string):
        # Geocode the location
        location = self.geolocator.geocode(location_string)
        if location is None:
            raise ValueError("Could not geocode the location.")

        # Prepare request parameters
        params = {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "hourly": "precipitation_probability"
        }

        # Make the API call
        responses = self.client.weather_api(self.url, params=params)


    
	
	

