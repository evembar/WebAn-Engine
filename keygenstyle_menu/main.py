from pygame import mixer
from tkinter import PhotoImage
from customtkinter import CTk, CTkButton, CTkFrame, CTkLabel

def runner():
    from script import game
    return 0

def stop_weban():
    play_button.configure(hover=True, fg_color = 'black')
    stop_button.configure(hover=False, fg_color = 'white')
    mixer.music.unpause()

def run_weban():
    play_button.configure(hover=False, fg_color = 'white')
    stop_button.configure(hover=True, fg_color='black')
    mixer.music.pause()
    runner()

des = CTk()
des.title('WebAn Engine Menu')
des.geometry('350x400+500+250')
des.resizable(False, False)

mixer.init()
mixer.music.load('music/explorers.wav')
mixer.music.play(-1)
weban_image = PhotoImage(file='weban.png', width=340, height=225)

image_frame = CTkFrame(des, width=340, height=225)
image_frame.place(x=5, y=5)
weban_label = CTkLabel(image_frame, image=weban_image, text='', width=340, height=225)
weban_label.place(x=0, y=0)
des.update()

menu_label = CTkLabel(des, text="WebAn Engine Menu", font=('Ubuntu-Light', 20))
menu_label.place(x=70, y= 235)

play_button = CTkButton(des, text = "Play", fg_color= "black", hover_color="grey", border_color="white", command=run_weban)
play_button.place(x=30, y = 300)

stop_button = CTkButton(des, text = "Stop", fg_color= "white", hover_color="white", border_color="white", hover=False, command=stop_weban)
stop_button.place(x=178, y = 300)



des.mainloop()

