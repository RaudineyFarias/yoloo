import cv2
import mediapipe as mp

import tkinter as tk

video = cv2.VideoCapture(1)

hand = mp.solutions.hands

Hand = hand.Hands(max_num_hands=1)

mpDraw = mp.solutions.drawing_utils

while True:
    check, img = video.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)
    handspoint = results.multi_hand_landmarks
    h,w,_ = img.shape
    pontos = []
    
    if handspoint:
        for points in handspoint:
            # print(points)
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
            for id,cord in enumerate(points.landmark):
               cx, cy = int(cord.x*w), int(cord.y*h)
               cv2.putText(img, str(id), (cx, cy+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,255,0),2)
               pontos.append((cx, cy))
               
               
        dedos = [8,12,16,20]
            
        contador = 0       
        if points:
            if pontos[4][0] < pontos[2][0]:
                contador +=1
            for x in dedos:
                if pontos[x][1] < pontos[x-2][1]:
                    contador +=1
                    
        cv2.rectangle(img,(80,10),(200, 100),(255,0.0),-1)            
        cv2.putText(img, str(contador), (100, 100), cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,0),5)
        
                        
    cv2.imshow("Imagem", img)
    cv2.waitKey(1)
    