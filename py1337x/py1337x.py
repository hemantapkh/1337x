import requests
import requests_cache
from py1337x import parser
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller
class py1337x():
    def __init__(self, proxy=None, cookie=None, cache=None, cacheTime=86400, backend='sqlite'):
        self.baseUrl = f'https://www.{proxy}' if proxy else 'https://www.1337x.to'
        self.headers = {
            'User-Agent': UserAgent().random
        }
        self.tor_proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
        self.proxies = ['1337x.to', '1337x.tw', '1377x.to', '1337xx.to', '1337x.st', 'x1337x.ws', 'x1337x.eu', 'x1337x.se', '1337x.is', '1337x.gd']
        self.categories = ['movies', 'tv', 'games', 'music', 'apps', 'anime', 'documentaries', 'xxx', 'others']

        if cookie:
            self.headers['cookie'] = f'cf_clearance={cookie}'

        self.requests = requests_cache.CachedSession(cache, expire_after=cacheTime, backend=backend) if cache else requests

    #: Define a New proxy
    def setNewProxy(self, proxy: str):
        """
            Define a new proxy for requests only if the original proxy didn't work

            Parameters
            ----------
            proxy: :class:`str`
                Proxy of type '1337x.to'
        """
        self.baseUrl = f'https://www.{proxy}'
    
    #: Get New Tor IP if too many requests
    def getNewIp(self, passwd: str):
        """
            Define a new Tor IP if you can't access a proxy at all because of it's thinking you're actually spamming.

            If you actually do, so please don't, thanks.

            Parameters
            ----------
            passwd: :class:`str`
                Clear password of Tor Controller (it's never stored anywhere)
        """
        with Controller.from_port(port = 9051) as controller:
            controller.authenticate(passwd)
            controller.signal(Signal.NEWNYM)

    #: Searching torrents
    def search(self, query, page=1, category=None, sortBy=None, order='desc'):
        query = '+'.join(query.split())
        category = category.upper() if category and category.lower() in ['xxx', 'tv'] else category.capitalize() if category else None
        url = f"{self.baseUrl}/{'sort-' if sortBy else ''}{'category-' if category else ''}search/{query}/{category+'/' if category else ''}{sortBy.lower()+'/' if sortBy else ''}{order.lower()+'/' if sortBy else ''}{page}/"

        response = self.requests.get(url, headers=self.headers, proxies=self.tor_proxies)
        
        return parser.torrentParser(response, baseUrl=self.baseUrl, page=page)

    #: Trending torrents
    def trending(self, category=None, week=False):
        url = f"{self.baseUrl}/trending{'-week' if week and not category else ''}{'/w/'+category.lower()+'/' if week and category else '/d/'+category.lower()+'/' if not week and category else ''}"

        response = self.requests.get(url, headers=self.headers, proxies=self.tor_proxies)
        
        return parser.torrentParser(response, baseUrl=self.baseUrl)

    #: Top 100 torrents
    def top(self, category=None):
        category = 'applications' if category and category.lower() == 'apps' else 'television' if category and category.lower() == 'tv' else category.lower() if category else None
        url = f"{self.baseUrl}/top-100{'-'+category if category else ''}"

        response = self.requests.get(url, headers=self.headers, proxies=self.tor_proxies)
        
        return parser.torrentParser(response, baseUrl=self.baseUrl)

    #: Popular torrents
    def popular(self, category, week=False):
        url = f"{self.baseUrl}/popular-{category.lower()}{'-week' if week else ''}"

        response = self.requests.get(url, headers=self.headers, proxies=self.tor_proxies)
        
        return parser.torrentParser(response, baseUrl=self.baseUrl)

    #: Browse torrents by category type
    def browse(self, category, page=1):
        category = category.upper() if category.lower() in ['xxx', 'tv'] else category.capitalize()
        url = f'{self.baseUrl}/cat/{category}/{page}/'

        response = self.requests.get(url, headers=self.headers, proxies=self.tor_proxies)
        
        return parser.torrentParser(response, baseUrl=self.baseUrl, page=page)

    #: Info of torrent
    def info(self, link=None, torrentId=None):
        if not link and not torrentId:
            raise TypeError('Missing 1 required positional argument: link or torrentId')
        elif link and torrentId:
            raise TypeError('Got an unexpected argument: Pass either link or torrentId')

        link = f'{self.baseUrl}/torrent/{torrentId}/h9/' if torrentId else link

        response = self.requests.get(link, headers=self.headers, proxies=self.tor_proxies)

        return parser.infoParser(response, baseUrl=self.baseUrl)
