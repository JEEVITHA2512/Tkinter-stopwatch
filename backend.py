from flask import Flask
from tkinter import *
app = Flask(__name__)

@app.route("/")
def hello():

    root = Tk()

    out = Label(root, text="0", bg="purple")

    def out_result():
        out.configure(text="button pressed")

    button1 = Checkbutton(root, command=out_result)

    button1.place(x=20, y=20)
    out.place(x=50, y=20)

    root.mainloop()

    if__name__= "__main__"
    app.run()