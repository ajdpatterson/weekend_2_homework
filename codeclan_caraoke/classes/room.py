class Room:


    def __init__(self, room_number):
        self.room_number = room_number
        self.guest_list = []
        self.track_list = []
        self.max_capacity = 4
        self.room_hire_fee = 10

    def add_guest_to_room(self, guest):
        if len(self.guest_list) < 4:
            self.guest_list.append(guest)
        else:
            print(f"Room {self.room_number} is already full!")

    def remove_guest_from_room(self, guest):
        self.guest_list.remove(guest)
    
    def add_song_to_room(self, song):
        self.track_list.append(song)
    
    def remove_song_from_room(self, song):
        self.track_list.remove(song)

    def charge_guest(self, guest):
        guest.wallet -= self.room_hire_fee

    def display_songs_by_genre(self, input_genre):
        fetched_songs = []
        for song in self.track_list:
            if song.metadata["genre"] == input_genre:
                fetched_songs.append(song.metadata)
        return fetched_songs

    def display_songs(self, track_list):
        return self.track_list
