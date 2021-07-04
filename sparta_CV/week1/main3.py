import cv2

img = cv2.imread('week1/01.jpg')
overlay_img = cv2.imread('week1/dices.png', cv2.IMREAD_UNCHANGED) # png 부를 때는 투명도를 같이 로드 -> 채널 4개 됨

overlay_img = cv2.resize(overlay_img, dsize=(150, 150)) # 150 * 150 으로 크기 조정
print(overlay_img.shape)
# 투명도를 표현하기 위해 기존의 BGR 채널에 A채널을 추가 (총 4채널)
# 완전 투명: 0, 완전 불투명: 255
overlay_alpha = overlay_img[:, :, 3:] / 255.0 # 0에서 1 사이값
background_alpha = 1.0 - overlay_alpha # overlay_alpha의 반대값 (배경 투명도)

x1 = 100 # 주사위 넣을 왼쪽 위 좌표
y1 = 100 # 마찬가지
x2 = x1 + 150 # 오른쪽은 픽셀만큼 더해
y2 = y1 + 150

img[y1:y2, x1:x2] = overlay_alpha * overlay_img[:, :, :3] + background_alpha * img[y1:y2, x1:x2] # 원래 이미지는 3차원이니까 인덱싱 안해도 댐

cv2.imshow('img', img)
cv2.waitKey(0)