import cv2
import dlib

# dlib의 face detector
detector = dlib.get_frontal_face_detector()
# landmark 모델 불러오기
predictor = dlib.shape_predictor('models/shape_predictor_5_face_landmarks.dat')

cap = cv2.VideoCapture('videos/02.mp4')
sticker_img = cv2.imread('imgs/pig.png', cv2.IMREAD_UNCHANGED)

while True:
    ret, img = cap.read()

    if not ret:
        break

    dets = detector(img)

    for det in dets:
        shape = predictor(img, det)
        # 돼지코 크기 조정을 위한 가중치 설정
        left_weight = shape.parts()[3].x - shape.parts()[2].x
        right_weight = shape.parts()[0].x - shape.parts()[1].x
        pig_x = shape.parts()[4].x
        pig_x1 = int(pig_x - left_weight) # 왼쪽 
        pig_x2 = int(pig_x + right_weight) # 오른쪽 
        
        h, w, c = sticker_img.shape

        pig_w = pig_x2 - pig_x1 # 돼지코의 가로 크기
        pig_h = int(h / w * pig_w) # 돼지코의 세로 크기. 이미지 비율 유지

        pig_y = shape.parts()[4].y # 돼지코 y 좌표
        
        pig_y1 = int(pig_y - 0.85*pig_h)
        pig_y2 = int(pig_y1 + pig_h)

        overlay_img = sticker_img.copy()
        overlay_img = cv2.resize(overlay_img, dsize=(pig_w, pig_h))

        overlay_alpha = overlay_img[:, :, 3:4] / 255.0
        background_alpha = 1.0 - overlay_alpha

        img[pig_y1:pig_y2, pig_x1:pig_x2] = overlay_alpha * overlay_img[:, :, :3] + background_alpha * img[pig_y1:pig_y2, pig_x1:pig_x2]

    cv2.imshow('result', img)
    if cv2.waitKey(1) == ord('q'):
        break