import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from src.broadcaster.broadcaster import BroadcasterType, make_broadcaster


class BroadcasterTests(unittest.TestCase):
    """ Tests Broadcaster methods. """

    def setUp(self):
        """ Create testing fields """
        self.testable = make_broadcaster()
        self.messenger = make_broadcaster(
            broadcaster_type=BroadcasterType.Messenger)
        self.filewriter = make_broadcaster(
            broadcaster_type=BroadcasterType.FileWriter, filename="test.txt")
        self.data = {
            1 : "test",
            2 : "test2",
            3 : "test3"
        }

    def test_update_data(self):
        """ Tests update data for broadcasters """
        self.testable.update_data()
        self.messenger.update_data()
        self.filewriter.update_data()

        self.assertEqual(self.testable.data, None)
        self.assertEqual(self.messenger.data, None)
        self.assertEqual(self.filewriter.data, None)

        self.testable.update_data(self.data)
        self.messenger.update_data(self.data)
        self.filewriter.update_data(self.data)

        self.assertEqual(self.testable.data, self.data)
        self.assertEqual(self.messenger.data, self.data)
        self.assertEqual(self.filewriter.data, self.data)

    @patch('src.broadcaster.broadcaster.open')
    @patch('src.broadcaster.broadcaster.pub')
    def test_read_data(self, mock_open, mock_pub):
        """ Tests read data """
        self.assertEqual(self.testable.read_data(), None)
        self.assertEqual(self.messenger.read_data(), None)
        self.assertEqual(self.filewriter.read_data(), None)

        self.testable.update_data(self.data)
        self.messenger.update_data(self.data)
        self.filewriter.update_data(self.data)

        self.assertEqual(self.testable.read_data(), None)
        self.assertEqual(self.messenger.read_data(), None)
        self.assertEqual(self.filewriter.read_data(), None)

        self.assertEqual(self.testable.read_data(key="inval"), None)
        self.assertEqual(self.messenger.read_data(key="inval"), None)
        self.assertEqual(self.filewriter.read_data(key="inval"), None)

        self.assertEqual(self.testable.read_data(key=1), "test")
        self.assertEqual(self.messenger.read_data(key=2), "test2")
        self.assertEqual(self.filewriter.read_data(key=3), "test3")
