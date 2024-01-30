# To Capture Frame
import cv2

# To process image array
import numpy as np


# import the tensorflow modules and load the model
model = load_model('keras_model.h5')
labels = open('labels.txt').read().splitlines()


# Attaching Cam indexed as 0, with the application software
camera = cv2.VideoCapture(0)

# Infinite loop
while True:

	# Reading / Requesting a Frame from the Camera 
	status , frame = camera.read()

	# if we were sucessfully able to read the frame
	if status:
 		cv2.putText(frame, predicted_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
		# Flip the frame
		frame = cv2.flip(frame	,	1)
		
		
		
		#resize the frame
    	resized_frame = cv2.resize(frame, (224, 224))		
		# expand the dimensions
		expanded_frame = np.expand_dims(normalized_frame, axis=0)
		# normalize it before feeding to the model
		normalized_frame = resized_frame / 255.0
		# get predictions from the model
		predictions = model.predict(expanded_frame)
    	predicted_label = labels[np.argmax(predictions)]
		
		
		# displaying the frames captured
		cv2.imshow('feed' , frame)

		# waiting for 1ms
		code = cv2.waitKey(1)
		
		# if space key is pressed, break the loop
		if code == 32:
			break

# release the camera from the application software
camera.release()

# close the open window
cv2.destroyAllWindows()
