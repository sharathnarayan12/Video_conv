from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import glob

# Get the second you do not want in the movie
files = glob.glob("*.mp4")
print([(n, f) for n, f in enumerate(files)])
filenumber = int(input("File number: "))
start = int(input("Start: "))
end = int(input("End: "))
ffmpeg_extract_subclip(
    files[filenumber], start, end, targetname="output_selected.mp4")