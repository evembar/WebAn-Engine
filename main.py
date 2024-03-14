from pygame import mixer
from tkinter import PhotoImage
from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel
from random import randint
from threading import Thread
import sys

def runner():
    from script import game
    return 0

def run_weban():
    play_button.configure(hover=False, fg_color = 'white')
    stop_button.configure(hover=True, fg_color='black')
    mixer.music.pause()
    runner()

def stop_weban():

    sys.exit()

des = CTk()
des.title('WebAn Engine Menu')
des.geometry('350x400+500+250')
des.resizable(False, False)

mixer.init()
randint_mus = randint(1,2)
if randint_mus == 1:
	mixer.music.load('music/explorers.mp3')
	music_autor = "    Hinkik - Explorers(chiptune remix)"
if randint_mus == 2:
	mixer.music.load('music/embers.mp3')
	music_autor = "Dex Arson - Embers(no with mettal remix)"
mixer.music.play(-1)
weban_image = PhotoImage(file='weban.png', width=340, height=225)

image_frame = CTkFrame(des, width=340, height=225)
image_frame.place(x=5, y=5)
weban_label = CTkLabel(image_frame, image=weban_image, text='', width=340, height=225)
weban_label.place(x=0, y=0)
des.update()

menu_label = CTkLabel(des, text="WebAn Engine Menu", font=('Colibri', 20))
menu_label.place(x=70, y= 235)

music_text = CTkLabel(des, text = music_autor, font=('Colibri', 15))
music_text.place(x = 20, y = 270)

play_button = CTkButton(des, text = "Play", fg_color= "black", hover_color="white", border_color="white", command=run_weban)
play_button.place(x=30, y = 300)

stop_button = CTkButton(des, text = "Exit", fg_color= "black", hover_color="white", border_color="white", command=stop_weban)
stop_button.place(x=178, y = 300)



des.mainloop()

