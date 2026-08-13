"""
Problem: If weather is updated in weather station, TvDisplay and MobileDisplay should display updated weather


WeatherStation -> weather, observers
               -> add_observer(observer), remove_observer(observer), update(weather) notify_observers()

TvDisplay -> weather
          -> update_weather(weather)
          -> display_weather()

MobileDisplay -> weather
              -> update_weather(weather)
              -> display_weather()

"""

from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    @abstractmethod
    def display_weather(self):
        pass

    def update_weather(self, weather: str):
        pass


class WeatherStation:
    def __init__(self):
        self.__weather = ""
        self.__observers: List[Observer] = []

    def add_observer(self, observer: Observer):
        self.__observers.append(observer)

    def remove_observer(self, observer: Observer):
        if observer in self.__observers:
            self.__observers.remove(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update_weather(self.__weather)

    def update(self, weather):
        self.__weather = weather
        self.notify_observers()

class TvDisplay(Observer):
    def __init__(self):
        self.weather=""

    def display_weather(self):
        print(f"printing latest updated tv weather {self.weather}")
    
    def update_weather(self, weather: str):
        self.weather=weather
        self.display_weather()
    
class MobileDisplay(Observer):
    def __init__(self):
        self.weather=""
    
    def display_weather(self):
        print(f"printing latest updated mobile weather {self.weather}")

    def update_weather(self, weather: str):
        self.weather=weather
        self.display_weather()



weather_station = WeatherStation()
tv_display = TvDisplay()
mobile_display = MobileDisplay()

weather_station.add_observer(tv_display)
# weather_station.add_observer(mobile_display)

weather_station.update("12 Degrees")