import cv2
import Cam
import FaceRecognition

# Init cam
cam = Cam.Cam(cv2)
# Init face recognition
face = FaceRecognition.FaceRecognition(cv2)

# Turn on cam
cam.onCam()

# Resize frame
rf = 0.25
rf_inv = 1/rf

# Higher numbers find smaller faces
nofttu = 1

while True:

    f, sf = cam.getFrame(resize_factor=rf)
    fs, f_marker = face.getFacesInFrame(frame=f, small_frame=sf, resize_factor=rf_inv,number_of_times_to_upsample=nofttu)

    cam.showFrame(f_marker)

    t = cv2.waitKey(1)
    if t == ord('q'):
        break
    pass

cam.offCam()
