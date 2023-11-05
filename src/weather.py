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

    def get_weather_data(self, location_string):
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

        # Extract information from the response
        coordinates = (response.Latitude(), response.Longitude())
        elevation = response.Elevation()
        timezone_info = (response.Timezone(), response.TimezoneAbbreviation(), response.UtcOffsetSeconds())

        # Process hourly data
        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

        hourly_data = {
            "date": pd.date_range(
                start=pd.to_datetime(hourly.Time(), unit="s"),
                end=pd.to_datetime(hourly.TimeEnd(), unit="s"),
                freq=pd.Timedelta(seconds=hourly.Interval()),
                inclusive="left"
            )
        }

        hourly_dataframe = pd.DataFrame(data=hourly_data)

        return {
            'coordinates': coordinates,
            'elevation': elevation,
            'timezone_info': timezone_info,
            'dataframe': hourly_dataframe
        }

