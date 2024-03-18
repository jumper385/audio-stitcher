import random
from pydub import AudioSegment
from Snippet import Snippet
from Song import Song

class Stitcher():
    def __init__(self, song_list, snippet_list, ad_list):
        self.song_list = song_list
        self.snippet_list = snippet_list
        self.ad_list = ad_list
        self.inserts = [*snippet_list, *ad_list]

    def assemble(self):
        random.shuffle(self.inserts)

        assembly = AudioSegment.silent(duration=0)

        for song, insert in zip(self.song_list, self.inserts[:len(self.song_list)]):
            assembly += insert.audio() + song.audio()

        return assembly

class SplicedSong(Song):
    def __init__(self, filepath, fade_in_sec=None, fade_out_sec=None):
        super().__init__(filepath, fade_in_sec, fade_out_sec)
        self.snippet_time_pairs = None

    def splice_in_at_time(self, snippet_filepath, splice_time_sec):
        if (not self.snippet_time_pairs):
            self.snippet_time_pairs = [(splice_time_sec, snippet_filepath)]
        else:
            self.snippet_time_pairs.append((splice_time_sec, snippet_filepath))

    def audio(self):
        orig = self.wav
        reversed_snippets = sorted(self.snippet_time_pairs, key=lambda x: x[0], reverse=True)
        out = orig
        for time_sec, path in reversed_snippets:
            snippet = Snippet(path)
            orig_head = out[:time_sec*1000]
            orig_tail = out[time_sec*1000:]
            out = orig_head.fade_out(30) + snippet.audio() + orig_tail.fade_in(30)

        return out
