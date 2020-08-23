# coding=utf-8
from shodan import Shodan
import requests

api = Shodan('PSKINdQe1GyxGgecYz2191H2JoS9qvgD')

for i in range(1, 20):
    print('开始第:{}页'.format(i))
    results = api.search('port:"888"', i)
    if len(results['matches']) > 0:
        for result in results['matches']:
            try:
                url = "http://" + result['ip_str'] + ":888/pma"
                res = requests.get(url)
                if res.status_code == 200:
                    print('接口状态:{} 地址:{}'.format(200, url))
            except:
                pass
    else:
        print '结束'
        break