from pydub import AudioSegment

class Snippet():
    def __init__(self, filepath, fade_in_sec = None, fade_out_sec = None):
        self.filepath = filepath
        self.wav = AudioSegment.from_file(self.filepath)
        self.fade_in_sec = fade_in_sec
        self.fade_out_sec = fade_out_sec

    def audio(self):
        audio_out = self.wav

        if (self.fade_in_sec):
            audio_out.fade_in(duration = self.fade_in_sec)
        if (self.fade_out_sec):
            audio_out.fade_out(duration = self.fade_out_sec)

        return audio_out
