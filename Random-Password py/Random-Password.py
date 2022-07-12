##!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import tkinter as tk
import  random
import pyperclip as py
from pymsgbox import password



def main():
    a = 'BVDHGVSACEHWUFGATGVFDCXHDBSADU'
    s = 'jvhbfvayfvcbjadsnfhvyvgacadnsburgfy'
    d = '2411752410230471206544504101457450'
    f = '!"£$%&/()=?^)(/&$"§°çé*_:;'

    all = a + s + d + f

    lengh = 20

    password = '' .join(random.sample(all, lengh))

    py.copy(password)

    label.config(text=password)
    button.config(command=main)

#start with a random password  program
root = tk.Tk()
# setting window icon
root.iconphoto(False, tk.PhotoImage(file ='icon.png'))
root.title('Password random')



button = tk.Button(root, text='Password', command=main)
button.configure(font=('Password',50,'bold'))
button.configure(bg='#FF6600')
button.configure(activebackground='#120A8F')
button.configure(activeforeground='#704214')
button.configure(width=10)
button.pack()


label = tk.Label(root, text='👆Click the button to generate passwords ')
label.configure(border=10)
label.configure(font=(password,19,'bold'))
label.pack()

#Description in program

description = tk.Label(root, text='Your password is already copied and ready to paste')
description.configure(font=(50))
description.configure(bg='#FF0000')
description.cconfigure(border=10)
description.pack()


root.mainloop()
