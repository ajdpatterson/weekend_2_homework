import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Bilbo", 100, "Enter Sandman")
        self.room = Room(1)
        self.room.song1 = Song("Enter Sandman", "Metallica", "Metal")
        self.room.add_song_to_room(self.room.song1)
    def test_guest_has_name(self):
        expected_output = "Bilbo"
        self.assertEqual(expected_output, self.guest.name)

    def test_guest_has_wallet(self):
        expected_output = 100
        self.assertEqual(expected_output, self.guest.wallet)

    def test_guest_happy_favourite_song_in_room(self):
        track_list = self.room.track_list
        expected_output = "Woohoo!"
        actual_output = self.guest.check_favourite_song_in_room(track_list)
        self.assertEqual(expected_output, actual_output)