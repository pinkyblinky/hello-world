import cv2
from webcam import pupilDilation


p = pupilDilation()
camera_port = 0
camera = cv2.VideoCapture(camera_port)
print('is the camera open?', camera.isOpened())


def do_pic():
    camera_capture = get_image()
    p.processPic(camera_capture)
    
def get_image():
    retval, im = camera.read()
    print(retval)
    return im


def deinitialize():
    del(camera)
#print('is the camera open?', camera.isOpened())
#camera_capture = get_image()
#file = "/Users/pinkyblinky01/Documents/AffectProject/hello-world/face.jpg"
#cv2.imwrite(file, camera_capture)
#del(camera)

#p.processPic()

do_pic()

