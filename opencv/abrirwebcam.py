import cv2
import numpy as np



def detectar_movimento_das_maos():
    pass

cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    
    cv2.imshow("imagem mil Grau", frame)
    
    cv2.waitKey(1)
    
    
    
    