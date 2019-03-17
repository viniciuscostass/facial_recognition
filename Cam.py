class Cam:

    def __init__(self, opencv):

        self.cv2 = opencv
        self.webcam = None

    def getFrame(self, resize_factor=0.25):

        s, frame = self.webcam.read()
        frame = self.cv2.flip(frame, 180)
        small_frame = self.cv2.resize(frame, (0, 0), fx=resize_factor, fy=resize_factor)

        return frame, small_frame

    def showFrame(self, frame=None):
        if frame is None:
            frame = self.getFrame()
        self.cv2.imshow('Cam', frame)

    def onCam(self):
        self.webcam = self.cv2.VideoCapture(0)

    def offCam(self):
        self.webcam.release()
        self.cv2.destroyAllWindows()