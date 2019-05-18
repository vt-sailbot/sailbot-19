import unittest
from unittest.mock import patch, MagicMock

from src.autopilot.helmsman import Helmsman


class RCReceiverTests(unittest.TestCase):
    """Tests methods in RCReceiver"""

    def setUp(self):
        """Sets up a receiver for each test method"""
        self.r = Helmsman(0)

    def test_rudder_angle(self):
        """Tests that the autopilot calculates rudder angles correctly"""

    @patch('src.autopilot.helmsman.pub', autospec=True)
    def test_turn_to(self, mock_pub):
        """Tests that the autopilot sets the right turn angles"""
        boat = MagicMock(name="src.boat")
        boat.current_heading = 0
        test_inputs = [90, -90, 0, 45, 180, -180]
        scaled_outputs = [90, -90, 45, 180, 180, 180]

        for test_input, scaled_output in zip(test_inputs, scaled_outputs):
            self.r.turn_to(test_input, boat)

            mock_pub.sendMessage.assert_any_call("set rudder", degrees_starboard=scaled_output)


if __name__ == "__main__":
    unittest.main()
