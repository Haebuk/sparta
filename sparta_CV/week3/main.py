from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model
import numpy as np
import cv2

facenet = cv2.dnn.readNet('models/deploy.prototxt', 'models/res10_300x300_ssd_iter_140000.caffemodel')
model = load_model('models/mask_detector.model')

cap = cv2.VideoCapture('videos/04.mp4')

while True:
    ret, img = cap.read()

    if ret == False:
        break
    h, w, c = img.shape
    # 이미지 전처리하기
    blob = cv2.dnn.blobFromImage(img, size=(300, 300), mean=(104., 177., 123.))

    # 얼굴 영역 탐지 모델로 추론하기
    facenet.setInput(blob)
    dets = facenet.forward()

    # 각 얼굴에 대해서 반복문 돌기
    for i in range(dets.shape[2]):
        confidence = dets[0, 0, i, 2]

        if confidence < 0.5: # 얼굴 확률 0.5 미만이면 생략
            continue

        # 사각형 꼭지점 찾기
        x1 = int(dets[0, 0, i, 3] * w)
        y1 = int(dets[0, 0, i, 4] * h)
        x2 = int(dets[0, 0, i, 5] * w)
        y2 = int(dets[0, 0, i, 6] * h)

        face = img[y1:y2, x1:x2] #crop

        face_input = cv2.resize(face, dsize=(224, 224))
        face_input = cv2.cvtColor(face_input, cv2.COLOR_BGR2RGB) # 모델이 rgb로 학습됨
        face_input = preprocess_input(face_input) # 마스크 모델의 전처리 함수 (224,224,3)
        face_input = np.expand_dims(face_input, axis=0) # (1, 224, 224, 3)

        mask, nomask = model.predict(face_input).squeeze() # 마스크률 쓴 확률, 마스크 안쓴 확률

        if mask > nomask:
            color = [0,255,0]
        else:
            color = [0,0,255]

        # 사각형 그리기
        cv2.rectangle(img, pt1=(x1, y1), pt2=(x2, y2), thickness=2, color=color)   
        cv2.imshow('result', img)

    if cv2.waitKey(1) == ord('q'):
        break

