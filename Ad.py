from Snippet import Snippet

class Ad(Snippet):
    def __init__(self, filepath, fade_in_sec = None, fade_out_sec = None):
        super().__init__(filepath, fade_in_sec, fade_out_sec)
