from hikvisionapi import Client
import cv2
import numpy as np
import time

def sharpen_image(img, alpha=1.5, beta=-0.5):
    # Apply a sharpening filter
    sharpened_img = cv2.addWeighted(img, alpha, img, 0, beta)
    return sharpened_img

def getvideo(response):
    try:
        with open('screen.jpg', 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        img = cv2.imread('screen.jpg')
        return img
    except:
        img = cv2.imread('screen.jpg')
        return img 
cam = Client('Ip', 'User', 'Password', timeout=30)
cam.count_events = 2 # The number of events we want to retrieve (default = 1)
while True:
    while True:
        response = cam.Streaming.channels[402].picture(method='get', type='opaque_data')
        img = getvideo(response)
        img = sharpen_image(img)
        cv2.imshow("show", img)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            break
    while True:
        response = cam.Streaming.channels[302].picture(method='get', type='opaque_data')
        img = getvideo(response)
        img = sharpen_image(img)
        cv2.imshow("show", img)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            break

