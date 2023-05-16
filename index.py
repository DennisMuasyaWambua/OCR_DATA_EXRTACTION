from paddleocr import PaddleOCR, draw_ocr
from matplotlib import pyplot as plt
import cv2
import os

ocr = PaddleOCR(lang= 'en')
img_path = os.path.join('./assets/images/','receipt.jpeg')
print(img_path)
result = ocr.ocr(img_path)
new_list = []

print("THE RESULTS ARE ***********************************\n")

for res in result:
    for i in res:
        new_list.append(i[1][0])
print(new_list)

boxes = []
for bx in result:
    for box in bx:
        boxes.append(box[0][0])
print("The boxes are:***********\n", boxes)

texts = []
for t in result:
    for text in t:
        texts.append(text[1][0])
print("The texts are:***********\n", texts)

scores = []
for sc in result:
    for score in sc:
        scores.append(score[1][1])
print("The scores are:***********\n", scores)


#specifying font path for drawing boxes
font_path = os.path.join('PaddleOCR','doc','fonts','latin.ttf')
print(font_path)

img =cv2.imread(img_path)
print(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(15,15))
annotated = draw_ocr(img,boxes,texts,scores,font_path=font_path)
plt.imshow(annotated)
plt.show()
