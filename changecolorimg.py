import cv2
import numpy as np
img = cv2.imread("captchanro.PNG")
kernel = np.ones((1,1),np.uint8)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations = 1)
imgEroded = cv2.erode(imgDialation,kernel,iterations = 2)
# cv2.imshow("Gray image",imgGray)
# cv2.imshow("Blur image",imgBlur)
# cv2.imshow("Canny image",imgCanny)
# cv2.imshow("dilate image",imgDialation)
# cv2.imshow("erode image",imgEroded)
# cv2.imwrite("b.png",imgGray)



# img = imgGray
change = [255,255,255]
after = [0,0,0]
for x in range(len(img)):
	for i in range(len(img[x])):
		temp = img[x][i]
		if temp[0]>=80 and temp[1] >=80 and temp[2] >=80:
			img[x][i] = after
		elif temp[0]<=10 and temp[1] <=16 and temp[2] <=70:
			img[x][i] =after
		else:
			img[x][i] = change
# cv2.imshow("img",img)
cv2.imwrite("captchanro2.png",img)
cv2.waitKey(0)


# import easyocr
# reader = easyocr.Reader(['vi'])
# results = reader.readtext("a.png")
# text = ""
# for i in results:
# 	text+=i[1]+ "\n"
# print(text)
