import cv2

capture = cv2.VideoCapture("http://192.168.1.5:8080/video")

while True:
	_, frame = capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
	mirror = cv2.flip(gray, -1)
	cv2.imshow('Live', mirror)
	if cv2.waitKey(1) == ord("q"):
		break

capture.release()
cv2.destroyAllWindows()
