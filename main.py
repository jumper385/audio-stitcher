from pydub.playback import play
from Snippet import Snippet
from Song import Song
from Ad import Ad
from Stitcher import Stitcher

def main():
    print("Hello world...")

    track1 = Snippet("snippets/ram.mp3")
    track2 = Snippet("snippets/ram2.mp3")

    ad1 = Ad("snippets/alpha.mp3")
    ad2 = Ad("snippets/ram4.mp3")

    song1 = Song("snippets/songs/song1.mp3")
    song2 = Song("snippets/songs/song2.mp3")

    print("Building song...")
    stitch = Stitcher(
        song_list = [song1, song2],
        snippet_list = [track1, track2],
        ad_list = [song1, song2]
    )

    out = stitch.assemble()

    out.export("build/build.mp3", format="mp3")

if __name__ == "__main__":
    main()
