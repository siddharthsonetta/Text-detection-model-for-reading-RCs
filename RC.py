# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:40:25 2020

@author: Sunit
"""

import cv2
import pytesseract
#import tesseract
import os
os.chdir(r'C:\Users\kolab\OneDrive\Desktop\RC') 
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


#UDF to Rename files
def main(): 
  
    for count, filename in enumerate(os.listdir('C:\\Users\\kolab\\OneDrive\\Desktop\\RC')): 
        dst ="Img" + str(count) + ".jpg"
        src ='C:\\Users\\kolab\\OneDrive\\Desktop\\RC\\'+ filename 
        dst ='C:\\Users\\kolab\\OneDrive\\Desktop\\RC\\'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
    

rc = []
files = os.listdir('C:\\Users\\kolab\\OneDrive\\Desktop\\RC\\')

for i in range(0,len(files)):
    text = pytesseract.image_to_string(Image.open('C:\\Users\\kolab\\OneDrive\\Desktop\\RC\\'+files[i]))
    rc.append(text)
print(rc)

import pickle
with open("Text-RC.txt", "wb") as fp: 
    pickle.dump(rc,fp)
