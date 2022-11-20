class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def check_favourite_song_in_room(self, track_list):
        for song in track_list:
            if self.favourite_song == song.metadata["track name"]:
                return "Woohoo!"

