# importing the Modules
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Capture Video From Camera



def capture_and_show_webcam(webcam_number):

    cap = cv2.VideoCapture(webcam_number)

    while True:
        isTrue, frame = cap.read()
        cv2.imshow('Video', frame)
        # waitkey has to be greater than 0 in order for the video to keep moving.
        k = cv2.waitKey(1) & 0xFF
        if k == 27:         # wait for ESC key to exit
            break
    # Once loop breaks close everything
    cv2.destroyAllWindows()
    cap.release()


def capture_and_show_video(path):
    
    cap = cv2.VideoCapture(path)

    while True:
        isTrue, frame = cap.read()
        cv2.imshow('Video', frame)
        # waitkey has to be greater than 0 in order for the video to keep moving.
        k = cv2.waitKey(1) & 0xFF
        if k == 27:         # wait for ESC key to exit
            break
    # Once loop breaks close everything
    cv2.destroyAllWindows()
    cap.release()


def main():
    capture_and_show_webcam(0)
    


if __name__ =='__main__':
    main()

    