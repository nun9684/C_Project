import numpy as np
import cv2
import pandas as pd
import os

class ObjectDetection:
    def __init__(self):
        print("ObjectDetection")
        
    def nothing(val):
        pass
    
    def mainproc(self):
        #number : count of items
        #indexOfList : tarm nun
        #pageForm.setNumber(number, strNameOfItem) --> user this
        
        # Read data
        CountFolder = 1
        Data = [None]
        print('Start mainproc')
        #Read File from path
        path = os.getcwd()
        print('Read file at : ' + path + r'\GUI\Camera\Data\Date_' + str(CountFolder))
        while os.path.exists(path + r'\GUI\Camera\Data\Date_' + str(CountFolder)):
            databbuffer = pd.ExcelFile(path + r'\GUI\Camera\Data\Date_' + str(CountFolder) + r'\Database\Database_' + str(CountFolder) + '.xlsx').parse(1)
            Data.append(databbuffer)
            CountFolder += 1
            
        print(len(Data))
        print(Data[1])
        print(Data[1].iloc[3, 1])
        print(Data[1].iloc[0, 4])
        print(Data[1].iloc[0, 5].astype(int))

        cv2.namedWindow("Parameters")
        cv2.resizeWindow("Parameters",640,240)
        cv2.createTrackbar("threshold1", "Parameters", 150, 255, self.nothing)
        cv2.createTrackbar("threshold2", "Parameters", 0, 255, self.nothing)
        cap = cv2.VideoCapture(0)


        while True:

            threshold1 = cv2.getTrackbarPos("threshold1", "Parameters")
            threshold2 = cv2.getTrackbarPos("threshold2", "Parameters")

            ret, frame = cap.read()
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            #frame = cv2.rotate(frame, cv2.ROTATE_180)


            Result = frame.copy()
            Grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # GaussianBlur = cv2.GaussianBlur(Grey, (1, 1), 1)

            Canny = cv2.Canny(Grey, threshold1, threshold2)
            Dilation = cv2.dilate(Canny, np.ones((5, 5), np.uint8), iterations=1)
            Closeing = cv2.morphologyEx(Dilation, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8), iterations=2)

            contours, hierarchy = cv2.findContours(Closeing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            #cv2.drawContours(Result, contours, -1, (0, 0, 255), 2)

            if len(contours) < 1:
                cv2.putText(Result, str("None detected object"), (18, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            else:
                cv2.putText(Result, str("Total objects ") + str(len(contours)), (18, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255, 0, 0), 2)
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

                    if Area > Data[1].iloc[3, 1] and Area < Data[1].iloc[7, 1]:
                        if Length > Data[1].iloc[3, 2] and Length < Data[1].iloc[7, 2]:
                            if len(PolyDP) > Data[1].iloc[3, 3] and len(PolyDP) < Data[1].iloc[7, 3]:
                                cv2.rectangle(Result, (x - 0, y - 0), (x + w + 0, y + h + 0), (0, 255, 0), 2)
                                cv2.putText(Result, "Name: " + str(Data[1].iloc[0, 4]), (x + w + 0, y + 0), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0),2)
                                cv2.putText(Result, "ID: " + str(Data[1].iloc[0, 5].astype(int)), (x + w + 0, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)


                    else:
                        cv2.putText(Result, "Undefined", (x + w + 0, y + 0), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)


            cv2.imshow("Object Detection Ver 1.1", Result)

            if cv2.waitKey(1) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()


object = ObjectDetection()
object.mainproc()