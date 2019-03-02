import cv2
import numpy as np

img = cv2.imread('shapes.jpg',0)
ret,thresh = cv2.threshold(img,195,195,195)
ret,thresh = cv2.threshold(img, thresh, maxValue, cv2.THRESH_TRUNC)
_,contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
	(x,y),radius = cv2.minEnclosingCircle(cnt)
	center = (int(x),int(y))
	radius = int(radius)
	img = cv2.circle(img,center,radius,(0,0,0),2)
	
cv2.imshow("shapes", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
