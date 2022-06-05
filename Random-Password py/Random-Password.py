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
button.config(font=('Password',50,'bold'))
button.config(bg='#FF6600')
button.config(activebackground='#120A8F')
button.config(activeforeground='#704214')
button.config(width=10)
button.pack()


label = tk.Label(root, text='👆Click the button to generate passwords ')
label.config(border=10)
label.config(font=(password,19,'bold'))
label.pack()

#Description in program

description = tk.Label(root, text='Your password is already copied and ready to paste')
description.config(font=(50))
description.config(bg='#FF0000')
description.config(border=10)
description.pack()


root.mainloop()
