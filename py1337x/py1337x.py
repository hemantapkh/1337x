import requests
import requests_cache
from py1337x import parser
from torpy.http.requests import do_request as requests_request
class py1337x():
    def __init__(self, proxy=None, cookie=None, cache=None, cacheTime=86400, backend='sqlite', use_tor=False):
        self.baseUrl = f'https://www.{proxy}' if proxy else 'https://www.1337x.to'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.5',
            'upgrade-insecure-requests': '1',
            'te': 'trailers'
        }
        self.proxies = ['1337x.to', '1337x.tw', '1377x.to', '1337xx.to', '1337x.st', 'x1337x.ws', 'x1337x.eu', 'x1337x.se', '1337x.is', '1337x.gd']
        self.categories = ['movies', 'tv', 'games', 'music', 'apps', 'anime', 'documentaries', 'xxx', 'others']

        if cookie:
            self.headers['cookie'] = f'cf_clearance={cookie}'

        self.requests = requests_cache.CachedSession(cache, expire_after=cacheTime, backend=backend) if cache else requests
        self.use_tor = use_tor

    #: Searching torrents
    def search(self, query, page=1, category=None, sortBy=None, order='desc'):
        query = '+'.join(query.split())
        category = category.upper() if category and category.lower() in ['xxx', 'tv'] else category.capitalize() if category else None
        url = f"{self.baseUrl}/{'sort-' if sortBy else ''}{'category-' if category else ''}search/{query}/{category+'/' if category else ''}{sortBy.lower()+'/' if sortBy else ''}{order.lower()+'/' if sortBy else ''}{page}/"

        if self.use_tor:
            for proxy in self.proxies:
                try:
                    response = requests_request(url, headers=self.headers, retries=1)
                    response = response.encode()
                except:
                    self.baseUrl = f'https://www.{proxy}'
                    url = f"{self.baseUrl}/{'sort-' if sortBy else ''}{'category-' if category else ''}search/{query}/{category+'/' if category else ''}{sortBy.lower()+'/' if sortBy else ''}{order.lower()+'/' if sortBy else ''}{page}/"
                    continue
                else:
                    break
        else:
            response = self.requests.get(url, headers=self.headers)
        
        return parser.torrentParser(response, baseUrl=self.baseUrl, page=page)

    #: Trending torrents
    def trending(self, category=None, week=False):
        url = f"{self.baseUrl}/trending{'-week' if week and not category else ''}{'/w/'+category.lower()+'/' if week and category else '/d/'+category.lower()+'/' if not week and category else ''}"

        if self.use_tor:
            for proxy in self.proxies:
                try:
                    response = requests_request(url, headers=self.headers, retries=1)
                    response = response.encode()
                except:
                    self.baseUrl = f'https://www.{proxy}'
                    url = f"{self.baseUrl}/trending{'-week' if week and not category else ''}{'/w/'+category.lower()+'/' if week and category else '/d/'+category.lower()+'/' if not week and category else ''}"
                    continue
                else:
                    break
        else:
            response = self.requests.get(url, headers=self.headers)
        
        return parser.torrentParser(response, baseUrl=self.baseUrl)

    #: Top 100 torrents
    def top(self, category=None):
        category = 'applications' if category and category.lower() == 'apps' else 'television' if category and category.lower() == 'tv' else category.lower() if category else None
        url = f"{self.baseUrl}/top-100{'-'+category if category else ''}"

        if self.use_tor:
            for proxy in self.proxies:
                try:
                    response = requests_request(url, headers=self.headers, retries=1)
                    response = response.encode()
                except:
                    self.baseUrl = f'https://www.{proxy}'
                    url = f"{self.baseUrl}/top-100{'-'+category if category else ''}"
                    continue
                else:
                    break
        else:
            response = self.requests.get(url, headers=self.headers)
        
        return parser.torrentParser(response, baseUrl=self.baseUrl)

    #: Popular torrents
    def popular(self, category, week=False):
        url = f"{self.baseUrl}/popular-{category.lower()}{'-week' if week else ''}"

        if self.use_tor:
            for proxy in self.proxies:
                try:
                    response = requests_request(url, headers=self.headers, retries=1)
                    response = response.encode()
                except:
                    self.baseUrl = f'https://www.{proxy}'
                    url = f"{self.baseUrl}/popular-{category.lower()}{'-week' if week else ''}"
                    continue
                else:
                    break
        else:
            response = self.requests.get(url, headers=self.headers)
        
        return parser.torrentParser(response, baseUrl=self.baseUrl)

    #: Browse torrents by category type
    def browse(self, category, page=1):
        category = category.upper() if category.lower() in ['xxx', 'tv'] else category.capitalize()
        url = f'{self.baseUrl}/cat/{category}/{page}/'

        if self.use_tor:
            for proxy in self.proxies:
                try:
                    response = requests_request(url, headers=self.headers, retries=1)
                    response = response.encode()
                except:
                    self.baseUrl = f'https://www.{proxy}'
                    url = f'{self.baseUrl}/cat/{category}/{page}/'
                    continue
                else:
                    break
        else:
            response = self.requests.get(url, headers=self.headers)
        
        return parser.torrentParser(response, baseUrl=self.baseUrl, page=page)

    #: Info of torrent
    def info(self, link=None, torrentId=None):
        if not link and not torrentId:
            raise TypeError('Missing 1 required positional argument: link or torrentId')
        elif link and torrentId:
            raise TypeError('Got an unexpected argument: Pass either link or torrentId')

        link = f'{self.baseUrl}/torrent/{torrentId}/h9/' if torrentId else link

        if self.use_tor:
            for proxy in self.proxies:
                try:
                    response = requests_request(link, headers=self.headers, retries=3)
                    response = response.encode()
                except:
                    self.baseUrl = f'https://www.{proxy}'
                    link = f'{self.baseUrl}/torrent/{torrentId}/h9/' if torrentId else link
                    continue
                else:
                    break
        else:
            response = self.requests.get(link, headers=self.headers)

        return parser.infoParser(response, baseUrl=self.baseUrl)
