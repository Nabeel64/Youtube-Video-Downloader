from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil
from tkinter import messagebox
import re

def download():
    video_url=url_entry.get()
    pattern=(r'(https?://)?(www\.)?''(youtube|youtu|youtube-nocookie)\.(com|be)/''(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    if re.match(pattern,video_url):
        download_path=path_label.cget("text")
        if download_path=='Select path to download':
            messagebox.showwarning('Youtube Video Downloader','Please select path')
        else:
            try:
                mp4=YouTube(video_url).streams.get_highest_resolution().download()
                video_clip=VideoFileClip(mp4)
                video_clip.close()
                shutil.move(mp4,download_path)
                messagebox.showinfo('Youtube Video Downloader','Download Complete')
            except Exception as e:
                messagebox.showerror('Youtube Video Downloader',e)
    else:
        messagebox.showerror('Youtube Video Downloader','Invalid Youtube URL')

def get_path():
    path=filedialog.askdirectory()
    path_label.config(text=path)

root=Tk()
root.title('Youtube Video Downloader')
root.resizable(False,False)
canvas=Canvas(root,width=400,height=300)
canvas.pack()

app_label=Label(root,text='Youtube Video Downloader',fg='black',font=('Arial',20))
canvas.create_window(200,20,window=app_label)

url_label=Label(root,text='Enter video URL')
url_entry=Entry(root)
canvas.create_window(200,80,window=url_label)
canvas.create_window(200,100,window=url_entry)

path_label=Label(root,text='Select path to download')
path_btn=Button(root,text='Select',command=get_path)
canvas.create_window(200,150,window=path_label)
canvas.create_window(200,180,window=path_btn)

download_btn=Button(root,text='Download',command=download)
canvas.create_window(200,250,window=download_btn)

root.mainloop()