# import requests
import grequests

urls = [f'https://dummyjson.com/products/{item}' for item in range(1, 101)]

# for url in urls:
#     response = requests.get(url)
#     print(url)
#     print(response)

responses = (grequests.get(url) for url in urls)

data = grequests.map(responses)

for i in data:
    print(i.status_code, i.json())

