import cv2
import numpy as np
import os
re_img1 = cv2.imread("C:\Users\Smart User\Desktop\soil1.jpg")
b, g, r = cv2.split(re_img1)

ttl = re_img1.size / 3 #divide by 3 to get the number of image PIXELS

"""b, g, and r are actually numpy.ndarray types,
so you need to use the appropriate method to sum
all array elements"""
B = float(np.sum(b)) / ttl #convert to float, as B, G, and R will otherwise be int
G = float(np.sum(g)) / ttl
R = float(np.sum(r)) / ttl
B_mean1 = list()
G_mean1 = list()
R_mean1 = list()
B_mean1.append(B)
G_mean1.append(G)
R_mean1.append(R)
F=R/G
J=F/B
if J<=0.0070 and J>=0.0261:
 print("7.30-7.50")
 if J<=0.0071 and J>=0.0451:
     print("6.80-7.04")
 if J>=0.0084 and J<=0.0239:
     print("5.58-6.58")
             
 
            


    
     
 
 
