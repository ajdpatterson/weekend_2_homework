import unittest
from classes.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Enter Sandman", "Metallica", "Metal")
    
    def test_has_track_name(self):
        expected_output = "Enter Sandman"
        self.assertEqual(expected_output, self.song.metadata["track name"])