from random import choice, randint
from captcha.image import ImageCaptcha
from tkinter import *
import string

root = Tk()
root.title("Captcha")
root.configure(background = "#a7d9c5")
root.geometry("680x680")

MainLabel = Label(root, text="Welcome to PYTHON CLASS", font=("Arial", 30), bg="#a7d9c5")
MainLabel.pack()

canvas = Canvas(root, width=500, height=500, bg = "#a7d9c5")
canvas.place(x = 100, y = 70)

RegLabel = Label(canvas, text = "Reg No", font = "Arial 10 bold", bg = "#a7d9c5")
PassLabel = Label(canvas, text = "Password", font = "Arial 10 bold", bg = "#a7d9c5")
RegLabel.place(x = 140, y = 10)
PassLabel.place(x = 140, y = 40)

RegEntry = Entry(canvas)
PassEntry = Entry(canvas)
RegEntry.place(x = 230, y = 10)
PassEntry.place(x = 230, y = 40)


# for create captcha
cap = ImageCaptcha(width=280, height=90)
ps = string.ascii_letters + string.digits
c_text = "".join(choice(ps) for w in range(randint(5, 6)))

cap.generate(c_text)
cap.write(c_text , "Pass.jpg")

# for show captcha
img = PhotoImage(file = "Pass.jpg")
canvas.create_image(120,70,anchor=NW, image=img)

# Enter Captcha text box
txtLabel = Label(canvas, text = "Enter Captcha", font = "Arial 10 bold", bg = "#a7d9c5")
txtLabel.place(x = 200, y = 200)
txt = Entry(canvas)
txt.grid(row = 3, column = 1)
canvas.create_window(250, 180, window=txt)

def change():
    global c_text
    c_text = "".join(choice(ps) for w in range(randint(4, 6)))

    cap.generate(c_text)
    cap.write(c_text, "Pass.jpg")
    img = PhotoImage(file="Pass.jpg")
    canvas.create_image(120,70,anchor=NW, image=img)
    canvas.mainloop()


# check captcha
def check():
    if txt.get() == c_text:
        lbl["text"] = "Login Successful!"
        lbl["foreground"] = "green"
    else:
        lbl["text"] = "Wrong Captcha!  Try Again."
        lbl["foreground"] = "red"
        change()
        txt.set("")

# for check captcha
checkBtn = Button(canvas, text="Check !", command=check)
checkBtn.place(x=165,y=220)

# for change captcha
changeBtn = Button(canvas, text="Change Captcha !", command=change)
changeBtn.place(x=225, y=220)

# for label
lbl = Label(canvas, font="irelham", bg = "#a7d9c5")
lbl.place(x=150, y=255)

root.mainloop()