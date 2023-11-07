# PyOMWeather

[![Build Status](https://github.com/software-students-fall2023/3-python-package-exercise-team1-pt3/actions/workflows/python-package.yml/badge.svg)](https://github.com/software-students-fall2023/3-python-package-exercise-team1-pt3/actions/workflows/python-package.yml)


### A python module to fetch weather data from ***[Open-Meteo](https://open-meteo.com/)***

## Installation

```PyOMWeather``` is available on [PyPi](https://pypi.org/project/PyOMWeather/) :

Install the package using pip:

```bash

pip install  PyOmWeather

```

## Usage

```PyOMWeather``` is meant to be used in your own Python programs. The ```PyOMWeather.weather``` module contains a class called *Weather* that contains functions that can access data from OpenMeteo's API for your Python programs. To do this, you can import ```Weather``` and create a weather **[instance](https://www.techtarget.com/whatis/definition/instance#:~:text=In%20the%20Python%20programming%20language,an%20object%20of%20that%20class.)**.

  

```python

from PyOMWeather.weather import Weather

weather_instance = Weather()

```

The weather class contains four methods that can access different data from OpenMeteo's API

### `get_temperature(location_string)`

Retrieves the ***hourly temperature*** data.

**Arguments:**

-  `location_string`: A string representing the location.

**Returns:**

- A pandas DataFrame with two columns: 'date' and 'values' for temperatures.

### `get_apparent_temperature(location_string)`

Retrieves the hourly ***apparent temperature*** data.

**Arguments:**

-  `location_string`: A string representing the location.

**Returns:**

- A pandas DataFrame with hourly apparent temperature data.

### `get_relative_humidity(location_string)`

Retrieves the hourly ***relative humidity*** data.

**Arguments:**

-  `location_string`: A string representing the location.

**Returns:**

- A pandas DataFrame with hourly relative humidity data.

### `get_rain_probability(location_string)`

Retrieves the hourly ***rain probability*** data.

**Arguments:**

-  `location_string`: A string representing the location.

**Returns:**

- A pandas DataFrame with hourly ***precipitation*** probability data.

An example Python program that uses each of the functions and prints the fetched data is provided [here](example-program.py)

## Contributing

  
If you want to contribute to ```PyOMWeather```, follow these steps to set up your development environment: 
1.  **Fork the Project**: Create your own fork of the project to work on. This will allow you to make changes to your own copy of the project. 
2.   **Clone your fork**: Clone your fork to your local machine. 
```bash 
git clone https://github.com/your-username/3-python-package-exercise-team1-pt3.git 
cd 3-python-package-exercise-team1-pt3 
``` 
3. **Set up your Virtual Environment**: It's recommended to use a virtual environment to keep dependencies required by different projects separate. Create a virtual environment by running: 
```bash 
python -m venv venv 
```
Activate the virtual environment: 
On Windows: 
```bash 
.\venv\Scripts\activate 
``` 
On MacOS/Linux: 
```bash 
source venv/bin/activate 
``` 
4. **Install Dependencies**: Install all required dependencies using the `requirements.txt` file
```bash 
pip install -r requirements.txt 
``` 
5. **Make Your Changes**: Make your changes to the codebase. Be sure to write or update tests as appropriate. 
6. **Run the Tests**: Before submitting your changes, make sure all tests pass: 
```bash 
pytest 
``` 
8. **Submit a Pull Request** : Once you've made your changes, tested everything, and are happy with the result, push your changes to your fork and submit a pull request to the main repository. 
Don't forget to update the documentation if needed. 
Thank you for your contributions!

## Authors

- [Nawaf](https://github.com/Verse1)
- [Geoffrey](https://github.com/geoffreybudiman91)
- [Alessandro](https://github.com/alessandrolandi)
- [Shreyas](https://github.com/ShreyasUjagar)