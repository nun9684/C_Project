import cv2
import numpy as np
import pandas as pd
import os


def nothing(val):
    pass


cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("threshold1", "Parameters", 150, 255, nothing)
cv2.createTrackbar("threshold2", "Parameters", 0, 255, nothing)
cv2.createTrackbar("areaMin", "Parameters", 0, 100000, nothing)
cv2.createTrackbar("areaMax", "Parameters", 50000, 100000, nothing)
cap = cv2.VideoCapture(0)



while True:

    threshold1 = cv2.getTrackbarPos("threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("threshold2", "Parameters")
    areaMin = cv2.getTrackbarPos("areaMin", "Parameters")
    areaMax = cv2.getTrackbarPos("areaMax", "Parameters")

    ret, frame = cap.read()
    # frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    #frame = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    Result = frame.copy()
    Grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # GaussianBlur = cv2.GaussianBlur(Grey, (1, 1), 1)

    Canny = cv2.Canny(Grey, threshold1, threshold2)

    Dilation = cv2.dilate(Canny, np.ones((5, 5), np.uint8), iterations=1)
    Closeing = cv2.morphologyEx(Dilation, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8), iterations=2)
    contours, hierarchy = cv2.findContours(Closeing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(Result, contours, -1, (0, 0, 255), 2)

    mu = [None] * len(contours)
    mc = [None] * len(contours)
    for i in range(len(contours)):

        mu[i] = cv2.moments(contours[i])
        mc[i] = (mu[i]['m10'] / (mu[i]['m00'] + 1e-6), mu[i]['m01'] / (mu[i]['m00'] + 1e-6))
        cv2.circle(Result, (int(mc[i][0]), int(mc[i][1])), 5, (0, 255, 0), -1)

        Area = cv2.contourArea(contours[i])
        Length = cv2.arcLength(contours[i], True)
        PolyDP = cv2.approxPolyDP(contours[i], 0.00001 * Length, True)
        x, y, w, h = cv2.boundingRect(PolyDP)

        cv2.line(Result, tuple(PolyDP[0][0]), tuple(PolyDP[len(PolyDP) - 1][0]), (0, 255, 0), 3)
        for j in range(len(PolyDP) - 1):
            cv2.line(Result, tuple(PolyDP[j][0]), tuple(PolyDP[j + 1][0]), (0, 0, 255), 3)

        cv2.rectangle(Result, (x - 0, y - 0), (x + w + 0, y + h + 0), (0, 255, 0), 2)
        cv2.putText(Result, "Area: " + str(Area), (x + w + 0, y + 0), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.putText(Result, "Length: " + str(Length), (x + w + 0, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.putText(Result, "Point: " + str(len(PolyDP)), (x + w + 0, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        if cv2.waitKey(1) == ord("s"):
            cv2.imshow("Capture", Result)

    cv2.imshow("Result", Result)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()


