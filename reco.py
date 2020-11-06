import cv2

# 人脸识别
def recognition(im):

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('./trainer/trainer.yml')
    cascadePath = "./data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX
    gray = cv2.cvtColor(im, cv2.COLOR_BGRA2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 4)
        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        if conf < 100:
            pass
        else:
            Id = "Unknow"
        cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 255, 0), -1)
        cv2.putText(im, str(Id), (x, y - 40), font, 2, (255, 255, 255), 3)
    return im