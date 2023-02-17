"""YouTUBE Video Downloader"""


# run command on terminal: $ pip install pytube
import pytube

link = input('Enter Youtube Video Url')

yt = pytube.YouTube(link)
yt.streams.first().download()
print('downloaded successfully ', link)
