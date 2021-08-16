import cv2

img = cv2.imread('C:\\') #Your photo path
face_cascade = cv2.CascadeClassifier('C:\\') #Your frontal face cascade

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


eye_cascade = cv2.CascadeClassifier('C:\\') #Your eye cascade

img2 = img[y:y+h, x:x+w]
gray2 = gray[y:y+h, x:x+w]

eyes = eye_cascade.detectMultiScale(gray2, 1.3, 7)

for (x, y, w, h) in eyes:
    cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()