import cv2
import numpy as np

net = cv2.dnn.readNetFromTorch('models/instance_norm/mosaic.t7')
net2 = cv2.dnn.readNetFromTorch('models/instance_norm/the_scream.t7')
net3 = cv2.dnn.readNetFromTorch('models/instance_norm/la_muse.t7')
net4 = cv2.dnn.readNetFromTorch('models/instance_norm/udnie.t7')

img = cv2.imread('imgs/hw.jpg')

h, w, c = img.shape

img = cv2.resize(img, dsize=(500, int(h / w * 500)))

MEAN_VALUE = [103.939, 116.779, 123.680]
blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)

net.setInput(blob)
output = net.forward()

output = output.squeeze().transpose((1, 2, 0))

output += MEAN_VALUE
output = np.clip(output, 0, 255)
output = output.astype('uint8')
cropped = output[57:143,188:317]
cv2.imshow('img', img)
img[57:143,188:317] = cropped
cv2.imshow('img_trans', img)

# 가로로 반반, 4분할
img2 = cv2.imread('imgs/hw.jpg')

h, w, c = img2.shape

img2 = cv2.resize(img2, dsize=(500, int(h / w * 500)))

h, w, c = img2.shape

MEAN_VALUE = [103.939, 116.779, 123.680]
blob = cv2.dnn.blobFromImage(img2, mean=MEAN_VALUE)

net2.setInput(blob)
net3.setInput(blob)
net4.setInput(blob)

output2 = net2.forward()
output3 = net3.forward()
output4 = net4.forward()

output2 = output2.squeeze().transpose((1, 2, 0))
output3 = output3.squeeze().transpose((1, 2, 0))
output4 = output4.squeeze().transpose((1, 2, 0))

output2 += MEAN_VALUE
output2 = np.clip(output2, 0, 255)
output2 = output2.astype('uint8')

output3 += MEAN_VALUE
output3 = np.clip(output3, 0, 255)
output3 = output3.astype('uint8')

output4 += MEAN_VALUE
output4 = np.clip(output4, 0, 255)
output4 = output4.astype('uint8')
print(int(h/2))
half = np.concatenate([output[:int(h/2),:], output2[int(h/2):,:]], axis=0)
half2 = np.concatenate([output3[:int(h/2),:], output4[int(h/2):,:]], axis=0)
quarter = np.concatenate([half[:,:int(w/2)], half2[:,int(w/2):]], axis=1)
cv2.imshow('half', half)
cv2.imshow('quarter', quarter)

# 동영상
cap = cv2.VideoCapture('imgs/03.mp4')
while True:
    ret, img = cap.read()

    if ret == False:
        break

    h, w, c = img.shape

    img = cv2.resize(img, dsize=(500, int(h / w * 500)))

    MEAN_VALUE = [103.939, 116.779, 123.680]
    blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)

    net2.setInput(blob)
    output = net2.forward()

    output = output.squeeze().transpose((1, 2, 0))

    output += MEAN_VALUE
    output = np.clip(output, 0, 255)
    output = output.astype('uint8')
    cv2.imshow('result', img)
    cv2.imshow('result2', output)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.waitKey(0)