#Mohamed Traore, Dec 2022
#This script will download a playlist
#Provide the playlist as argument, while calling the script

from pytube import Playlist, YouTube
from pytube.cli import on_progress
import os, sys

#link = "https://www.youtube.com/playlist?list=PLGaQya5sgY3mtmFcsVkd5BYq8j1Hl-QTE"
link = sys.argv[1]
SAVE_PATH = "D:/Users/Music/mp3/Playlist"

p = Playlist(link)
n_tot_video = len(p.video_urls)
n_success = 0
n_failure = 0

print(f'Downloading: {p.title}\n')
for i in range(n_tot_video):
    v = p.video_urls[i]
    try:
        yt = YouTube(v, on_progress_callback = on_progress)
    except VideoUnavailable:
        print(f'Video {v} is unavaialable, skipping.')
        n_failure = n_failure + 1
    else:
        print(yt.title + " downloading:")
        video = yt.streams.filter(only_audio=True).first()
       
        # download the file
        out_file = video.download(output_path=SAVE_PATH, skip_existing=True)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        isFile = os.path.isfile(new_file)
        
        while isFile :
                base, ext = os.path.splitext(new_file)
                base = base +  '#'
                new_file = base +  '.mp3'
                isFile = os.path.isfile(new_file)
        
        os.rename(out_file, new_file)

    # number of success
    n_success = n_success + 1
    print("\n")
print('SUMMARY:')
print('===============')
print('Total video: ' + str(n_tot_video))
print('Downloaded : ' + str(n_success))
print('Failure    : ' + str(n_failure))