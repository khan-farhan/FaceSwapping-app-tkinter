from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2, time, threading, dlib, os
from threading import Thread
import numpy as np
import faceswap

def select_image1():
    # grab a reference to the image panels
    global panelA
    global Face1

    # open a file chooser dialog and allow the user to select an input
    # image
    path = filedialog.askopenfilename()

    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale, and detect
        # edges in it
        image = cv2.imread(path)
        image = cv2.resize(image,(200,200))
        Face1 = image

        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # convert the images to PIL format...
        image = Image.fromarray(image)

        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)

        # if the panels are None, initialize them
        if panelA is None:
            # while the second panel will store the edge map
            panelA = Label(frame1, image=image)
            panelA.image = image
            panelA.pack(side="top", padx=10, pady=10)

        # otherwise, update the image panels
        else:
            # update the pannels
            panelA.configure(image=image)
            panelA.image = image
    

root = Tk()
# 画像を開く
frame = Frame(root)
frame.pack()
btn2 = Button(frame, padx=16, bd=8, text="AIRCARD A-1 ON LINE", bg="green", fg="black", command=select_image1)
# btn2.place(x = 525, y = 350, height = 200, width = 200)
btn2.pack()
# tkinter.PhotoImage ではなく ImageTk.PhotoImage() を使う

# Button(root, image = photo).pack()
root.mainloop()