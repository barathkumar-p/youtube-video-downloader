from tkinter import *
from pytube import YouTube
bk = Tk()
bk.geometry('800x500')
bk.resizable(0,0)
bk.title("youtube video downloader")
Label(bk,text = 'YOUTUBE VIDEO DOWNLOADER', font ='arial 30 bold' ,fg= 'blue').pack()
link = StringVar()

Label(bk, text = 'Paste Youtube Link Here:', font = 'arial 25 bold').place(x= 220 , y = 100)
Label(bk, text = 'Done by BK!', font = 'arial 15 italic').place(x= 600 , y = 450)
link_enter = Entry(bk,width = 90,textvariable = link).place(x = 120, y = 250)
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(bk, text = 'DOWNLOADED', font = 'arial 15',bg = 'blue', padx = 2).place(x= 300 , y = 300)  

Button(bk,text = 'DOWNLOAD', font = 'arial 20 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=300 ,y = 350)

bk.mainloop()

