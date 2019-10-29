import tkinter as tk
import numpy as np
import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog


class LoadImage:

    def LoadImage_openCV(self):
        filename = filedialog.askopenfilename(initialdir = "C:/Users/USER/Pictures",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        if(filename == ""):
            print("you have not choose your image , please choose again.")
        else:
            img = cv2.imread(filename)
            type(img)
            print("height:",img.shape[0])
            print("weight:",img.shape[1])
            print("dimension:",img.shape[2])
            return img





if __name__ == '__main__':
    window = tk.Tk()
    window.title('Image_Processing GUI')
    window.geometry('200x200')
    #  design your windows form below

    L0 = tk.Label(window, text = "1.Image Processing")
    L0.grid(row = 0,column = 0)

    btn0 = tk.Button(window, text = "1.1 Load Image", command = lambda:LoadImage().LoadImage_openCV())
    # you shouldn't have parameter in your command(origin set), if you have you need to use lambda
    btn0.grid(row = 1, column = 0)

    window.mainloop()


