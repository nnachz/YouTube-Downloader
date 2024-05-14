from pytube import YouTube
import os

link = input("Link: ")
yt = YouTube(link)

video = yt.streams.get_highest_resolution()
video.download()
print("Download Succesful")