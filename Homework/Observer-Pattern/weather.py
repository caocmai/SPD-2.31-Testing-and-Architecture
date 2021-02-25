class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def registerObserver(observer):
        pass
    def removeObserver(observer):
        pass
    
    # This method is called to notify all observers
    # when the Subject's state (measuremetns) has changed.
    def notifyObservers():
        pass
    
# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and 
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        pass

# WeatherData now implements the subject/publisher interface.
class WeatherData(Subject):
    
    def __init__(self):        
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
    
    
    def registerObserver(self, observer):
        # When an observer registers, we just 
        # add it to the end of the list.
        self.observers.append(observer)
        
    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)
    
    def notifyObservers(self):
        # We notify the observers when we get updated measurements 
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)
    
    def measurementsChanged(self):
        self.notifyObservers()
    
    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        
        self.measurementsChanged()
    
    # other WeatherData methods here.

class CurrentConditionsDisplay(Observer):
    
    def __init__(self, weatherData):        
        self.temerature = 0
        self.humidity = 0
        self.pressure = 0
        
        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer 
                                           # so it gets data updates.
    def update(self, temperature, humidity, pressure):
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()
        
    def display(self):
        print("Current conditions:", self.temerature, 
              "F degrees and", self.humidity,"[%] humidity",
              "and pressure", self.pressure)
        
# TODO: implement StatisticsDisplay class and ForecastDisplay class.
class StatisticsDisplay(Observer):
    
    def __init__(self, weatherData):
        self.temperatures = []
        self.min = 0
        self.max = 0
        self.average = 0

        self.weatherData = weatherData
        weatherData.registerObserver(self)

    # These extra arguments are required but not used why?
    def update(self, temperature, humidity, pressure):
        self.temperatures.append(temperature)
        self.min = min(self.temperatures)
        self.max = max(self.temperatures)
        self.average = sum(self.temperatures) / len(self.temperatures)
        self.display()

    def display(self):
        print("Min: ", self.min, "Max: ", self.max, "Average: ", self.average)



class ForecastDisplay(Observer):

    def __init__(self, weatherData):
        self.forcast_temp = 0
        self.forcast_humidity = 0
        self.forecast_pressure = 0

        # Registering observer to subject/publisher
        self.weatherData = weatherData
        self.weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.forcast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        self.forcast_humidity = humidity - 0.9 * humidity
        self.forcast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
        self.display()

    def display(self):
        print("Forecast Temp: ", self.forcast_temp, "Forecast Humidity: ", self.forcast_humidity, 
              "Forecast Pressure: ", self.forcast_pressure)
    
class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        # current_display = CurrentConditionsDisplay(weather_data)
        # stats_display = StatisticsDisplay(weather_data)
        forcast_display = ForecastDisplay(weather_data)
        
        # TODO: Create two objects from StatisticsDisplay class and 
        # ForecastDisplay class. Also register them to the concerete instance
        # of the Subject class so the they get the measurements' updates.
        
        # The StatisticsDisplay class should keep track of the min/average/max
        # measurements and display them.
        
        # The ForecastDisplay class shows the weather Forecast based on the current
        # temperature, humidity and pressure. Use the following formuals :
        # forcast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        # forcast_humadity = humidity - 0.9 * humidity
        # forcast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
        
        weather_data.setMeasurements(80, 65,30.4)
        weather_data.setMeasurements(82, 70,29.2)
        weather_data.setMeasurements(78, 90,29.2)
        
        # un-register the observer
        # weather_data.removeObserver(current_display)
        weather_data.setMeasurements(120, 100,1000)
        weather_data.registerObserver(forcast_display)
    
        

if __name__ == "__main__":
    w = WeatherStation()
    w.main()