import unittest
from television import Television


class TestTelevision(unittest.TestCase):

    def setUp(self):
        """Set up the initial state of the television for testing."""
        self.tv = Television()

    def test_init(self):
        """Test that the TV is initialized with the correct values."""
        self.assertEqual(str(self.tv), "Power: False, Channel: 0, Volume: 0")

    def test_power_on(self):
        """Test that the TV can be powered on."""
        self.tv.power()
        self.assertEqual(str(self.tv), "Power: True, Channel: 0, Volume: 0")

    def test_power_off(self):
        """Test that the TV can be powered off."""
        self.tv.power()
        self.tv.power()
        self.assertEqual(str(self.tv), "Power: False, Channel: 0, Volume: 0")

    def test_mute(self):
        """Test muting the TV."""
        self.tv.power()  # Turn on the TV
        self.tv.mute()
        self.assertEqual(str(self.tv), "Power: True, Channel: 0, Volume: 0")

    def test_unmute(self):
        """Test unmuting the TV."""
        self.tv.power()  # Turn on the TV
        self.tv.mute()  # Mute the TV
        self.tv.mute()  # Unmute the TV
        self.assertEqual(str(self.tv), "Power: True, Channel: 0, Volume: 0")

    def test_mute_unmute_after_volume_change(self):
        """Test mute/unmute behavior after volume change."""
        self.tv.power()  # Turn on the TV
        self.tv.volume_up()  # Increase volume
        self.tv.mute()  # Mute the TV
        self.assertEqual(str(self.tv), "Power: True, Channel: 0, Volume: 0")  # Volume should be 0
        self.tv.mute()  # Unmute the TV
        self.assertEqual(str(self.tv), "Power: True, Channel: 0, Volume: 1")  # Volume should be restored

    def test_channel_up(self):
        """Test increasing the channel."""
        self.tv.power()  # Turn on the TV
        self.tv.channel_up()
        self.assertEqual(str(self.tv), "Power: True, Channel: 1, Volume: 0")
        self.tv.channel_up()
        self.assertEqual(str(self.tv), "Power: True, Channel: 2, Volume: 0")
        self.tv.channel_up()
        self.assertEqual(str(self.tv), "Power: True, Channel: 3, Volume: 0")
        self.tv.channel_up()
        self.assertEqual(str(self.tv), "Power: True, Channel: 0, Volume: 0")  # Channel should wrap around

    def test_channel_down(self):
        """Test decreasing the channel."""
        self.tv.power()  # Turn on the TV
        self.tv.channel_down()
        self.assertEqual(str(self.tv), "Power: True, Channel: 3, Volume: 0")  # Channel wraps around
        self.tv.channel_down()
        self.assertEqual(str(self.tv), "Power: True, Channel: 2, Volume: 0")

    def test_volume_up(self):
        """Test increasing the volume."""
        self.tv.power()  # Turn on the TV
        self.tv.volume_up()
        self.assertEqual(str(self.tv), "Power: True, Channel: 0, Volume: 1")
        self.tv.volume_up()
        self.assertEqual(str(self.tv), "Power: True, Channel: 0, Volume: 2")
        self.tv.volume_up()  # Should not increase beyond MAX_VOLUME
        self.assertEqual(str(self.tv), "Power: True, Channel: 0, Volume: 2")

    def test_volume_up_when_muted(self):
        """Test increasing volume when the TV is muted."""
        self.tv.power()  # Turn on the TV
        self.tv.mute()  # Mute the TV
        self.tv.volume_up()
        self.assertEqual(str(self.tv), "Power: True, Channel: 0, Volume: 1")  # Should unmute and set volume to 1

    def test_volume_down(self):
        """Test decreasing the volume."""
        self.tv.power()  # Turn on the TV
        self.tv.volume_up()  # Increase volume to test downwards
        self.tv.volume_down()
        self.tv.volume_down()
        self.assertEqual(str(self.tv), "Power: True, Channel: 0, Volume: 0")  # Should not go below MIN_VOLUME

    def test_volume_down_when_muted(self):
        """Test decreasing volume when the TV is muted."""
        self.tv.power()  # Turn on the TV
        self.tv.mute()  # Mute the TV
        self.tv.volume_down()
        self.assertEqual(str(self.tv), "Power: True, Channel: 0, Volume: 0")  # Volume stays 0 when muted

    def test_power_when_muted(self):
        """Test power on/off behavior when the TV is muted."""
        self.tv.power()  # Turn on the TV
        self.tv.mute()  # Mute the TV
        self.tv.power()  # Turn off the TV
        self.assertEqual(str(self.tv), "Power: False, Channel: 0, Volume: 0")  # TV should be off
        self.tv.power()  # Turn on the TV again
        self.assertEqual(str(self.tv), "Power: True, Channel: 0, Volume: 0")  # Should stay muted


if __name__ == '__main__':
    unittest.main()
