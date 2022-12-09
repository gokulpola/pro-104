import cv2

img = cv2.imread("solar-system.jpg")


cv2.putText(img,
            "sun",
            (60,70),
            cv2.FONT_HERSHEY_DUPLEX,
            2,
            (0,0,255)
            )
            
cv2.putText(img,
            "mercury",
            (125,190),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (225,225,225)
            )
            
cv2.putText(img,
            "venus",
            (199,175),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (225,225,225)
            )
            
cv2.putText(img,
            "earth",
            (290,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (225,225,225)
            )
            
cv2.putText(img,
            "mars",
            (390,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (225,225,225)
            )
            
cv2.putText(img,
            "jupiter",
            (450,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (225,225,225)
            )
            
cv2.putText(img,
            "saturn",
            (690,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (225,225,225)
            )
            
cv2.putText(img,
            "uranus",
            (950,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (225,225,225)
            )
            
cv2.putText(img,
            "neptune",
            (1100,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (225,225,225)
            )

cv2.putText(img,
            "SOLAR SYSTEM",
            (400,400),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            2,
            (225,225,225)
            )
            


cv2.imshow("output",img)
cv2.waitKey(0)


