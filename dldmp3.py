from pytube import YouTube
from pytube.cli import on_progress
import os, sys, re

#This function will take an argument that is a link of youtube link to download
def yt_dld(link):
    link = str(link)
    SAVE_PATH = "D:/Users/medtr/Music/mp3"

    yt = YouTube(link, on_progress_callback=on_progress)

    print(yt.title + " downloading...\n")
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=SAVE_PATH)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    isFile = os.path.isfile(new_file)
    #Making sure file's name is unique

    while isFile :
        #base, ext = os.path.splitext(new_file)
        base = base +  '#'
        new_file = base +  '.mp3'
        isFile = os.path.isfile(new_file)

    os.rename(out_file, new_file)


n_link = len(sys.argv)
if n_link > 1:
    # Going through all the links provided as argument
    for i in range(1, n_link):
    # Check if it's a valid yt link
        youtube_regex = r"^(http(s)?://)?((w){3}.)?youtu(be|.be)?(\.com)?/.+"
        youtube_link = sys.argv[i]
        if re.match(youtube_regex, youtube_link):
            yt_dld(youtube_link)
        else:
            print("Invalid YouTube link: " + youtube_link)
else:
    print("Please provide a link as argument to the script")