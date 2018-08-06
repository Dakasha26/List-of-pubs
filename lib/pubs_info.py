import json
import os
import requests

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


def pubs_info(TOKEN, DATA):
    errors = 0
    tags_start = ['<html>', '<head>', '<meta charset="utf-8">', '</head>', '<body>', '<ul>']
    tags_end = ['</ul>', '</body>', '</html>']
    count = 0
    pubs = DATA.read()
    pubs = json.loads(pubs)
    
    for pub in pubs:
        try:
            vk_request('wall.get', ['count=100', 'owner_id='+str(pub['id'])], TOKEN)
            try:
                name = pub['name'] + '.html' 
                f = open(os.path.join(r'.\pub_info\pubs', name), 'w', encoding='utf-8')
            except:
                name = 'pub' + str(count) + '.txt'
                f = open(os.path.join(r'.\pub_info\pubs', name), 'w', encoding='utf-8')
            
            for tag in tags_start:
                f.write(tag)
                f.write('\n')
        
            for post in info['response']['items']:
                f.write('\n<li>'+str(post['likes']['count'])+'</li>')
        
            for tag in tags_end:
                f.write(tag)
                f.write('\n')
            
            f.close()
        except:
            errors += 1
        print('Во время выполнения программы возникло', errors, 'ошибок')



if __name__ == '__main__':
    pass