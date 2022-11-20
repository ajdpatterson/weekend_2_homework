import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1)
        self.guest = Guest("Jim", 100, "Enter Sandman")
        self.song1 = Song("Enter Sandman", "Metallica", "Metal")
        self.song2 = Song("Song 2", "Blur", "Alt Rock")
        self.song3 = Song("Black Hole Sun", "Soundgarden", "Metal")
        self.song4 = Song("Where Is My Mind?", "Pixies", "Alt Rock")
        self.song5 = Song("Folsom Prison Blues", "Johnny Cash", "Folk Rock")
        self.room.add_song_to_room(self.song1)
        self.room.add_song_to_room(self.song2)
        self.room.add_song_to_room(self.song3)

    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest)
        expected_output = 1
        self.assertEqual(expected_output, len(self.room.guest_list))
    
    def test_remove_guest_from_room(self):
        self.room.add_guest_to_room(self.guest)
        self.room.remove_guest_from_room(self.guest)
        expected_output = 0
        self.assertEqual(expected_output, len(self.room.guest_list))

    def test_add_song_to_room(self):
        self.room.add_song_to_room(self.song4)
        expected_output = 4
        self.assertEqual(expected_output, len(self.room.track_list))

    def test_remove_song_from_room(self):
        self.room.add_song_to_room(self.song4)
        self.room.remove_song_from_room(self.song4)
        expected_output = 3
        self.assertEqual(expected_output, len(self.room.track_list))

    def test_can_check_room_at_capacity(self):
        self.room.guest_list = ["Jo", "James", "Jenny", "Jarvis"]
        self.room.add_guest_to_room(self.guest)
        expected_outcome = 4
        self.assertEqual(expected_outcome, len(self.room.guest_list))

    def test_can_charge_guest(self):
        expected_outcome = 90
        self.room.add_guest_to_room(self.guest)
        self.room.charge_guest(self.guest)
        self.assertEqual(expected_outcome, self.guest.wallet)

    def test_can_display_songs_by_genre(self):

        expected_outcome = [{"track name": "Enter Sandman", "artist name": "Metallica", "genre": "Metal"}, {"track name": "Black Hole Sun", "artist name": "Soundgarden", "genre": "Metal"}]
        actual_outcome =  self.room.display_songs_by_genre(input("Enter genre: "))
        # self.assertEqual(expected_outcome, self.room.display_songs_by_genre(input("Enter genre: ")))
        self.assertEqual(expected_outcome, actual_outcome)

    def test_can_output_tracklist(self):
        expected_outcome = [{"track name": "Enter Sandman", "artist name": "Metallica", "genre": "Metal"}, {"track name": "Song 2", "artist name": "Blur", "genre": "Alt Rock"}, {"track name": "Black Hole Sun", "artist name": "Soundgarden", "genre": "Metal"}]
        actual_outcome = self.room.display_songs(self.room.track_list)