import cv2

cap = cv2.VideoCapture('week1/04.mp4') # 안에 다 지우고 0만 넣으면 웹캠으로 나옴

# 동영상은 이미지의 연속 
# ret: 동영상이 끝나면 False
# img: 이미지
while True:
    ret, img = cap.read()

    if ret == False:
        break

    cv2.rectangle(img, pt1=(721, 183), pt2=(878, 465), color=(255, 0, 0), thickness=2)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.resize(img, dsize=(640, 360))

    img = img[100:200, 150:250] # y부터 !

    cv2.imshow('result', img)

    if cv2.waitKey(100) == ord('q'):
        break