from tkinter import *
from tkVideoPlayer import TkinterVideo
from tkinter.filedialog import askopenfile

videoplayer = None

def openFile():
    global videoplayer
    if videoplayer:
        videoplayer.destroy()
    file = askopenfile(mode='r', filetypes=[('Video Files', ['*.mp4', '*.avi', '*.flv', '*.mov' , '*.webm'])])
    if file is not NONE:
        global filename
        filename = file.name
        videoplayer = TkinterVideo(master= window, scaled=True, bg="#333333",)
        videoplayer.load(r"{}".format(filename))
        videoplayer.pack(expand=True, fill='both')
        videoplayer.play()

def playFile():
    videoplayer.play()

def pauseFile():
    videoplayer.pause()

def stopFile():
    if videoplayer:
        videoplayer.destroy()


window = Tk()
window.title("TKINTER VIDEO PLAYER")
window.iconbitmap("rickroll.ico")

window.geometry("1280x720")

window.config(bg= "#333333")

baslik = Label(window, text="VIDEO PLAYER PROJECT", font=("Times New Roman", 20), fg="white", bg="#333333")
baslik.configure(anchor=CENTER)
baslik.pack()

buttonFrame = Frame(window, bg="#333333")
buttonFrame.pack()

videoSelect = Button(buttonFrame, text="Select Video", font=("Times New Roman", 15), fg="white", bg="#333333", command=lambda: openFile())
videoSelect.pack(side=LEFT, padx= 10, pady=10)

videoPlay = Button(buttonFrame, text="Play Video", font=("Times New Roman", 15), fg="white", bg="#333333", command=lambda: playFile())
videoPlay.pack(side=LEFT, padx= 10, pady=10)

videoPause = Button(buttonFrame, text="Pause Video", font=("Times New Roman", 15), fg="white", bg="#333333", command=lambda: pauseFile())
videoPause.pack(side=LEFT, padx= 10, pady=10)

videoStop = Button(buttonFrame, text="Stop Video", font=("Times New Roman", 15), fg="white", bg="#333333", command=lambda: stopFile())
videoStop.pack(side=LEFT, padx= 10, pady=10)

window.mainloop()