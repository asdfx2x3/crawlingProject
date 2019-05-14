import requests


response = requests.get('http://p1.pstatp.com/origin/pgc-image/59d69e9780ac4672b69f6fb62b8897a5')
with open('1.jpg', 'wb') as f:
    f.write(response.content)
