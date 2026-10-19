
#  WEATHER ANALYZER 

# Features:
# 1. Average Temperature
# 2. Maximum Temperature
# 3. Minimum Temperature
# 4. Average Humidity
# 5. Total Rainfall
# 6. Hottest Day
# 7. Coldest Day
# 8. Rainiest Day
# 9. Temperature Standard Deviation
# 10. Temperature/Humidity Correlation
# 11. Temperature/Rainfall Correlation
# 12. Temperature Changes


#  IMPORTS 

import numpy as np
import pandas as pd
from pathlib import Path


#  READ DATASET 

data_path = Path(__file__).with_name("weather_data.csv")
data = pd.read_csv(data_path)


#  EXTRACT COLUMNS 

date = data["date"].to_numpy()
day = data["day"].to_numpy()
min_temp = data["min_temp"].to_numpy()
max_temp = data["max_temp"].to_numpy()
temperature = data["temperature"].to_numpy()
humidity = data["humidity"].to_numpy()
rainfall_mm = data["rainfall_mm"].to_numpy()


#  WEATHER ANALYZER CLASS 

class WeatherAnalyzer:

    # 1. Average Temperature
    @staticmethod
    def AverageTemperature():
        print("Average Temperature:", np.mean(temperature))

    # 2. Maximum Temperature
    @staticmethod
    def MaximumTemperature():
        print("Maximum Temperature:", np.max(temperature))

    # 3. Minimum Temperature
    @staticmethod
    def MinimumTemperature():
        print("Minimum Temperature:", np.min(temperature))

    # 4. Average Humidity
    @staticmethod
    def AverageHumidity():
        print("Average Humidity:", np.mean(humidity), "%")

    # 5. Total Rainfall
    @staticmethod
    def TotalRainfall():
        print("Total Rainfall:", np.sum(rainfall_mm), "mm")

    # 6. Hottest Day
    @staticmethod
    def HottestDay():
        i = np.argmax(temperature)

        print("Hottest Day:", date[i], day[i])
        print("Temperature:", temperature[i])

    # 7. Coldest Day
    @staticmethod
    def ColdestDay():
        i = np.argmin(temperature)

        print("Coldest Day:", date[i], day[i])
        print("Temperature:", temperature[i])

    # 8. Rainiest Day
    @staticmethod
    def RainiestDay():
        i = np.argmax(rainfall_mm)

        print("Rainiest Day:", date[i], day[i])
        print("Rainfall:", rainfall_mm[i], "mm")

    # 9. Temperature Standard Deviation
    @staticmethod
    def TemperatureStandardDeviation():
        print(
            "Temperature Standard Deviation:",
            np.std(temperature)
        )

    # 10. Temperature/Humidity Correlation
    @staticmethod
    def TemperatureHumidityCorrelation():
        correlation = np.corrcoef(temperature, humidity)[0, 1]

        print("Temperature/Humidity Correlation:", correlation)

    # 11. Temperature/Rainfall Correlation
    @staticmethod
    def TemperatureRainfallCorrelation():
        correlation = np.corrcoef(temperature, rainfall_mm)[0, 1]

        print("Temperature/Rainfall Correlation:", correlation)

    # 12. Temperature Changes
    @staticmethod
    def ChangeInTemperature():
        changes = np.diff(temperature)

        print("Temperature Changes:", changes)

        print("\nDay-to-Day Changes:")

        for i in range(1, len(temperature)):
            change = temperature[i] - temperature[i - 1]

            if change > 0:
                status = "Increased"
            elif change < 0:
                status = "Decreased"
            else:
                status = "No Change"

            print(
                date[i],day[i],"| Change:",change,"|",status)


print(" WEATHER ANALYZER ")

while True:

    print("\n1. Average Temperature")
    print("2. Maximum Temperature")
    print("3. Minimum Temperature")
    print("4. Average Humidity")
    print("5. Total Rainfall")
    print("6. Hottest Day")
    print("7. Coldest Day")
    print("8. Rainiest Day")
    print("9. Temperature Standard Deviation")
    print("10. Temperature/Humidity Correlation")
    print("11. Temperature/Rainfall Correlation")
    print("12. Change in Temperature")
    print("0. Exit")

    try:
        n = int(input("\nEnter Your Command: "))

    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    match n:

        case 1:
            WeatherAnalyzer.AverageTemperature()

        case 2:
            WeatherAnalyzer.MaximumTemperature()

        case 3:
            WeatherAnalyzer.MinimumTemperature()

        case 4:
            WeatherAnalyzer.AverageHumidity()

        case 5:
            WeatherAnalyzer.TotalRainfall()

        case 6:
            WeatherAnalyzer.HottestDay()

        case 7:
            WeatherAnalyzer.ColdestDay()

        case 8:
            WeatherAnalyzer.RainiestDay()

        case 9:
            WeatherAnalyzer.TemperatureStandardDeviation()

        case 10:
            WeatherAnalyzer.TemperatureHumidityCorrelation()

        case 11:
            WeatherAnalyzer.TemperatureRainfallCorrelation()

        case 12:
            WeatherAnalyzer.ChangeInTemperature()

        case 0:
            print("Thank you for using Weather Analyzer!")
            break

        case _:
            print("Invalid choice! Enter a number from 0 to 12.")

