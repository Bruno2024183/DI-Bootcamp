class Song:
    def _init_(self, lyrics):
        self.lyrics = lyrics

def sing_me_a_song(self):
    for line in self.lyrics:
        print(line)

stairway = Song([
    "There's a lady who's sure",
    "all that glitters is gold",
    "and she's buying a stairwat to heaven"
])

stairway.sing_me_a_song()



