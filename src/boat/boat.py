from pubsub import pub

from src.gps_point import GPSPoint
from src.boat.config_reader import upwind_angle


class Boat:
    """Holds information about the boat"""

    @property
    def current_position(self):
        """Gets the current position of the boat"""
        return self._current_position

    @property
    def current_heading(self):
        return self._current_heading

    def __init__(self):
        """Builds a new boat"""
        self.upwind_angle = upwind_angle()
        self._current_heading = 0
        self._current_position = GPSPoint(0, 0)
        pub.subscribe(self.read_latitude, "boat latitude")
        pub.subscribe(self.read_longitude, "boat longitude")
        pub.subscribe(self.read_heading, "boat heading")
        print("Boat ready\nupwind_angle={0}".format(self.upwind_angle))

    def read_latitude(self, latitude):
        """Updates the boat's latitude"""
        self._current_position.lat = latitude

    def read_longitude(self, longitude):
        """Updates the boat's longitude"""
        self._current_position.long = longitude

    def read_heading(self, heading):
        """Updates the boat's current heading"""
        self._current_heading = heading
