# PyOMWeather
[![Build Status](https://github.com/software-students-fall2023/3-python-package-exercise-team1-pt3/actions/workflows/python-package.yml/badge.svg)](https://github.com/software-students-fall2023/3-python-package-exercise-team1-pt3/actions/workflows/python-package.yml)


### A python module to fetch weather data from ***[Open-Meteo](https://open-meteo.com/)*** (Open Source Weather API)

## Installation

Install the PyOMWeather module using pip:

</br>


```

pip install -i https://test.pypi.org/simple/PyOMWeather==0.0.2

```

***or*** 


```

pip3 install -i https://test.pypi.org/simple/PyOMWeather==0.0.2

```
</br>

Please **make sure** to install other modules mentioned in [requirements.txt](https://github.com/software-students-fall2023/3-python-package-exercise-team1-pt3/blob/shreyas/requirements.txt) using ***pip*** as well. You can start a ***[python virtual environment](https://packaging.python.org/en/latest/tutorials/managing-dependencies/)*** so that you can organise the various python packages that are being installed. 

Please note that you can group install all dependencies using 

```
pip install -r requirements.txt
```



## Usage

Once installed, you can access weather data in your own project by importing *Weather* and creating a weather **[instance](https://www.techtarget.com/whatis/definition/instance#:~:text=In%20the%20Python%20programming%20language,an%20object%20of%20that%20class.)**.

```
from weather import Weather

weather_instance = Weather()
```

After doing this, you can use functions such as **get_temperature** for any location.

```
location = "Manhattan, New York"

temperature_data = weather_instance.get_temperature("location")

dataframe_temperature = temperature_data['dataframe']

print(f"Temperature data for {location}:")

print(dataframe_temperature)
```
</br>


#### See ***documentation*** [here](https://github.com/software-students-fall2023/3-python-package-exercise-team1-pt3/blob/shreyas/Documentation.md)


#### See an ***example file*** [here](https://github.com/software-students-fall2023/3-python-package-exercise-team1-pt3/blob/shreyas/src/__main__.py)

</br>

## Link to PyPI Website

</br>

### You can find this project on the **PYPI website** [here]()
</br>



## Contributors

- [Nawaf](https://github.com/Verse1)

- [Geoffrey](https://github.com/geoffreybudiman91)

- [Alessandro](https://github.com/alessandrolandi)

- [Shreyas](https://github.com/ShreyasUjagar)

</br>


## And You 😊?
</br>

Feel free to ***contribute*** to this project! Submit a ***Pull Request*** with clear documentation on what changes you are bringing in! 

When working with our project, please **make sure** to install other modules mentioned in [requirements.txt](https://github.com/software-students-fall2023/3-python-package-exercise-team1-pt3/blob/shreyas/requirements.txt) using ***pip*** as well. You can start a ***[python virtual environment](https://packaging.python.org/en/latest/tutorials/managing-dependencies/)*** so that you can organise the various python packages that are being installed. 

Again, please note that you can 'group install' all dependencies using 
</br>

```
pip install -r requirements.txt
```

- Use [pytest](https://docs.pytest.org/en/latest/) to write and run tests to validate that your code behaves as expected. Create as many tests as necessary to thoroughly verify each function's expected behavior - this should be no fewer than three tests per package function.
  
- Use [build](https://pypa-build.readthedocs.io/en/stable/index.html) to create the package artifacts.
- Use [GitHub Actions](https://github.com/actions) to build your package and run your tests on two different recent versions of Python with every pull request to the `main` branch of your GitHub repository.


