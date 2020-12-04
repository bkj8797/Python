import cv2
import matplotlib.pyplot as plt

#캐스케이드 파일 지정
cascade_file = 'haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_file)

#이미지를 호출한 후 그레이스케일로 변환


    
import numpy as np

# 웹 카메라로부터 입력받기 --- (*1)
cap = cv2.VideoCapture(0)
while True:
    # 카메라의 이미지 읽어 들이기 --- (*2)
    _, frame = cap.read()
    # 이미지를 축소해서 출력하기 --- (*3)
    frame = cv2.resize(frame, (500,300))
    # 윈도우에 이미지 출력하기 --- (*4)
    cv2.imshow('OpenCV Web Camera', frame)
    # ESC 또는 Enter 키가 입력되면 반복 종료하기
    k = cv2.waitKey(1) # 1msec 대기
    if k == 27 or k == 13: break
    elif k == 26:   
        print("캡쳐")
        cv2.imwrite("fali.png", frame)
        print("캡쳐성공")

cap.release() # 카메라 해제하기
cv2.destroyAllWindows() # 윈도우 제거하기

img = cv2.imread('fali.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#얼굴 인식
face_list = cascade.detectMultiScale(img_gray,minSize = (20,20))

# 결과 확인
if len(face_list) == 0 :
    print("얼굴인식 실패")
    quit()

# 인식한 부분 출력하기
i=0
for (x,y,w,h) in face_list :
    print("얼굴 좌표 :",x,y,w,h)
    red = (0,0,255)
    cv2.rectangle(img,(x,y),(x+w,y+h),red,thickness=10)
                                     
    # 이미지 자르기
    img2 = img[y:y+h,x:x+w]
    cv2.imwrite('fali{}.png'.format(i),img2)
    i=i+1
        
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()
