from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from webbrowser import open_new


main_window = Tk()
main_window.geometry('600x600') 
main_window.title('Text Editor')

def git():
    open_new(r"https://github.com/ardavan8102")

heading = Button(main_window, text = 'My Github', font = ('bold',18), bg = 'light blue', command = git)
heading.pack()

scrollbar = Scrollbar(main_window)

scrollbar.pack(side = RIGHT,fill = Y)  

Editor=Text(main_window, width = 400,height = 450,yscrollcommand = scrollbar.set)
Editor.pack(fill=BOTH)

def save():
    filepath = asksaveasfilename(defaultextension = "txt", filetypes = [("Save As Text", "*.txt")])
    
    if not filepath:
        return
      
    with open(filepath, "w") as f:
        text = Editor.get(1.0, tk.END)
        f.write(text)
        
    main_window.title(f"Saved AS - {filepath}")


button = Button(main_window , text= ' Save Text ', command = save, font = ('bold',12), bg='light green')
button.place(x = 250,y = 520)

main_window.mainloop()