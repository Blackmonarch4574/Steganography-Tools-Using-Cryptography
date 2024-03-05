def txt_encode(text):
    l=len(text)
    i=0
    add=''
    while i<l:
        t=ord(text[i])
        if(t>=32 and t<=64):
            t1=t+48
            t2=t1^170       #170: 10101010
            res = bin(t2)[2:].zfill(8)
            add+="0011"+res
        
        else:
            t1=t-48
            t2=t1^170
            res = bin(t2)[2:].zfill(8)
            add+="0110"+res
        i+=1
    res1=add+"111111111111"
    print("The string after binary conversion appyling all the transformation :- " + (res1))   
    length = len(res1)
    print("Length of binary after conversion:- ",length)
    HM_SK=""
    ZWC={"00":u'\u200C',"01":u'\u202C',"11":u'\u202D',"10":u'\u200E'}      
    file1 = open("Sample_cover_files/cover_text.txt","r+")
    nameoffile = input("\nEnter the name of the Stego file after Encoding(with extension):- ")
    file3= open(nameoffile,"w+", encoding="utf-8")
    word=[]
    for line in file1: 
        word+=line.split()
    i=0
    while(i<len(res1)):  
        s=word[int(i/12)]
        j=0
        x=""
        HM_SK=""
        while(j<12):
            x=res1[j+i]+res1[i+j+1]
            HM_SK+=ZWC[x]
            j+=2
        s1=s+HM_SK
        file3.write(s1)
        file3.write(" ")
        i+=12
    t=int(len(res1)/12)     
    while t<len(word): 
        file3.write(word[t])
        file3.write(" ")
        t+=1
    file3.close()  
    file1.close()
    print("\nStego file has successfully generated")



def encode_txt_data():
    count2=0
    nameoffile = input("Enter name of the file (with extension) :- ")
    file_path = f"Sample_cover_files/{nameoffile}"
    file1 = open(file_path,"r")
    for line in file1: 
        for word in line.split():
            count2=count2+1
    file1.close()       
    bt=int(count2)
    print("Maximum number of words that can be inserted :- ",int(bt/6))
    text1=input("\nEnter data to be encoded:- ")
    l=len(text1)
    if(l<=bt):
        print("\nInputed message can be hidden in the cover file\n")
        txt_encode(text1)
    else:
        print("\nString is too big please reduce string size")
        encode_txt_data()

