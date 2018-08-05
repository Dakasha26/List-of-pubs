import requests
import json
import codecs

global token
token= ''
global pubs
pubs = ['tvoya_sychevalnya', 'anime_memasi', 'ilikehorror', 'zatinylo', '155881327', '151711800', '136669536', 'cuteunion', 'anime__world', 'anime', 
        'ttanime', 'danimeworld', 'anime__typical', 'animekunu', 'ani_jp', 'anime_t', 'typicall_anime', '1st.anime', 'animewebm', 'v_mire_anime',
        'evil_na', 'paradoksanime', 'onepsixonelove', 'fan_club_kuroko', 'animeshnik_navsegda', 'anime_memess', 'mega_kawaii_quotes', 'anime_skill', 'anicomix', 'anime11111111111111111111',
        '162975316', 'anime_arigato', '45156906', 'what_anima', 'animeart', 'the_anime_moments', 'lolispolis', 'anime.artschool', 'animedonetsk', 'clubsfa777',
        'desu.anime', 'ani_ny', 'ohayo', 'yuukime', 'kawai_animeshnik', '46073638', 'animetc', 'animemadness_666', 'shinbi', '0mach']

class Pub:
    def __init__(self, href):
        self.href = href
        self.name = None
        self.subs = None
        self.posts = None
        self.info = None
    
    @property
    def update_info(self):   
        vk_request('groups.getById', ['group_id='+self.href, 'fields=members_count'], token)
        self.info = info
        self.name = self.info['response'][0]['name']
        self.subs = self.info['response'][0]['members_count']
        print('\nИмя паблика: ', self.name, '\nСсылка: https://vk.com/' + self.href, '\nКоличество подписчиков: ' + str(self.subs))
        
        el = {'name' : self.name, 'href' : self.href, 'members_count' : self.subs}
        el_js = json.dumps(el, ensure_ascii=False)
    
        f.write('\n')
        f.write(el_js)
        f.write(',')
 
 
def vk_API(func):
	def wrapper(method, arguments, *token):
		new_method = method + "?"
		for arg in arguments:
			new_method = new_method + arg + "&"
		func(new_method, *token)
	return wrapper

@vk_API
def vk_request(new_method, token):
    request = "https://api.vk.com/method/" + new_method + "access_token=" + token + "&v=5.80"
    s = requests.get(request)
    global info
    info = s.json()


if __name__ == '__main__':
    global f
    f = codecs.open('data.json', 'w', encoding='utf-8')
    f.write('[')

    for pub in pubs:
        group = Pub(pub)
        group.update_info

    f.close()
    input('\nНажмите Enter для выхода')
