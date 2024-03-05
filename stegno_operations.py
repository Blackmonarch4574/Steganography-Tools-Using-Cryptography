
# codes for all 

import numpy as np
import cv2
from matplotlib import pyplot as plt
from encode_txt_data import encode_txt_data
from decode_txt_data import decode_txt_data

from encode_img_data import encode_img_data
from decode_img_data import decode_img_data

from encode_aud_data import encode_aud_data
from decode_aud_data import decode_aud_data

from encode_vid_data import encode_vid_data
from decode_vid_data import decode_vid_data
from main import *
import tkinter as tk
from tkinter import messagebox


def txt_steg():
    while True:
        print("\n\t\tTEXT STEGANOGRAPHY OPERATIONS") 
        print("1. Encode the Text message")  
        print("2. Decode the Text message")  
        print("3. Exit")  
        choice1 = int(input("Enter the Choice:"))   
        if choice1 == 1:
            encode_txt_data()
        elif choice1 == 2:
            decode_txt_data() 
        elif choice1 == 3:
            break
        else:
            print("Incorrect Choice")
        print("\n")
        

def img_steg():
    while True:
        print("\n\t\tIMAGE STEGANOGRAPHY OPERATIONS\n") 
        print("1. Encode the Text message") 
        print("2. Decode the Text message") 
        print("3. Exit")  
        choice1 = int(input("Enter the Choice: "))   
        if choice1 == 1:
            nameoffile = input("Enter name of the file (with extension) :- ")
            file_path = f"Sample_cover_files/{nameoffile}"
            image=cv2.imread(file_path)
            encode_img_data(image)
        elif choice1 == 2:
            image1=cv2.imread(input("Enter the Image you need to Decode to get the Secret message :  "))
            decode_img_data(image1)
        elif choice1 == 3:
            break
        else:
            print("Incorrect Choice")
        print("\n")


def aud_steg():
    while True:
        print("\n\t\tAUDIO STEGANOGRAPHY OPERATIONS") 
        print("1. Encode the Text message")  
        print("2. Decode the Text message")  
        print("3. Exit")  
        choice1 = int(input("Enter the Choice:"))   
        if choice1 == 1:
            encode_aud_data()
        elif choice1 == 2:
            decode_aud_data()
        elif choice1 == 3:
            break
        else:
            print("Incorrect Choice")
        print("\n")



def vid_steg():
    while True:
        print("\n\t\tVIDEO STEGANOGRAPHY OPERATIONS") 
        print("1. Encode the Text message")  
        print("2. Decode the Text message")  
        print("3. Exit")  
        choice1 = int(input("Enter the Choice:"))   
        if choice1 == 1:
           a = encode_vid_data()
        elif choice1 == 2:
            decode_vid_data(a)
        elif choice1 == 3:
            break
        else:
            print("Incorrect Choice")
        print("\n")



def main():
    print("\t\t      STEGANOGRAPHY")   
    while True:  
        print("\n\t\t\tMAIN MENU\n")  
        print("1. IMAGE STEGANOGRAPHY {Hiding Text in Image cover file}")  
        print("2. TEXT STEGANOGRAPHY {Hiding Text in Text cover file}")  
        print("3. AUDIO STEGANOGRAPHY {Hiding Text in Audio cover file}")
        print("4. VIDEO STEGANOGRAPHY {Hiding Text in Video cover file}")
        print("5. Request Encoded File from the Server")
        print("6. Exit\n")  
        choice1 = int(input("Enter the Choice: "))   
        if choice1 == 1: 
            # Perform image steganography operation and save the result
            img_steg()
            
        elif choice1 == 2:
            # Perform text steganography operation and save the result
            txt_steg()
        elif choice1 == 3:
            # Perform audio steganography operation and save the result
            aud_steg()
        elif choice1 == 4:
            # Perform video steganography operation and save the result
            vid_steg()
        elif choice1 == 5:
            request_file_from_server()
        elif choice1 == 6:
            break
        else:
            print("Incorrect Choice")
        print("\n\n")


if __name__ == "__main__":
    main()
    