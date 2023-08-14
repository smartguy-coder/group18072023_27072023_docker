# import requests
#
# urls = [f'https://dummyjson.com/products/{item}' for item in range(1, 101)]
#
# for url in urls:
#     response = requests.get(url)
#     print(url)
#     print(response)

import multiprocessing
print(multiprocessing.cpu_count())