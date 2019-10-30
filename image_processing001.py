import tkinter as tk
import numpy as np
import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog
from PIL import Image, ImageTk

img = []
image_for_colorconversion = []

class LoadImage:
    def __init__(self):
        self.img_load = []

    def LoadImage_openCV(self):
        self.filename = filedialog.askopenfilename(initialdir="C:/Users/USER/Pictures",title="Select file",filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
        if(self.filename == ""):
            print("you have not choose your image , please choose again.")
        else:
            # method 1 , in this case a reference to the image to global scope is required.
            # due to the way that python deals with garbage disposal
            # it will throw your image to garbage after you open it

            self.img_load = cv2.imread(self.filename)
            # global img 
            # img = self.img
            self.window = tk.Toplevel(root)
            self.photo = ImageTk.PhotoImage(file=self.filename)
            self.L0_Pic01 = tk.Label(self.window, image=self.photo)
            self.L0_Pic01.pack()

            # method 2, just use the method below you can get image
            # cv2.imshow(self.filename , self.img)
            # cv2.waitKey()
            height, width, dimension = self.img_load.shape
            print("height:",height)
            print("width:",width)
            print("dimension:",dimension)

class ColorConversion:
    def ColorConversion_openCV(self,image_for_colorconversion):
        self.img_colorconversion = []
        self.img_colorconversion = cv2.cvtColor(image_for_colorconversion, cv2.COLOR_BGR2RGB)
        cv2.imshow(self.img_colorconversion)
        cv2.waitKey()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Image_Processing GUI')
    root.geometry('200x200')
    #  design your windows form below

    L0 = tk.Label(root, text = "1.Image Processing")
    L0.grid(row = 0,column = 0)

    btn0_loadImage = tk.Button(root, text = "1.1 Load Image", command = lambda:LoadImage().LoadImage_openCV())
    # you shouldn't have parameter in your command(origin set), if you have you need to use lambda
    btn0_loadImage.grid(row=1, column=0)

    btn1_colorConversion = tk.Button(root, text="1.2 Color Conversion", command=lambda:ColorConversion().ColorConversion_openCV(img))
    # you shouldn't have parameter in your command(origin set), if you have you need to use lambda
    btn1_colorConversion.grid(row=2, column=0)

    root.mainloop()
