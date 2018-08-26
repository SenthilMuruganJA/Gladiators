from PIL import Image
import numpy as np
image=Image.open("C:\Users\Smart User\Desktop\soil2.jpg")

print(image.size)

#convert to array
li_r=list(image.getdata(band=0))
arr_r=np.array(li_r,dtype="uint8")
li_g=list(image.getdata(band=1))
arr_g=np.array(li_g,dtype="uint8")
li_b=list(image.getdata(band=2))
arr_b=np.array(li_b,dtype="uint8")

# reshape 
reshaper=arr_r.reshape(298,169) #size flipped so it reshapes correctly
reshapeb=arr_b.reshape(298,169)
reshapeg=arr_g.reshape(298,169)

imr=Image.fromarray(reshaper,mode=None) # mode I
imb=Image.fromarray(reshapeb,mode=None)
img=Image.fromarray(reshapeg,mode=None)

#merge
merged=Image.merge("RGB",(imr,img,imb))
merged.show()
