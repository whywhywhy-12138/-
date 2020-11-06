import cv2


# 人脸数据采集
def collect(self):
        count = 0
        face_detector = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
        face_id=1
        while True:
            _, img = self.cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                count += 1
                cv2.imwrite("./dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
            if count > 60:
                break
        print('收集完成')
