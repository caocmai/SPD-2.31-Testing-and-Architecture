# by Kami Bigdely
# Docstrings and blank lines
class OnBoardTemperatureSensor:
    """Get the onboard temperature ."""
    VOLTAGE_TO_TEMP_FACTOR = 5.6
    def __init__(self):
        pass

    def read_voltage(self):
        """Read the voltage."""
        return 2.7
        
    def get_temperature(self):
        """Get the temperture.
        Returns:
            The onboard temperature.    
        """
        return self.read_voltage() * OnBoardTemperatureSensor.VOLTAGE_TO_TEMP_FACTOR # [celcius]

class CarbonMonoxideSensor:
    """Determine the carbon monoxide level.
    Args: 
        temperature_sensor: The temperature gotten from the sensor
    """
    VOLTAGE_TO_CO_FACTOR = 0.048
    def __init__(self, temperature_sensor):
        self.on_board_temp_sensor = temperature_sensor
        if not self.on_board_temp_sensor:
            self.on_board_temp_sensor = OnBoardTemperatureSensor()

    def get_carbon_monoxide_level(self):
        """Get the carbon monoxide level.
        Returns:
            The carbon monoxide level.
        """
        sensor_voltage = self.read_sensor_voltage()
        self.carbon_monoxide = CarbonMonoxideSensor.convert_volt_to_co2_lvl(self, sensor_voltage, 
                                                                            self.on_board_temp_sensor.get_temperature())
        return self.carbon_monoxide

    def read_sensor_voltage(self):
        """Read the sensor voltage.
        Returns:
            The voltage from the sensor.
        """
        # In real life, it should read from hardware.        
        return 2.3

    def convert_volt_to_co2_lvl(self, voltage, temperature):
        """Convert the voltage to carbon monoxide level.

        Returns:
            The carbon monoxide level.
        """
        return voltage * CarbonMonoxideSensor.VOLTAGE_TO_CO_FACTOR * temperature

class DisplayUnit:
    """Disply the message."""
    def __init__(self):
        self.string = ''

    def display(self, msg):
        """Display the message."""
        print(msg)

class CarbonMonoxideDevice():
    """Display the carbon monoxide level of device."""
    def __init__(self, co_sensor, display_unit):
        self.carbonMonoxideSensor = co_sensor 
        self.display_unit = display_unit    

    def display(self):
        """Show the carbon monoxide level."""
        msg = 'Carbon Monoxide Level is : ' + str(self.carbonMonoxideSensor.get_carbon_monoxide_level())
        self.display_unit.display(msg)

if __name__ == "__main__":
    temp_sensor = OnBoardTemperatureSensor()
    co_sensor = CarbonMonoxideSensor(temp_sensor)
    display_unit = DisplayUnit()
    co_device = CarbonMonoxideDevice(co_sensor, display_unit)
    co_device.display()
    