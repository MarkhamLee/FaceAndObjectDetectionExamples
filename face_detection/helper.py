import matplotlib as plt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
from PIL import Image, ImageDraw
from ipywidgets import Button
from tkinter import Tk, filedialog
from IPython.display import clear_output, display


class Helper: 

    # this method is for displaying images for comparison 
    # it also does the post display tinting for match or not match
    # inputs are file path + a 0 non matched photos, 1 for matched 
    # photos and any  other integer for phots that don't require tinting 
    def display_compared_images(self, reference, sample, tint):

        self.reference = reference
        self.sample = sample 
        self.tint = tint

        # open reference image
        self.reference = Image.open(self.reference).convert("RGB")

        # add tinting (if needed)

        # red tint if the photo doesn't match 
        if self.tint == 0:
            img = Image.open(self.sample).convert("RGB")
            tint = Image.new("RGB", (img.size), color=(255,155,15))
            self.sample = Image.blend(img, tint, 0.5)
            title = "DOESN'T MATCH!"

        # green tint if the photos match 
        elif self.tint == 1:
            img = Image.open(self.sample).convert("RGB")
            tint = Image.new("RGB", (img.size), color=(55,255,11))
            self.sample = Image.blend(img, tint, 0.5)
            title = "SUCCESS! MATCH!"

        # no match if we're just displaying the photos
        else:
            self.sample = Image.open(self.sample).convert("RGB")
            title = "Sample Photo"


        # use matplot library to display the images 
        figure = plt.figure(figsize=(8, 8))
        
        # reference photo 
        figure.add_subplot(1, 2, 1)
        plt.title("Reference")
        plt.imshow(self.reference)

        # sample photo/photo being evaluated 
        figure.add_subplot(1, 2, 2)

        plt.title(title)
        plt.imshow(self.sample)   

    
    # basic function to plot two images side by side
    # inputs are the image files 
    def plot_images(self, reference, sample):

        self.reference = reference
        self.sample = sample 

        figure = plt.figure(figsize=(8,8))

        figure.add_subplot(1, 2, 1)
        plt.title("Reference")
        plt.imshow(self.reference)

        figure.add_subplot(1, 2, 2)
        plt.title("Sample")
        plt.imshow(self.sample)    

    # function to plot a single image 
    # input is the path to the image file 
    def plot_single_image (self, image, title):
        
        self.image = image
        self.title = title
        img = Image.open(self.image)

        plt.figure(figsize=(6,6))
        plt.title(self.title)
        plt.imshow(img)

    def select_files(self, b):
        clear_output()
        root = Tk()
        root.withdraw() # Hide the main window.
        root.call('wm', 'attributes', '.', '-topmost', True) # Raise the root to the top of all windows.
        b.files = filedialog.askopenfilename(multiple=True) # List of selected files will be set button's file attribute.
        #print(b.files) # Print the list of files selected.


    def three_images(self, first, second, third):

        self.first = first
        self.second = second
        self.third = third  

        figure = plt.figure(figsize=(8,8))

        figure.add_subplot(1, 2, 1)
        plt.title("Reference")
        plt.imshow(self.first)

        figure.add_subplot(1, 2, 2)
        plt.title("Sample")
        plt.imshow(self.second) 

        figure.add_subplot(1, 2, 3)
        plt.title("Sample")
        plt.imshow(self.third) 