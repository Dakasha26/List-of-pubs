import json
import os
import requests
import codecs
import datetime

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
    logs('Выполнен запрос: '+ request)
    s = requests.get(request)
    global info
    info = s.json()


def pubs_info(TOKEN, DATA):
    global logs_f
    logs_f = open('log.txt', 'w', encoding='utf-8')
    errors = 0
    tags_start = ['<html>', '<head>', '<meta charset="utf-8">', '<style>a{font-size: 1.5em; color: #000000; text-decoration: none;} #list{margin-bottom: 10px;}</style>', '</head>', '<body>']
    tags_end = ['</ul>', '</body>', '</html>']
    count = 1
    pubs = DATA.read()
    pubs = json.loads(pubs)
    
    for pub in pubs:
        logs("Обрабатывается паблик: "+ str(pub['id']))
        count_of_likes = 0
        count_of_views = 0
        try:
            vk_request('wall.get', ['count=100', 'owner_id=-'+str(pub['id'])], TOKEN)
            f_name = str(count) + '.html'
            f = open(os.path.join(r'.\pub_info\pubs', f_name), 'w', encoding='utf-8')
            count += 1
            
            for tag in tags_start:
                f.write(tag)
                f.write('\n')
            
            name = '<h1>%s</h1>\n' %pub['name']
            f.write(name)
            
            for post in info['response']['items']:
                #f.write('\n<li>'+str(post['likes']['count'])+'</li>')
                count_of_likes += post['likes']['count']
                count_of_views += post['views']['count']
            
            count_of_views = int(count_of_views* 10) / 1000
            count_of_likes = int(count_of_likes * 10) / 1000
            raiting = int(count_of_likes/count_of_views *100) / 100
            count_of_likes = '<h2>Среднее значение лайков на последних 100 постах: %s</h2>\n' %count_of_likes
            count_of_views = '<h2>Среднее значение просмотров на последних 100 постах: %s</h2>\n' %count_of_views
            raiting = '<h2>Рейтинг активности: %s</h2>\n' %raiting
            f.write(count_of_likes)
            f.write(count_of_views)
            f.write(raiting)
            
            f.write('<ul><h2 id="list">Возможные ссылки на паблик:</h2>')
            public = '<li><a href="https://vk.com/public%s">https://vk.com/public%s</a></li>' %(pub['id'], pub['id'])
            group = '<li><a href="https://vk.com/group%s">https://vk.com/group%s</a></li>' %(pub['id'], pub['id'])
            link_name = '<li><a href="https://vk.com/%s">href="https://vk.com/%s</a></li>' %(pub['href'], pub['href'])
            f.write(public)
            f.write(group)
            f.write(link_name)
            
            for tag in tags_end:
                f.write(tag)
                f.write('\n')
            
            f.close()
            logs('Паблик обработан успешно')
        except:
            logs('Во время обработки паблика произошла ошибка')
            errors += 1
    print('Во время выполнения программы возникло', errors, 'ошибок')
    logs('\nВо время выполнения программы возникло ' + str(errors) + ' ошибок')
    logs_f.close()

def logs(action):
    now = datetime.datetime.now()
    string = '[' + str(now.hour) + ' : ' + str(now.minute) + '] ' + action + '\n'
    logs_f.write(string)
    


if __name__ == '__main__':
    pass