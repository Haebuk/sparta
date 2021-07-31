import cv2

sr = cv2.dnn_superres.DnnSuperResImpl_create() # Super resolution 모델
sr.readModel('models/EDSR_x3.pb')
sr.setModel('edsr', 3)

img = cv2.imread('imgs/06.jpg') # 이미지 읽기

result = sr.upsample(img) # 추론

resized_img = cv2.resize(img, dsize=None, fx=3, fy=3) # 가로 세로 3배씩 늘리기

cv2.imshow('img', img) # 원본
cv2.imshow('result', result) # 해상도 향상
cv2.imshow('resized_img', resized_img) # 단순 3배 늘린 이미지
cv2.waitKey(0)