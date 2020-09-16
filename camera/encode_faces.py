from imutils import paths
import face_recognition
import numpy as np
import cv2
import os
import imutils
import pickle
from .models import Employee

def face_embedding(storage_path, storeid, empid, video_file):

	abs_path = f'{storage_path}/{storeid}'
	if not os.path.exists(abs_path):
		os.mkdir(abs_path)
	filename = f'{storage_path}/{storeid}/{storeid}.pickle'
# grab the paths to the input images in our dataset
	data = {"encodings": [], "id": []}
	if os.path.exists(filename):
		pickle_in = open(filename,"rb")
		data = pickle.load(pickle_in)
		pickle_in.close()
		# faces_data = list(np.fromfile(filename, dtype=np.float32))
		# id_data = list(np.fromfile(id_filename, dtype=np.float32))
	stream = cv2.VideoCapture(video_file)
	frame_id = 0
	while True:
		(grabbed, frame) = stream.read()
		
		# if the frame was not grabbed, then we have reached the
		# end of the stream
		if not grabbed:
			break
		# print(grabbed)
		# print(frame_id)
		# print(frame.shape)
		if frame_id % 7 == 0:
			frame = imutils.resize(frame,width=(500))
			# print('resized')
			rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			# print("rgb convertion")
			# detect the (x, y)-coordinates of the bounding boxes
			# corresponding to each face in the input image
			boxes = face_recognition.face_locations(rgb,model='cnn')
			# print('boxes')
			# compute the facial embedding for the face
			encodings = face_recognition.face_encodings(rgb, boxes)
			# loop over the encodings
			print(encodings)
			for encoding in encodings:
				print('convert to embed and store')
				# add each encoding + name to our set of known names and
				# encodings
				# print(np.asarray(encoding))
				data["encodings"].append(encoding)
				data["id"].append(int(empid))
		frame_id += 1
	stream.release()
	# np.array(faces_data).tofile(filename)
	# np.array(id_data).tofile(id_filename)
	print("[INFO] serializing encodings...")
	# data = {"encodings": knownEncodings, "id": knownNames}
	if empid in data['id']:
		f = open(filename, "wb")
		f.write(pickle.dumps(data))
		f.close()
		Flag = 1
		print('Flag is ----', Flag)
		e = Employee.objects.get(id=empid)
		e.embedding = True
		e.save()

		


# face_embedding('/home/harsh/django-dataviv/embedding','1','121','https://storage.googleapis.com/camerax-bucket/Face_data/edab4e76f3b74c2a8eca45b367e68edc.mp4?Expires=1600086785&GoogleAccessId=camerax%40brave-computer-288608.iam.gserviceaccount.com&Signature=j6fsHwwtlGwdcCSauTur%2Bwg2wUhjddIqO7pcslnPun5h8YZx9XQPzcuZ47LhWlaeR%2FLXC9VfU8VIyOZQh3ghMR4OdVr%2BerJ%2FQuH4vAgGX2YHLXijJ871gNRqZgmD9uSxyaWfA5rw87A%2FaAORa8BKbSOq%2FKfN4iPXwuDpDHsyjNJznMlpvC7l1toCIlsbgWtM2XWKqWhQE1cyno8V7qmy2S9UrIW3TrvrUHZslLHKf3Jx5uk1RbM%2FHOEfjIc6K%2BDIvDFiH98JaqPb%2B%2BRfT2s6nJ2skFpAoYrX2qeiPDL3RSS2s4LiKuYYLlvdcNr%2FUa7GfCIRPwQlCwU6SG7UTwylgg%3D%3D')
def see_embeding(filename):
	pickle_in = open(filename,"rb")
	data = pickle.load(pickle_in)
	pickle_in.close()
	print(data)

see_embeding('/home/harsh/django-dataviv/embedding/1/1.pickle')