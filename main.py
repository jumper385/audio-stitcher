from pydub.playback import play
from Snippet import Snippet
from Song import Song
from Ad import Ad
from Stitcher import Stitcher, SplicedSong

def main():
    print("Hello world...")

    track1 = Snippet("snippets/ram.mp3")
    track2 = Snippet("snippets/ram2.mp3")

    ad1 = Ad("snippets/alpha.mp3")
    ad2 = Ad("snippets/ram4.mp3")

    song1 = SplicedSong("snippets/songs/wii.mp3")
    song1.splice_in_at_time("snippets/alpha.mp3", 10)
    song1.splice_in_at_time("snippets/keep_running.mp4", 20)

    # song2 = Song("snippets/songs/confused.mp3")
    # song3 = Song("snippets/songs/scheming.mp3")
    # song4 = Song("snippets/songs/song2.mp3")

    print("Building song...")
    stitch = Stitcher(
        song_list = [song1],
        snippet_list = [track1, track2],
        ad_list = [ad1, ad2]
    )

    out = stitch.assemble()

    # out.export("build/build.mp3", format="mp3")
    play(out)

if __name__ == "__main__":
    main()
