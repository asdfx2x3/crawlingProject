import requests
import json


def get_json(num):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    }
    base_url = 'https://unsplash.com/napi/collections/1065976/photos?page={}'.format(num)
    response = requests.get(base_url, headers=headers)
    json_info = json.loads(response.content.decode())

    return json_info


def parse_json():
    num = 1
    while get_json(num) is not None:
        json_text = get_json(num)
        num = num + 1
        if json_text is not None:
            for a_dict in json_text:
                img_name = a_dict['id'] + '.jpg'
                img_href = a_dict['urls']['raw']
                yield {
                    '图片id': img_name,
                    '图片地址': img_href,
                }


def save_img():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    }
    img_item = parse_json()
    for item in img_item:
        name = './image/' + item['图片id']
        url = item['图片地址']
        img_data = requests.get(url, headers=headers)
        with open(name, 'wb') as f:
            f.write(img_data.content)
            print('正在下载',name)


if __name__ == '__main__':
    save_img()
