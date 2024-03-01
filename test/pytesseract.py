import cv2
from PIL import Image
import pytesseract

# Pseudo code of OCR project
def ocr(img):
    # 1. Determine the type of source is Img or PDF
    # 2. If it's img, use img extract function; if it's PDF, use PDF extract function
    # 3. Use ML model(such as Tesseract) to identitfy the content
    # 4. Read in multiple sources at once  
    pass


image = cv2.imread('data/4.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite('temp/index_gray.jpg',gray)
blur = cv2.GaussianBlur(gray,(7,7),0)
cv2.imwrite('temp/index_blur.jpg',blur)
thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV  +cv2.THRESH_OTSU)[1]
cv2.imwrite('temp/index_thresh.jpg',thresh)
kernal = cv2.getStructuringElement(cv2.MORPH_RECT,(3,13))
cv2.imwrite('temp/index_kernal.jpg',kernal)
dilate = cv2.dilate(thresh,kernal,iterations=1)
cv2.imwrite('temp/index_dilate.jpg',dilate)
cnts = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(image,(x,y),(x+w,y+h),(36,255,12),2)
cv2.imwrite('temp/index_bbox.jpg',image)

img_file = 'data/4.jpg'
# img_file = 'temp/index_bbox.jpg'
img = Image.open(img_file)

ocr_result = pytesseract.image_to_string(img)
print(ocr_result)

