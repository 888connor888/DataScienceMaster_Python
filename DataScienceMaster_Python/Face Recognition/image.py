 # to read and show an image
import cv2

img = cv2.imread('dog.png')
# read a gray scale image
gray = cv2.imread('dog.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('Dog Image',img)
cv2.imshow('Gray Image of Dog',gray)

cv2.waitKey(0) # zero means wait infinitely (here time is in ms)

cv2.destroyAllWindows() # after waiting for some time the image window is closed