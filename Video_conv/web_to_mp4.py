import moviepy.editor as moviepy
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import glob
files = glob.glob("C:/Users/sharath.narayanaswam/Downloads/01_Video_editor_scripts/01_Video_editor_scripts/new")
print([(n, f) for n, f in enumerate(files)])
filenumber = int(input("File number: "))
# clip = moviepy.VideoFileClip(r"C:\Users\sharath.narayanaswam\Desktop\03_SITIS_Data\2021-02-11_060009-vahana-sstci-cam1.webm")
# print(clip)
# clip.write_videofile("SITIS_Cam_1.mp4")
start = float(input("Start: "))
end = float(input("End: "))
ffmpeg_extract_subclip(files[filenumber], start, end, targetname="output_selected.mp4")