import requests
from py1337x import parser

class py1337x():
    def __init__(self, proxy=None):
        self.baseUrl = f'https://www.{proxy}' if proxy else 'https://www.1337xx.to'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.5',
            'upgrade-insecure-requests': '1',
            'te': 'trailers'
        }
    
    #: Searching torrents
    def search(self, query, page=1, category=None, sortBy=None, order='desc'):
        query = '+'.join(query.split())
        category = category.upper() if category and category.lower() in ['xxx', 'tv'] else category.capitalize() if category else None
        url = f"{self.baseUrl}/{'sort-' if sortBy else ''}{'category-' if category else ''}search/{query}/{category+'/' if category else ''}{sortBy.lower()+'/' if sortBy else ''}{order.lower()+'/' if sortBy else ''}{page}/"

        response = requests.get(url, headers=self.headers)
        return parser.torrentParser(response, page)

    #: Trending torrents
    def trending(self, category=None, week=False):
        url = f"{self.baseUrl}/trending{'-week' if week and not category else ''}{'/w/'+category.lower()+'/' if week and category else '/d/'+category.lower()+'/' if not week and category else ''}"
        
        response = requests.get(url, headers=self.headers)
        return parser.torrentParser(response)
    
    #: Top 100 torrents
    def top(self, category=None):
        url = f"{self.baseUrl}/top-100{'-'+category.lower() if category else ''}"
        
        response = requests.get(url, headers=self.headers)
        return parser.torrentParser(response)
    
    #: Popular torrents
    def popular(self, category, week=False):
        url = f"{self.baseUrl}/popular-{category.lower()}{'-week' if week else ''}"

        response = requests.get(url, headers=self.headers)
        return parser.torrentParser(response)

    #: Browse torrents by category type
    def browse(self, category, page=1):
        category = category.upper() if category.lower() in ['xxx', 'tv'] else category.capitalize()
        url = f'{self.baseUrl}/cat/{category}/{page}/'

        response = requests.get(url, headers=self.headers)
        return parser.torrentParser(response, page)

    #: Info of torrent
    def info(self, link, id=False):
        link = f'{self.baseUrl}/torrent/{link}/h9/'
        response = requests.get(link, headers=self.headers)

        return parser.infoParser(response)