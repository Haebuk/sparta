import cv2
import matplotlib.pyplot as plt

img =  cv2.imread(r'week1\01.jpg')

print(img)
print(img.shape) #404 높이 640 너비 3 채널, BGR

# pt1: 왼쪽위 pt2: 오른쪽 아래 (x,y) 좌표
cv2.rectangle(img, pt1=(259,89), pt2=(380,348), color=(255,0,0), thickness=2)
# center: 중심, radius: 반지름
cv2.circle(img, center=(320,220), radius=100, color=(0,0,255), thickness=3)

# 자를 때는 y, x 순서 y 89 ~ 348, x 259~380
cropped_img = img[89:348, 259:380]
# 이미지 리사이즈. 중요!
img_resized = cv2.resize(img, (512, 256))
# 이미지 컬러 변경
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('result', img_rgb)
cv2.imshow('resized', img_resized)
cv2.imshow('crop', cropped_img)
cv2.imshow('img', img) # img라는 윈도우에 img를 띄운다
cv2.waitKey(0) # 키를 입력할 때 까지 창을 띄운다
