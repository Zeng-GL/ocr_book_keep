import easyocr

reader = easyocr.Reader(['en'], gpu=True)
result = reader.readtext('data/4.jpg')

for (bbox, text, prob) in result:
    print(text)