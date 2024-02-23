import json
import pickle
import requests

### Call API to generate json file with extracted data:
# url = 'https://ocr.asprise.com/api/v1/receipt'
# image = 'data/4.jpg'

# res = requests.post(url,
#                    data = {
#                        'api_key':'TEST',
#                        'recognizer':'auto',
#                        'ref_no':'oct_python_123'
#                    },
#                    files={
#                        'file':open(image,'rb')
#                    }) 

### Convert data into JSON file
# with open('response1.json','w') as f:
#     json.dump(json.loads(res.text),f)

### Data Extract
with open('response1.json','r') as f:
    data = json.load(f)

print(data['receipts'][0].keys())

items = data['receipts'][0]['items']

print(f"Your purchase at {data['receipts'][0]['merchant_name']}")

for item in items:
    print(f"{item['description']} - {item['amount']} {data['receipts'][0]['currency']}")