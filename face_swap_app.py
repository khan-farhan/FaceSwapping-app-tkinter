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
        

def select_image2():
    # grab a reference to the image panels
    global panelB
    global panelD
    # open a file chooser dialog and allow the user to select an input
    # image
    path = filedialog.askopenfilename()

    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale, and detect
        # edges in it
        image = cv2.imread(path)
        image = cv2.resize(image,(200,200))
        img_np = image

        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # convert the images to PIL format...
        image = Image.fromarray(image)

        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)

        # if the panels are None, initialize them
        if panelB is None:
            # while the second panel will store the edge map
            panelB = Label(frame2, image=image)
            panelB.image = image
            panelB.pack(side="top", padx=10, pady=10)

        # otherwise, update the image panels
        else:
            # update the pannels
            panelB.configure(image=image)
            panelB.image = image

        logo = Image.open("logo.png")
        logo = logo.resize((100, 100), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)
        if panelD is None:
            # while the second panel will store the edge map
            panelD = Label(frame4, image=logo)
            panelD.image = logo
            panelD.pack(side="top", padx=10, pady=10)

        # otherwise, update the image panels
        else:
            # update the pannels
            panelD.configure(image=logo)
            panelD.image = logo

        show_Swap_image(Face1,img_np)

def show_Swap_image(face1, face2):
    global panelC

    faceswap.FaceSwap(face1,face2)
    Swaped_image = cv2.imread("output.jpg")
    Swaped_image = cv2.cvtColor(Swaped_image, cv2.COLOR_BGR2RGB)

        # convert the images to PIL format...
    Swaped_image = Image.fromarray(Swaped_image)

        # ...and then to ImageTk format
    Swaped_image = ImageTk.PhotoImage(Swaped_image)

    if panelC is None:
            # while the second panel will store the edge map
            panelC = Label(frame3, image=Swaped_image)
            panelC.image = Swaped_image
            panelC.pack(side="top", padx=10, pady=10)
    else:
            panelC.configure(image=Swaped_image)
            panelC.image = Swaped_image

    Go_back()

def Go_back():
    global Go_back_botton
    Go_back_botton = Button(root, command=clear_widgets,text = "Back", padx=10, pady=10)
    Go_back_botton.pack()

def clear_widgets():
    global panelA, panelB, panelC, Go_back_botton
    panelA.configure(image=None)
    panelA.image = None

    panelB.configure(image=None)
    panelB.image = None

    panelC.configure(image=None)
    panelC.image = None

    Go_back_botton.forget()



root = Tk()
root.title("Face Swap")
root.geometry("800x800")
panelA = None
panelB = None
panelC = None
panelD = None
Face1 = None
Go_back_botton = None

frame1 = Frame(root,bg = "black")
frame1.place(x = 100,y = 100)


frame2 = Frame(root,bg = "black")
frame2.place(x = 500,y = 100)


frame3 = Frame(root,bg = "black")
frame3.place(x = 300,y = 500)

frame4 = Frame(root)
frame4.place(x = 350,y = 150)

btn1 = Button(root, text="Select first face", command=select_image1, padx="10", pady="10",bg = "black")
# btn1.config(image = ImageTk.PhotoImage(Image.open("back.jpg")),width="10",height="10")
btn1.place(x = 125, y = 350, height = 50, width = 150)

btn2 = Button(root, text="Select second face", command=select_image2, padx="10", pady="10",bg = "black")
btn2.place(x = 525, y = 350, height = 50, width = 150)

root.mainloop()