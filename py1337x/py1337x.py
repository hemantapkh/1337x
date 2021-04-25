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
    def search(self, query, page=1, catagory=None, sortBy=None, order='desc'):
        catagory = catagory.upper() if catagory and catagory.lower() in ['xxx', 'tv'] else catagory.capitalize() if catagory else None
        url = f"{self.baseUrl}/{'sort-' if sortBy else ''}{'category-' if catagory else ''}search/{query}/{catagory+'/' if catagory else ''}{sortBy.lower()+'/' if sortBy else ''}{order.lower()+'/' if sortBy else ''}{page}/"

        response = requests.get(url, headers=self.headers)
        return parser.torrentParser(response)

    #: Trending torrents
    def trending(self, catagory=None, week=False):
        url = f"{self.baseUrl}/trending{'-week' if week and not catagory else ''}{'/w/'+catagory.lower()+'/' if week and catagory else '/d/'+catagory.lower()+'/' if not week and catagory else ''}"
        
        response = requests.get(url, headers=self.headers)
        return parser.torrentParser(response)
    
    #: Top 100 torrents
    def top100(self, catagory=None):
        url = f"{self.baseUrl}/top-100{'-'+catagory.lower() if catagory else ''}"
        
        response = requests.get(url, headers=self.headers)
        return parser.torrentParser(response)
    
    #: Popular torrents
    def popular(self, catagory, week=False):
        url = f"{self.baseUrl}/popular-{catagory.lower()}{'-week' if week else ''}"

        response = requests.get(url, headers=self.headers)
        return parser.torrentParser(response)

    #: Browse torrents by catagory type
    def browse(self, catagory, page=1):
        catagory = catagory.upper() if catagory.lower() in ['xxx', 'tv'] else catagory.capitalize()
        url = f'{self.baseUrl}/cat/{catagory}/{page}/'

        response = requests.get(url, headers=self.headers)
        return parser.torrentParser(response)

    #: Info of torrent
    def info(self, link):
        response = requests.get(link, headers=self.headers)

        return parser.infoParser(response)