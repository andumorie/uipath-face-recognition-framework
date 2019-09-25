import cv2
import os
import win32security
import win32api

WINDOW_TITLE = "Take photos using SPACE. Close window when done."

def checkCredentials(user, passw, should_check):
    if not should_check:
        return 'Success'
    domain, username = win32api.GetUserNameEx(win32api.NameSamCompatible).split('\\')
    if user.lower() != username.lower():
        return 'Wrong credentials. Please try again.'
    try:
        lg = win32security.LogonUser(user, domain, passw, win32security.LOGON32_LOGON_NETWORK,win32security.LOGON32_PROVIDER_DEFAULT)
    except:
        return 'Wrong credentials. Please try again.'
    else:
        return 'Success'


def takePhoto(cwd, name):
    os.chdir(cwd)


    cam = cv2.VideoCapture(0)
    cv2.namedWindow(WINDOW_TITLE)
    img_counter = 0
    path = "/FaceRecognition/train_img/{}/".format(name)

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
            cv2.imwrite(cwd + path + img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()

    return img_counter
