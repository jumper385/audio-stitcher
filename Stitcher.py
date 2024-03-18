import random
from pydub import AudioSegment

class Stitcher():
    def __init__(self, song_list, snippet_list, ad_list):
        self.song_list = song_list
        self.snippet_list = snippet_list
        self.ad_list = ad_list

    def assemble(self):

        inserts = [*self.snippet_list, *self.ad_list][:len(self.song_list)]

        assembly = AudioSegment.silent(duration=100)

        for song, insert in zip(self.song_list, inserts):
            print(song.filepath)
            print(insert.filepath)
            assembly += insert.audio() + song.audio()

        return assembly
