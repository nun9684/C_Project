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

Data = {
    "Sampling": ["0"],
    "Aera": ["0"],
    "Length": ["0"],
    "Point": ["0"],
}

Data = pd.DataFrame(Data)
mu = [None]
mc = [None]

CountFolder = 1
PCount = 1
NCount = 1

while os.path.exists('Data/Date_' + str(CountFolder)):
    CountFolder += 1
os.makedirs('Data/Date_' + str(CountFolder))
os.makedirs('Data/Date_' + str(CountFolder) + '/p')
os.makedirs('Data/Date_' + str(CountFolder) + '/n')
os.makedirs('Data/Date_' + str(CountFolder) + '/Database')

while True:

    threshold1 = cv2.getTrackbarPos("threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("threshold2", "Parameters")
    areaMin = cv2.getTrackbarPos("areaMin", "Parameters")
    areaMax = cv2.getTrackbarPos("areaMax", "Parameters")

    ret, frame = cap.read()
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    # frame = cv2.rotate(frame, cv2.ROTATE_180)
    # frame = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    Result = frame.copy()
    Grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # GaussianBlur = cv2.GaussianBlur(Grey, (1, 1), 1)

    Canny = cv2.Canny(Grey, threshold1, threshold2)

    Dilation = cv2.dilate(Canny, np.ones((5, 5), np.uint8), iterations=1)
    Closeing = cv2.morphologyEx(Dilation, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8), iterations=2)
    contours, hierarchy = cv2.findContours(Closeing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) < 1:

        cv2.putText(Result, str("Environment Capture"), (18, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        if cv2.waitKey(1) == ord("s"):
            cv2.putText(Result, str("Environment Sampling ") + str(NCount), (18, 68), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0),2)
            cv2.imwrite('Data/Date_' + str(CountFolder) + '/n/e' + str(NCount) + ".png", frame)
            cv2.imshow("Environment Capture", Result)
            NCount += 1

    elif len(contours) >= 2:

        cv2.putText(Result, str("The object over data"), (18, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    else:
        cv2.putText(Result, str("Sampling Capture"), (18, 34), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        mu[0] = cv2.moments(contours[0])
        mc[0] = (mu[0]['m10'] / (mu[0]['m00'] + 1e-6), mu[0]['m01'] / (mu[0]['m00'] + 1e-6))
        Area = cv2.contourArea(contours[0])
        Length = cv2.arcLength(contours[0], True)
        PolyDP = cv2.approxPolyDP(contours[0], 0.00001 * Length, True)
        x, y, w, h = cv2.boundingRect(PolyDP)
        p = frame[y:y + h, x:x + w]
        if Area > areaMin and Area < areaMax:

            cv2.line(Result, tuple(PolyDP[0][0]), tuple(PolyDP[len(PolyDP) - 1][0]), (0, 255, 0), 3)
            for i in range(len(PolyDP) - 1):
                cv2.line(Result, tuple(PolyDP[i][0]), tuple(PolyDP[i + 1][0]), (0, 0, 255), 3)

            # cv2.drawContours(Result, contours, -1, (0, 0, 255), 2)
            cv2.circle(Result, (int(mc[0][0]), int(mc[0][1])), 5, (0, 255, 0), -1)
            cv2.rectangle(Result, (x - 0, y - 0), (x + w + 0, y + h + 0), (0, 255, 0), 2)
            cv2.putText(Result, "Area: " + str(Area), (x + w + 0, y + 0), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cv2.putText(Result, "Length: " + str(Length), (x + w + 0, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cv2.putText(Result, "Point: " + str(len(PolyDP)), (x + w + 0, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            if cv2.waitKey(1) == ord("s"):
                cv2.putText(Result, str("Sampling ") + str(PCount), (18, 68), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0),
                            2)
                cv2.imwrite('Data/Date_' + str(CountFolder) + '/p/' + str(PCount) + ".png", p)
                cv2.imshow("Sampling Capture", Result)
                Data.loc[PCount, 'Sampling'] = PCount
                Data.loc[PCount, 'Aera'] = Area
                Data.loc[PCount, 'Length'] = Length
                Data.loc[PCount, 'Point'] = len(PolyDP)
                PCount += 1

    cv2.imshow("Object Scan Version 1.1", Result)

    if cv2.waitKey(1) & 0xFF == 27:
        break

Data = Data.drop(index=0)
Data_save = pd.ExcelWriter('Data/Date_' + str(CountFolder) + '/Database/' + 'Database_' + str(CountFolder) + '.xlsx', engine='xlsxwriter')
Data.to_excel(Data_save, sheet_name='Sampling', index=False)
Data.to_html('Data/Date_' + str(CountFolder) + '/Database/' + 'Sampling_' + str(CountFolder) + '.html', index=False)


Data = Data.drop(columns=['Sampling'])
Data.to_excel('Data/Date_' + str(CountFolder) + '/Database/' + 'Database_' + str(CountFolder) + '.xlsx', index=False)
Data = pd.read_excel('Data/Date_' + str(CountFolder) + '/Database/' + 'Database_' + str(CountFolder) + '.xlsx')


Analysis_result = Data.describe()
Analysis_result.to_html('Data/Date_' + str(CountFolder) + '/Database/' + 'Analysis_result_' + str(CountFolder) + '.html')
Analysis_result["Name"] = ""
Analysis_result.loc['count', 'Name'] = "abcd"
Analysis_result["ID"] = ""
Analysis_result.loc['count', 'ID'] = "12345"
Analysis_result.to_excel(Data_save, sheet_name='Analysis_result')
Data_save.save()
cap.release()
cv2.destroyAllWindows()
