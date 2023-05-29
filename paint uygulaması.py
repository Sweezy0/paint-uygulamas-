import tkinter as tk
from tkinter import colorchooser

def start_drawing(event):
    canvas.bind("<B1-Motion>",draw)
def stop_drawing(event):
    canvas.unbind("<B1-Motion>")
def draw(event):
    x,y=event.x,event.y
    canvas.create_oval(x-2,y-2,x+2,y+2,fill=current_color)
def clear_canvas():
    canvas.delete("all")
def select_color():
    color=colorchooser.askcolor()
    if color:
        global current_color
        current_color=color[1]
window=tk.Tk()
window.title("Basit Paint Uygulaması")
canvas=tk.Canvas(window,width=400,height=400)
canvas.pack()
canvas.bind("<ButtonPress-1>",start_drawing)
canvas.bind("<ButtonRelease-1>",stop_drawing)
clear_button=tk.Button(window,text="Temizle",command=clear_canvas)
clear_button.pack()
color_button=tk.Button(window,text="Temizle",command=select_color)
color_button.pack()
current_color="black"
window.mainloop()