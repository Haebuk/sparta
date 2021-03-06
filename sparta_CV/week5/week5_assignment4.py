import cv2
import numpy as np

proto = 'models/colorization_deploy_v2.prototxt'
weights = 'models/colorization_release_v2.caffemodel'
sr = cv2.dnn_superres.DnnSuperResImpl_create() # Super resolution 모델
sr.readModel('models/EDSR_x3.pb')
sr.setModel('edsr', 3)

net = cv2.dnn.readNetFromCaffe(proto, weights)

pts_in_hull = np.load('models/pts_in_hull.npy')
pts_in_hull = pts_in_hull.transpose().reshape(2, 313, 1, 1).astype(np.float32)
net.getLayer(net.getLayerId('class8_ab')).blobs = [pts_in_hull]

net.getLayer(net.getLayerId('conv8_313_rh')).blobs = [np.full((1, 313), 2.606, np.float32)]

img = cv2.imread('imgs/07.jpg')

result = sr.upsample(img) # 추론

resized_img = cv2.resize(img, dsize=None, fx=3, fy=3) # 가로 세로 3배씩 늘리기


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

result_sr = sr.upsample(output_bgr) # 추론
cv2.imshow('img', img) # 원본
cv2.imshow('result', resized_img) # 흑백 + 해상도 향상 
cv2.imshow('sr', result_sr) # 컬러라이즈 + 해상도 향상
cv2.waitKey(0)