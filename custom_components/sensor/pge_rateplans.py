# PG&E [Residential] Rate Plan Sensor for HomeAssistant

from homeassistant.helpers.entity import Entity
import time

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""
    add_devices([RatePlanSensor()])


class RatePlanSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'PG&E Rate Plan'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return ""

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """

        if int(time.strftime("%w")) in [0, 6]:
            if int(time.strftime("%H")) in range(13, 19):
                self._state = "Peak"
            else:
                self._state = "Off-Peak"
        else:
            if int(time.strftime("%H")) in range(7, 13) or int(time.strftime("%H")) in [21, 22]:
                self._state = "Partial-Peak"
            elif int(time.strftime("%H")) in range(14, 20):
                self._state = "Peak"
            else:
                self._state = "Off-Peak"
