# -*- coding: utf-8 -*-
import codecs
import requests
import json
import os


def vk_API(func):
	def wrapper(method, arguments, *TOKEN):
		new_method = method + "?"
		for arg in arguments:
			new_method = new_method + arg + "&"
		func(new_method, *TOKEN)
	return wrapper
    
@vk_API
def vk_request(new_method, TOKEN):
    request = "https://api.vk.com/method/" + new_method + "access_token=" + TOKEN + "&v=5.80"
    s = requests.get(request)
    global info
    info = s.json()

def append_data(pub, TOKEN):
    vk_request('groups.getById', ['group_id='+pub, 'fields=members_count'], TOKEN)
    name = info['response'][0]['name']
    subs = info['response'][0]['members_count']
    id = info['response'][0]['id']
    
    vk_request('wall.get', ['count=100', 'owner_id=-'+str(info['response'][0]['id'])], TOKEN)
    posts = info['response']['count']
    
    dic = {'name' : name, 'href' : pub, 'members_count' : subs, 'posts_count' : posts, 'id': id}
    data = json.dumps(dic, ensure_ascii=False)
    
    return data
    
 
def create_data(PUBS, TOKEN):
    os.chdir(r".\pub_info")
    
    f = codecs.open('data.json', 'w', encoding='utf-8')
    f.write('[')
    
    for pub in PUBS:
        data = append_data(pub, TOKEN)
        f.write('\n')
        f.write(data)
        f.write(',')
    f.seek(-1, os.SEEK_END)
    f.truncate()
    f.write('\n')
    f.write(']')
    f.close()
    
    

if __name__ == '__main__':
    pass