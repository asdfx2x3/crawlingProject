import pymongo


client = pymongo.MongoClient('localhost', 27017)
db = client['banzhu']
collection_lcygx = db['六朝燕歌行']

print('=' * 60)

cursor = collection_lcygx.find().sort('chap_name', 1)
print(cursor.count())

for item in cursor:
    with open('六朝燕歌行2.txt', 'a', encoding='utf-8') as f:
        f.write(item['chap_name'].join('\n'))
        f.write(item['content'].replace('\n',''))
        print('写入中...')

