import tkinter as tk
from tkinter import messagebox
import pyttsx3
root=tk.Tk()
root.geometry('500x400')
root.title("Text to speach")
def play_text():
    text=entry.get()
    if text.strip():
        engine=pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("Error")
def exit_program():
    root.destroy()
def clear_text():
    entry.delete(0,tk.END)

mylabel=tk.Label(root,text="Text to speach",font="Tahoma 30 bold")
mylabel.pack(pady=30)
label=tk.Label(root,text="Enter your text",font="Helvatica 10 bold")
label.pack(pady=10)
entry=tk.Entry(root,width=50)
entry.pack(pady=5)
button_play=tk.Button(root,text="play",fg="black",bg="yellow",font="Helvatica 10 bold",padx=10,pady=3,command=play_text)
button_play.pack(pady=5)
button_play.place(x=100,y=230)
button_exit=tk.Button(root,text="Exit",fg="red",bg="black",font="Helvatica 10 bold",padx=10,pady=3,command=exit_program)
button_exit.pack(pady=5)
button_exit.place(x=200,y=230)
button_set=tk.Button(root,text="Set",fg="blue",bg="black",font="Helvatica 10 bold",padx=10,pady=3,command=clear_text)
button_exit.pack(pady=5)
button_exit.place(x=300,y=230)
root.mainloop()