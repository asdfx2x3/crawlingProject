import requests
import json


headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        }

for num in range(10):
    url = 'https://unsplash.com/napi/collections/1065976/photos?page={num}'.format(num=num)
    response = requests.get(url, headers=headers)
    json_file = json.dumps(response.content.decode())
    with open(json_file, 'w') as f:
        f.write()


if __name__ == '__main__':
    pass

