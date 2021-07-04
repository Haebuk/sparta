import cv2

video = cv2.VideoCapture('week1/03.mp4') # 영상 불러오기

while True:
    process, img = video.read()
    if not process: # 동영상 종료되면 탈출
        break

    img = img[183:465, 721:878] # x: 721~878, y:183~465 크롭
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 영상 그레이스케일로 변환
    cv2.imshow('img', img) # 영상 출력

    if cv2.waitKey(10) == ord('q'): # 10ms마다 이미지 출력, q입력시 종료
        break