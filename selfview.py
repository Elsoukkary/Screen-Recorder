import cv2 as cv
from keyboard import is_pressed

def live_view():
	global running
	capture = cv.VideoCapture(0)

	while running:
		isTrue, own_frame = capture.read()
		cv.imshow('Recording', own_frame)

		cv.waitKey(1)
		if is_pressed('q'):
			running = False

	cv.destroyAllWindows()


running = False
print("Press S to start selfview")
while not running:
	if is_pressed('s'):
		running = True
		live_view()