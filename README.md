# PyOMWeather
[![Build Status](https://github.com/software-students-fall2023/3-python-package-exercise-team1-pt3/actions/workflows/python-package.yml/badge.svg)](https://github.com/software-students-fall2023/3-python-package-exercise-team1-pt3/actions/workflows/python-package.yml)


### A python module to fetch weather data from Open-Meteo (Open Source Weather API)

## Installation

Install the PyOMWeather module using pip:

```

pip install -i https://test.pypi.org/simple/PyOMWeather==0.0.2

```

or 


```

pip3 install -i https://test.pypi.org/simple/PyOMWeather==0.0.2

```


## Usage

Once installed, you can access weather data in your own project by importing *Weather* and creating a weather **[instance](https://www.techtarget.com/whatis/definition/instance#:~:text=In%20the%20Python%20programming%20language,an%20object%20of%20that%20class.)**.

```
from weather import Weather

weather_instance = Weather()
```

After doing this, you can use functions such as *get_temperature* and *get_rain_probability* for any location.

```
location = "Manhattan, New York"

temperature_data = weather_instance.get_temperature("location")

dataframe_temperature = temperature_data['dataframe']

print(f"Temperature data for {location}:")

print(dataframe_temperature)
```

