from pydub.playback import play
from Snippet import Snippet
from Song import Song
from Ad import Ad
from Stitcher import Joiner, GlobalTimeline, Splicer

def main():
    print("Hello world...")

    track1 = Snippet("snippets/ram1.mp3")
    track2 = Snippet("snippets/ram2.mp3")

    ad1 = Ad("snippets/alpha.mp3")
    ad2 = Ad("snippets/ram4.mp3")

    song1 = Splicer("snippets/songs/wii.mp3")
    song1.splice_in_at_time("snippets/alpha.mp3", 10)
    song1.splice_in_at_time("snippets/keep_running.mp4", 20)
    song1.debug(f"song_spliced")

    song2 = Splicer("snippets/songs/confused.mp3")
    song2.splice_in_at_time("snippets/ram2.mp3", 3)
    block2 = Joiner()
    block2.add_clip(song2)
    block2.add_clip(ad1)
    block2.debug("test")

    song3 = Splicer("snippets/songs/scheming.mp3")

    print("Building song...")
    stitch = GlobalTimeline(
        song_list = [song1, block2, song3],
        snippet_list = [track1, track2],
        ad_list = [ad1, ad2]
    )

    stitch.assemble()
    out = stitch.audio()

    print(f"Exporting {int(len(out)/1000/60)} minute mixtape...")
    out.export("build/build.mp3", format="mp3")
    play(out)

if __name__ == "__main__":
    main()
