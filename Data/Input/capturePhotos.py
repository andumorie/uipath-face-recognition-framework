import cv2
import os
from datetime import datetime

WINDOW_TITLE = "Take photos using SPACE. Close window when done."


def takePhoto(cwd):

    cam = cv2.VideoCapture(0)
    cv2.namedWindow(WINDOW_TITLE)
    img_name = ""

    while cv2.getWindowProperty(WINDOW_TITLE, 0) >= 0:
        ret, frame = cam.read()
        cv2.imshow(WINDOW_TITLE, frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 32:
            # SPACE pressed
            img_name = cwd + "capture_{}.png".format(datetime.now().strftime("%d%m%Y%H%M%S"))
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            break

    cam.release()

    cv2.destroyAllWindows()

    return img_name


def takePhotos(cwd):

    cam = cv2.VideoCapture(0)
    cv2.namedWindow(WINDOW_TITLE)
    img_counter = 0

    while cv2.getWindowProperty(WINDOW_TITLE, 0) >= 0:
        ret, frame = cam.read()
        cv2.imshow(WINDOW_TITLE, frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "frame_{}.png".format(img_counter)
            cv2.imwrite(cwd  + img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()

    return img_counter