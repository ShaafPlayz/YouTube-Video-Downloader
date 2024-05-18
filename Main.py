import tkinter
import customtkinter
from pytube import YouTube

def download_now():
    try:
        ytlink = url.get()
        videoLINK = YouTube(ytlink)
        video = videoLINK.streams.get_highest_resolution()

        info.configure(text=videoLINK.title)

        video.download()
        error.configure(text="Download Complete")
    except:
        error.configure(text="Download Error", text_color="orange")
        info.configure(text="Insert Your YouTube Link")


def report_prog(stream, chunk, rem_bytes):
    total = stream.filesize
    progress = total - rem_bytes
    percentage = (progress * 100) / total
    print(percentage)



customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.geometry("800x500")
window.title("YouTube Downloader (testing)")

info = customtkinter.CTkLabel(window, text="Insert Your YouTube Link")
info.pack()

url = customtkinter.StringVar()
field = customtkinter.CTkEntry(window, width=200, height=10, textvariable= url)
field.pack()

bar = customtkinter.CTkProgressBar(window, orientation="horizontal", width=200)
bar.set(0)
bar.pack(padx=5, pady=5)

error = customtkinter.CTkLabel(window, text="")
error.pack()

download_button = customtkinter.CTkButton(window, text="Begin Download", command=download_now)
download_button.pack()



window.mainloop()