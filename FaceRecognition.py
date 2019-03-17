import face_recognition

green = (0, 255, 0)

class FaceRecognition:

    def __init__(self, opencv):

        self.cv2 = opencv

    def getFacesInFrame(self, frame, small_frame=None, resize_factor=4, model='hog', number_of_times_to_upsample=1):

        faces = []
        frame_copy = frame.copy()

        if small_frame is None:
            face_locations = face_recognition.face_locations(frame, model=model, number_of_times_to_upsample=number_of_times_to_upsample)
        else:
            face_locations = face_recognition.face_locations(small_frame, model=model, number_of_times_to_upsample=number_of_times_to_upsample)

        for (top, right, bottom, left) in face_locations:
            if small_frame is not None:
                top = int(resize_factor * top)
                right = int(resize_factor * right)
                bottom = int(resize_factor * bottom)
                left = int(resize_factor * left)
            face = frame[top:bottom, left:right]
            faces.append(face)
            self.cv2.rectangle(frame_copy, (left, top), (right, bottom), green, 5)

        return faces, frame_copy