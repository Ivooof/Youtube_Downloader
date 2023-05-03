#CREATED BY IVOOF_

import pytube
import time
import sys

url = input("Enter the URL of the FULL YOUTUBE video TO DOWNLOAD:")
yt = pytube.YouTube(url)

def download():
    print(""".-MENU-. 
    1. HIGH definition video.
    2. LOW definition video.
    3. MP3 Audio. """)
    opt = input("Choose an option from the previous MENU:")

    if(opt=="1"):
        print("You chose the HIGH definition video option.")
        print("Downloading, please wait a moment...")
        toolbar_width = 40
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width + 1))
        for i in range(toolbar_width):
            time.sleep(0.1)
            sys.stdout.write("-")
            sys.stdout.flush()
        sys.stdout.write("]\n")
        videoHD = yt.streams.get_highest_resolution()
        videoHD.download(filename="Video high resolution download.mp4")
    elif(opt=="2"):
        print("You chose the LOW definition video option.")
        print("Downloading, please wait a moment...")
        toolbar_width = 40
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width + 1))
        for i in range(toolbar_width):
            time.sleep(0.1)
            sys.stdout.write("-")
            sys.stdout.flush()
        sys.stdout.write("]\n")
        videoLOW = yt.streams.get_lowest_resolution()
        videoLOW.download(filename="Low resolution video downloaded.mp4")
    elif(opt=="3"):
        print("You chose the MP3 Audio option.")
        print("Downloading, please wait a moment...")
        toolbar_width = 40
        sys.stdout.write("[%s]" % (" " * toolbar_width))
        sys.stdout.flush()
        sys.stdout.write("\b" * (toolbar_width + 1))
        for i in range(toolbar_width):
            time.sleep(0.1)
            sys.stdout.write("-")
            sys.stdout.flush()
        sys.stdout.write("]\n")
        audio = yt.streams.get_audio_only()
        audio.download(filename="Downloaded audio.mp3")
    else:
        print("WRONG OPTION.")

download()
print("DOWNLOAD COMPLETED CHECK THE DESTINATION FOLDER.")

#CREATED BY IVOOF_
