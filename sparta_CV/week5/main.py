import cv2
import numpy as np

proto = 'models/colorization_deploy_v2.prototxt'
weights = 'models/colorization_release_v2.caffemodel'

net = cv2.dnn.readNetFromCaffe(proto, weights)

pts_in_hull = np.load('models/pts_in_hull.npy')
pts_in_hull = pts_in_hull.transpose().reshape(2, 313, 1, 1).astype(np.float32)
net.getLayer(net.getLayerId('class8_ab')).blobs = [pts_in_hull]

net.getLayer(net.getLayerId('conv8_313_rh')).blobs = [np.full((1, 313), 2.606, np.float32)]

img = cv2.imread('imgs/02.jpg')

h, w, c = img.shape

img_input = img.copy()

img_input = img_input.astype('float32') / 255.
img_lab = cv2.cvtColor(img_input, cv2.COLOR_BGR2Lab) # Lab로
img_l = img_lab[:, :, 0:1] # L, a, b 채널 중 0번째 채널

blob = cv2.dnn.blobFromImage(img_l, size=(224, 224), mean=[50, 50, 50])

net.setInput(blob)
output = net.forward()

output = output.squeeze().transpose((1, 2, 0))

output_resized = cv2.resize(output, (w, h)) # 원본 이미지 크기로 재변형

# 딥러닝 모델은 ab채널을 반환하므로 l채널을 합쳐줌, 축은 채널 방향
output_lab = np.concatenate([img_l, output_resized], axis=2)

output_bgr = cv2.cvtColor(output_lab, cv2.COLOR_LAB2BGR)
output_bgr = output_bgr * 255
output_bgr = np.clip(output_bgr, 0, 255) # 255넘는거 자름
output_bgr = output_bgr.astype('uint8') # 정수형으로 변환

mask = np.zeros_like(img, dtype='uint8') # 이미지와 같은 형태로 0을 채워라
mask = cv2.circle(mask, center=(260, 260), radius=200, color=(1, 1, 1), thickness=-1)

color = output_bgr * mask # 마스크를 한 부분
gray = img * (1 - mask) # 마스크 안한 부분

output2 = color + gray

cv2.imshow('result2', output2)

cv2.imshow('img', img)
cv2.imshow('output', output_bgr)
cv2.waitKey(0)