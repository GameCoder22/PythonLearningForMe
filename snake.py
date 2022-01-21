import tkinter

window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500, height=500)

my_label = tkinter.Label(text="I am a label", font="ComicSans")
my_label.pack()

my_label.pack(side="bottom")


def bc():
    print("I got clicked.")
    nt = inp.get()
    my_label.config(text=nt)


button = tkinter.Button(text="Click Me!", command=bc)
button.pack()



inp = tkinter.Entry()
inp.pack()



















window.mainloop()
