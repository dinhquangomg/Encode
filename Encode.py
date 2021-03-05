from tkinter import *

window=Tk()
window.title("Encode")
window.geometry("400x450")

label_encode=Label(
    master=window,
    text="ENCODE",
    foreground="#f64c72",
    font=("arial",24,"bold")
)
text_input=Text(
    master=window,
    height=8,
    width=40,
    background="#659dbd"
)

text_output=Text(
    master=window,
    height=8,
    width=40,
    background="#8ee4af"
)

button_encode=Button(
    window,
    text="Encode"
)

label_encode.pack(pady=10)
text_input.pack(pady=10)
button_encode.place(x=100,y=220)
text_output.pack(pady=50)

window.mainloop()