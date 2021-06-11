import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'/opt/homebrew/bin/tesseract'
img=cv2.imread('img.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img))
z=pytesseract.image_to_boxes(img)
he,wi,_=img.shape
for i in z.splitlines():
 i=i.split(" ")
 print(i)
 x,y,w,h=int(i[1]),int(i[2]),int(i[3]),int(i[4])
 cv2.rectangle(img,(x,he-y),(w,he-h),(0,255,0),3)
 cv2.putText(img,i[0],(x+5,he-y+30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
cv2.imshow('img',img)
cv2.waitKey(0)