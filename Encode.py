from tkinter import *

window=Tk()
window.iconbitmap("icon.ico")
window.title("Encode")
window.geometry("400x450")

#method of handling event
def encode():
    data=text_input.get(0.0,END)
    char=[]
    for x in range(len(data)):
        if data[x]==" ":
            char.append(" ")
            continue
        if x%2==0:
            char.append(chr(ord(data[x])+21))
        else:
            char.append(chr(ord(data[x])-8))
    char.pop()
    text_output.delete(0.0,END)
    text_output.insert(0.0,str("".join(char)))

def decryption():
    data=text_input.get(0.0,END)
    char=[]
    for x in range(len(data)):
        if data[x]==" ":
            char.append(" ")
            continue
        if x%2==0:
            char.append(chr(ord(data[x])-21))
        else:
            char.append(chr(ord(data[x])+8))
    char.pop()
    text_output.delete(0.0,END)
    text_output.insert(0.0,str("".join(char)))


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
    text="Encode",
    command=encode,
    width=len("Decryption")
)
button_decryption=Button(
    master=window,
    text="Decryption",
    command=decryption
)

label_encode.pack(pady=10)
text_input.pack(pady=10)
button_encode.place(x=100,y=220)
button_decryption.place(x=220,y=220)
text_output.pack(pady=50)

window.mainloop()