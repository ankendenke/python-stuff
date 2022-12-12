#Mohamed Traore, Dec 2022
#This program is a command line Youtube MP3 downloader
#It downloads individual links or a bunch of link in a file ending with .txt, as argument
#Call the script with either a valide Youtube link or a text file as argument
#TODO: 
#     - ask the user for the destination directory
#     - check if the computer is connected to the internet
#     - create a GUI version?

# Import needed libraries
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
        base = base +  '#'
        new_file = base +  '.mp3'
        isFile = os.path.isfile(new_file)

    os.rename(out_file, new_file)
    print("\n")


#This function takes a number of links passed as argument and download all of them
def yt_dl_links(n_links):
    # Going through all the links provided as argument
    for i in range(1, n_links):
    # Check if it's a valid yt link
        youtube_regex = r"^(http(s)?://)?((w){3}.)?youtu(be|.be)?(\.com)?/.+"
        youtube_link = sys.argv[i]
        if re.match(youtube_regex, youtube_link):
            yt_dld(youtube_link)
        else:
            print("Invalid YouTube link: " + youtube_link)


#This function takes a file ending with .txt contening lines with youtoube links

def yt_dl_file(fl):
    
    if fl.endswith(".txt"):
        # Open the file and read each line
        with open(fl, "r") as file:
            # Check if each line is a YouTube link
            youtube_regex = r"^(http(s)?://)?((w){3}.)?youtu(be|.be)?(\.com)?/.+"
            for line in file:
                if re.match(youtube_regex, line):
                    yt_dld(line)
                else:
                    print("Invalid YouTube link")
    else:
        print("Invalid file type. Please provide a .txt file")


# Check if the command-line argument is a .txt file
n_args = len(sys.argv)
if n_args > 1:
    # let's see if it's a file first
    isFile = os.path.isfile(sys.argv[1])
    if isFile:
        # Calling the function to download links from a text file
        file_path = sys.argv[1]
        yt_dl_file(file_path)
    else:
        # Calling the function to download individuals links
        yt_dl_links(n_args)
else:
    print("Please provide an argument...")