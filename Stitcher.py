import random
from pydub import AudioSegment
from Snippet import Snippet
from Song import Song

class Joiner(Snippet):
    def __init__(self):
        self.timeline = []
        self.wav = AudioSegment.silent(duration=0)

    def add_clip(self, snippet):
        self.timeline.append(snippet)

    def audio(self):
        for snippet in self.timeline:
            self.wav += snippet.audio()

        return self.wav

    def debug(self, debug_filename = None, debug_dir = "build/debug"):
        filename = ""
        if debug_filename == None:
            filename = generate_random_string(6)
        else:
            filename = debug_filename

        out = self.audio()
        out.export(f"{debug_dir}/{filename}.mp3", format="mp3")

class GlobalTimeline(Joiner):
    def __init__(self, song_list, snippet_list, ad_list):
        self.song_list = song_list
        self.snippet_list = snippet_list
        self.ad_list = ad_list
        super().__init__()

    def assemble(self):
        song_count = len(self.song_list)
        inserts = [*self.snippet_list, *self.ad_list]
        random.shuffle(inserts)
        for insert, song in zip(inserts[:song_count], self.song_list):
            self.timeline.append(insert)
            self.timeline.append(song)

class Splicer(Song):
    def __init__(self, filepath):
        super().__init__(
                filepath = filepath)
        self.snippet_time_pairs = None

    def splice_in_at_time(self, snippet_filepath, splice_time_sec):
        if (not self.snippet_time_pairs):
            self.snippet_time_pairs = [(splice_time_sec, snippet_filepath)]
        else:
            self.snippet_time_pairs.append((splice_time_sec, snippet_filepath))

    def audio(self):

        if (self.snippet_time_pairs != None):
            reversed_snippets = sorted(self.snippet_time_pairs, key=lambda x: x[0], reverse=True)
            for time_sec, path in reversed_snippets:
                snippet = Snippet(path)
                orig_head = self.wav[:time_sec*1000]
                orig_tail = self.wav[time_sec*1000:]
                self.wav = orig_head.fade_out(30) + snippet.audio() + orig_tail.fade_in(30)
            return self.wav
        else:
            return self.wav
