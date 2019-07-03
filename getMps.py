import json
# 下载
import requests

with open ('baijie.json', 'r') as obj:
    dic = json.load(obj);
    # print('........', dic['results']['tracks'])
    mp3s = dic['results']['tracks']
    for item in mp3s:
        mp3url = item['streaming_url']
        title = item['title']
        print('...............', mp3url)
        response = requests.get(mp3url).content
        f = open('./{}.mp3'.format(title), 'wb')
        f.write(response)
        f.close() 
        