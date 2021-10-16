from pytube import YouTube
from pytube import Search
import vlc
import time
import os
import string

while True:
    search_enc = Search(str(input("Name of song: ")))
    search_dec = search_enc.results
    VideoId="".join(str(search_dec[0]))
    UrlId = VideoId[41:-1]
    YouTubeUrlTemplate = "https://www.youtube.com/watch?v="
    CompleteUrl = YouTubeUrlTemplate + UrlId
    myVideo = YouTube (CompleteUrl)

    len = int(myVideo.length)
    len_min = len // 60
    len_sec = len % 60
    print("\nNow playing: " + myVideo.title + "|" + str(len_min) + ":"+ str(len_sec) +  "|")

    VideoList = myVideo.streams.filter(only_audio=True)
    Path = VideoList[0].download()

    base, exit = os.path.splitext(Path)
    base = base.replace(" ","")
    NewPath = base + '.mp3'
    os.rename(Path, NewPath)
    ShortName = NewPath[40:]

    p = vlc.MediaPlayer(ShortName, ":no-video")
    p.play()
    time.sleep(len+10)
    p.stop

    os.remove(ShortName)
