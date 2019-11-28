# TODO 01: Make suitable changes in borders of the widgets.
# TODO 02: Didn't add text referring the feature of the button, you might want to do it.
# TODO 03: Change image laying in middle of the two buttons with actual piece of code from .grid() method.
# TODO 05: Buy Cyberpunk 2077

import tkinter
from tkinter import *
from tkinter import filedialog


def select_photo():
    image = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                       filetypes=(("jpg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
    # TODO: add necessary image file extensions. We might have to make two different functions for each button.


window = tkinter.Tk()
window.title("AB MAIN GAN CHODEGA")
window.geometry('850x400')
window.configure(background='#333333')
window.resizable(False, False)  # We cant maximize the window


main_frame = LabelFrame(window, padx=5, pady=5)
main_frame.pack(padx=15, pady=15)
# we can use only one of .pack() / .grid() / .place() methods in a single window/frame.
# Hence created two frames to use two different methods.
not_main_frame = LabelFrame(window, padx=5, pady=5, border=0)
not_main_frame.pack(padx=10, pady=15)


title = Label(main_frame, text='IMAGE GENERATION AND SUPER-RESOLUTION USING GAN', highlightthickness=0, anchor=CENTER,
              bg='#333333', fg='#ffffff')
title.grid(row=0, column=2)


converter = PhotoImage(file="translate.png")
resolute = PhotoImage(file='wow.png')
hack = PhotoImage(file='hack.png')

converter_button = Button(not_main_frame, image=converter, border=0, command=lambda: select_photo())
converter_button.grid(row=2, column=2)

hackerman = Label(not_main_frame, image=hack)
hackerman.grid(row=2, column=3)

resolute_button = Button(not_main_frame, image=resolute, border=0, command=lambda: select_photo())
resolute_button.grid(row=2, column=4)


window.mainloop()
