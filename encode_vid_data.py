import cv2
from msgtobinary import msgtobinary
from encryption_decryption import encryption,decryption,KSA,PRGA,preparing_key_array

def embed(frame):
    data=input("\nEnter the data to be Encoded in Video :") 
    data=encryption(data)
    print("The encrypted data is : ",data)
    if (len(data) == 0): 
        raise ValueError('Data entered to be encoded is empty')

    data +='*^*^*'
    
    binary_data=msgtobinary(data)
    length_data = len(binary_data)
    
    index_data = 0
    
    for i in frame:
        for pixel in i:
            r, g, b = msgtobinary(pixel)
            if index_data < length_data:
                pixel[0] = int(r[:-1] + binary_data[index_data], 2) 
                index_data += 1
            if index_data < length_data:
                pixel[1] = int(g[:-1] + binary_data[index_data], 2) 
                index_data += 1
            if index_data < length_data:
                pixel[2] = int(b[:-1] + binary_data[index_data], 2) 
                index_data += 1
            if index_data >= length_data:
                break
        return frame
    

def encode_vid_data():
    # nameoffile = input("Enter name of the file (with extension) :- ")
    # file_path = f"Sample_cover_files/{nameoffile}"
    nameoffile = input("Enter name of the file (with extension) :- ")
    file_path = f"Sample_cover_files/{nameoffile}"
    cap=cv2.VideoCapture(file_path)
    vidcap = cv2.VideoCapture(file_path)    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    frame_width = int(vidcap.get(3))
    frame_height = int(vidcap.get(4))
    size = (frame_width, frame_height)
    out = cv2.VideoWriter('stego_video.mp4',fourcc, 25.0, size)
    max_frame=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        max_frame+=1
    cap.release()
    print("Total number of Frame in selected Video :",max_frame)
    print("Enter the frame number where you want to embed data : ")
    n=int(input())
    frame_number = 0
    while(vidcap.isOpened()):
        frame_number += 1
        ret, frame = vidcap.read()
        if ret == False:
            break
        if frame_number == n:    
            change_frame_with = embed(frame)
            frame_ = change_frame_with
            
            frame = change_frame_with
        out.write(frame)

    print("\nEncoded the data successfully in the video file.")

    return frame_

