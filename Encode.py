from tkinter import *

window=Tk()
window.title("Encode")
window.geometry("400x500")

label_encode=Label(
    master=window,
    text="ENCODE",
    foreground="#f64c72",
    font=("arial",16,"bold")
)
label_encode.place(x=160, y=20)


window.mainloop()