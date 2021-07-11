import cv2
import numpy as np

net = cv2.dnn.readNetFromTorch('models/instance_norm/udnie.t7')

# img = cv2.imread('imgs/01.jpg')
img = cv2.imread('imgs/kade.jpg')
h, w, c = img.shape
print(img.shape)
# 적당한 크기로 RESIZE
# 가로 500, 세로는 가로 500에 맞는 비율의 이미지크기
# h:w = new_h:500 -> new_h = h / w * 500
img = cv2.resize(img, dsize=(500, int(h / w * 500)))
# img = img[162:, 140:] # y축을 162~513 자르고, x축은 183~428, for 02.jpg 

# blobFromImage 전처리 함수, MEAN_VALUE를 이미지에서 빼준다
# 차원 변형도 시켜줌
MEAN_VALUE = [103.939, 116.779, 123.680]
blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)
print(blob.shape)

net.setInput(blob) # 전처리한 걸 모델에 입력
output = net.forward() # inference

# 후처리
output = output.squeeze().transpose((1, 2, 0)) # 늘렸던 차원을 줄이고, 변형된 차원을 원상태로 복구
output += MEAN_VALUE # 뺐던 MEAN_VALUE를 다시 더함

output = np.clip(output, 0, 255) # 더하면 255를 초과하는 경우가 있는데, 0~255로 제한
output = output.astype('uint8') # 정수형태로 변환

cv2.imshow('output', output)
cv2.imshow('img', img)
cv2.waitKey(0)