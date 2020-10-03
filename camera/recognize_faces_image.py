import numpy as np
import face_recognition
import pickle
import cv2
import os
# import time
from datetime import datetime as dt

# detect the (x, y)-coordinates of the bounding boxes corresponding
# to each face in the input image, then compute the facial embeddings
# for each face
#format [(78, 139, 176, 40)]

from urllib.request import urlopen
def url_to_image(url, readFlag=cv2.IMREAD_COLOR):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, readFlag)

    # return the image
    return image

def get_box(image):
	# image = url_to_image(image_path)
	# image = cv2.imread(image_path)
	print(image.shape)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	boxes = face_recognition.face_locations(rgb,
		model='cnn')
	return boxes


def recognize_face(storage_embedding_path,image,boxes):
	# for box in bbox:
	data = pickle.loads(open(storage_embedding_path, "rb").read())

	# image = cv2.imread(image_path)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	print(rgb.shape)
	print("[INFO] recognizing faces...")
	encodings = face_recognition.face_encodings(rgb, boxes)

	# initialize the list of names for each face detected
	names = []

	# loop over the facial embeddings
	for encoding in encodings:
		# attempt to match each face in the input image to our known
		# encodings
		matches = face_recognition.compare_faces(data["encodings"],
			encoding)
		name = "Unknown"

		# check to see if we have found a match
		if True in matches:
			# find the indexes of all matched faces then initialize a
			# dictionary to count the total number of times each face
			# was matched
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			# loop over the matched indexes and maintain a count for
			# each recognized face face
			for i in matchedIdxs:
				name = data["id"][i]
				counts[name] = counts.get(name, 0) + 1

			# determine the recognized face with the largest number of
			# votes (note: in the event of an unlikely tie Python will
			# select first entry in the dictionary)
			name = max(counts, key=counts.get)

		# update the list of names
		names.append(name)

	# loop over the recognized faces
	# for ((top, right, bottom, left), name) in zip(boxes, names):
	# 	# draw the predicted face name on the image
	# 	cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
	# 	y = top - 15 if top - 15 > 15 else top + 15
	# 	cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
	# 		0.75, (0, 255, 0), 2)

	# show the output image
	print("The persion identified in the pic" ,name,dt.now())
	# cv2.imshow("Image", image)
	# cv2.waitKey(0)
	#print("The persion identified in the pic" ,{a = names})

	return name


# a = get_box('path')