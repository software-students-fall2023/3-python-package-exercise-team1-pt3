# Documentation

</br> 

### `get_temperature(location_string)`


</br>

Retrieves the ***hourly temperature data***.


</br>


**Arguments:**

- `location_string`: A string representing the location.

</br>

**Returns:**
- A pandas DataFrame with two columns: 'date' and 'values' for temperatures.

</br> 

**Usage:**

```
temperature_df = weather.get_temperature("New York, NY")
print(temperature_df['dataframe'])
```
</br>
</br> 


### `get_apparent_temperature(location_string)`

</br>

*Retrieves the hourly ***apparent*** temperature data.*
</br>
</br>

**Arguments:**
- `location_string`: A string representing the location.

</br> 

**Returns:**
- A pandas DataFrame with hourly apparent temperature data.

</br> 

**Usage:**

```
apparent_temp_df = weather.get_apparent_temperature("New York, NY")
print(apparent_temp_df['dataframe'])
```
</br>
</br> 

### `get_relative_humidity(location_string)`


</br> 

Retrieves the hourly ***relative*** humidity data.

</br> 

**Arguments:**
- `location_string`: A string representing the location.

</br> 

**Returns:**
- A pandas DataFrame with hourly relative humidity data.

</br> 

**Usage:**


```
humidity_df = weather.get_relative_humidity("New York, NY")
print(humidity_df['dataframe'])
```

</br>
</br> 

### `get_rain_probability(location_string)`

</br> 

Retrieves the hourly ***precipitation*** probability data.

</br> 

**Arguments:**
- `location_string`: A string representing the location.

</br> 

**Returns:**

- A pandas DataFrame with hourly ***precipitation*** probability data.

</br> 

**Usage:**

```o0i0i
rain_prob_df = weather.get_rain_probability("New York, NY")
print(rain_prob_df['dataframe'])
```
</br>
 

## Example

An example python file that implements these functions is linked [here](https://github.com/software-students-fall2023/3-python-package-exercise-team1-pt3/blob/main/src/__main__.py).
