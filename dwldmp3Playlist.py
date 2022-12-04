from pytube import Playlist, YouTube
from pytube.cli import on_progress
import os, sys

link = "https://www.youtube.com/playlist?list=PLGaQya5sgY3mtmFcsVkd5BYq8j1Hl-QTE"
SAVE_PATH = "D:/Users/medtr/VSCode/pytube project/mp3/Salif Keita"

def progress_function(chunk, file_handle, bytes_remaining):
    filesize = chunk.filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()


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
        
        while True :
            if isFile :
                base, ext = os.path.splitext(new_file)
                base = base +  '#'
                new_file = base +  '.mp3'
                isFile = os.path.isfile(new_file)
            else: 
                 break

        os.rename(out_file, new_file)

    # number of success
    n_success = n_success + 1
    print("\n")
print('SUMMARY:')
print('===============')
print('Total video: ' + str(n_tot_video))
print('Downloaded : ' + str(n_success))
print('Failure    : ' + str(n_failure))