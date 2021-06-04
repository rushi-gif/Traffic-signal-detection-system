import cv2 as cv2
import numpy as np

# capturing video through webcam
cap = cv2.VideoCapture("whatsapp.mp4")

while True:
    _, img = cap.read()

    # converting frame(img i.e BGR) to HSV (hue-saturation-value)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # definig the range of red color
    red_lower = np.array([0, 205, 0], np.uint8)
    red_upper = np.array([5, 255, 255], np.uint8)

    # defining the Range of Blue color
    yellow_lower = np.array([18, 215, 0], np.uint8)
    yellow_upper = np.array([52, 225, 225], np.uint8)

    # defining the Range of yellow color
    green_lower = np.array([37, 5, 88], np.uint8)
    green_upper = np.array([120, 255, 255], np.uint8)

    # finding the range of red,blue and yellow color in the image
    red = cv2.inRange(hsv, red_lower, red_upper)
    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    green = cv2.inRange(hsv, green_lower, green_upper)

    # Morphological transformation, Dilation
    kernal = np.ones((5, 5), "uint8")

    red = cv2.dilate(red, kernal)
    res = cv2.bitwise_and(img, img, mask=red)

    yellow = cv2.dilate(yellow, kernal)
    res1 = cv2.bitwise_and(img, img, mask=yellow)

    green = cv2.dilate(green, kernal)
    res2 = cv2.bitwise_and(img, img, mask=green)

    cv2.add

    # Tracking the Red Color
    (contours, hierarchy) = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "Red color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

    # Tracking the Yellow Color
    (contours, hierarchy) = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (52, 255, 255), 2)
            cv2.putText(img, "Yellow color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (52, 255, 255))

    # Tracking the Green Color
    (contours, hierarchy) = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Green  color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0))

            # cv2.imshow("Redcolour",red)
        cv2.imshow("Color Tracking", img)
        # cv2.imshow("red",res)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # save on pressing 'y'
            cap.release()
            cv2.destroyAllWindows()
            break

        # while (1):
        #     if cv2.waitKey(10) & 0xFF == ord('q'):
        #         cap.release()
        #         cv2.destroyAllWindows()
        #         break

