# Read a video stream from camera(Frame by Frame)
import cv2

cap = cv2.VideoCapture(0)

while True:
	ret,frame = cap.read() # reaturns two values one is bool and the other is frame
	# if the bool value is false that means that the frame is not captured properly
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	if ret == False:
		continue

	cv2.imshow("Video Frame",frame)
	cv2.imshow('Gray Frame',gray_frame)

	# wait for a user input -q, then you will stop the loop
	key_pressed = cv2.waitKey(1) & 0xFF # bitwise and # here we get the ascii value of the key that the user pressed 
	if key_pressed == ord('q'):  # ord returns ascii value of the given character
		break

cap.release()
cv2.destroyAllWindows()
