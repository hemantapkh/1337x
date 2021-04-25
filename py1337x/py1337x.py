import requests
from bs4 import BeautifulSoup

def torrentParser(response):
    soup = BeautifulSoup(response.content, 'html.parser')

    torrentList = soup.find_all('td', {'class': 'coll-1 name'})
    seedersList = soup.find_all('td', {'class': 'coll-2 seeds'})
    leechersList = soup.find_all('td', {'class': 'coll-3 leeches'})
    sizeList = soup.find_all('td', {'class': ['coll-4 size mob-vip', 'coll-4 size mob-uploader', 'coll-4 size mob-user', 'coll-4 size mob-trial-uploader']})
    timeList = soup.find_all('td', {'class': 'coll-date'})
    uploaderList = soup.find_all('td', {'class': ['coll-5 vip', 'coll-5 uploader', 'coll-5 user', 'coll-5 trial-uploader']})

    pageCount = soup.find('li', {'class': 'last'})
    pageCount = pageCount.findAll('a')[0]['href'].split('/')[-2] if pageCount else 1

    results = {'items': [], 'pageCount': pageCount}

    if torrentList:
        for count,torrent in enumerate(torrentList):
            seeders = seedersList[count].text
            leechers = leechersList[count].text
            size = sizeList[count].text
            time = timeList[count].text
            uploader = uploaderList[count].text
            
            results['items'].append({'name': torrent.text, 'link': 'https://www.1337xx.to'+torrent.findAll('a')[0]['href'], 'seeders': seeders, 'leechers': leechers, 'size': size, 'time': time, 'uploader': uploader})

    return results

def infoParser(response):
    soup = BeautifulSoup(response.content)

    name = soup.find('div', {'class': 'box-info-heading clearfix'})
    name = name.text.strip() if name else None
    
    shortName =  soup.find('div', {'class': 'torrent-detail-info'})
    shortName = shortName.find('h3').getText() if shortName else None

    description = soup.find('div', {'class': 'torrent-detail-info'})
    description = description.find('p').getText().strip() if description else None

    genre = soup.find('div', {'class': 'torrent-category clearfix'})
    genre = [i.text for i in genre.find_all('span')] if genre else None

    image = soup.find('div', {'class': 'torrent-image'})
    image = image.find('img')['src'] if image else None

    magnetLink = soup.select('a[href^="magnet"]')
    magnetLink = magnetLink[0]['href'] if magnetLink else None

    infoHash = soup.find('div', {'class': 'infohash-box'})
    infoHash = infoHash.find('span').getText() if infoHash else None

    descriptionList = soup.find_all('ul', {'class': 'list'})
    if descriptionList:
        firstList = descriptionList[1].find_all('li')
        secondList = descriptionList[2].find_all('li')
        
        category = firstList[0].find('span').getText()
        species = firstList[1].find('span').getText()
        language = firstList[2].find('span').getText()
        size = firstList[3].find('span').getText()
        uploader = firstList[4].find('span').getText()
        uploaderLink = firstList[4].find('a')['href']
        uploaderLink = 'https://www.1337xx.to'+uploaderLink if uploaderLink else None
        downloads = secondList[0].find('span').getText()
        lastChecked = secondList[1].find('span').getText()
        uploadDate = secondList[2].find('span').getText()
        seeders = secondList[3].find('span').getText()
        leechers = secondList[4].find('span').getText()
    
    else:
        category = species =  language = size = uploader = uploaderLink = downloads = lastChecked = uploadDate = seeders = leechers = None

    return {'name': name, 'shortName': shortName, 'description': description, 'category': category, 'type': species, 'genre': genre, 'language': language, 'size': size, 'image': image, 'uploader': uploader, 'uploaderLink': uploaderLink, 'lastChecked': lastChecked, 'uploadDate': uploadDate, 'seeders': seeders, 'leechers': leechers, 'magnetLink': magnetLink, 'infoHash': infoHash}

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
        return torrentParser(response)

    #: Trending torrents
    def trending(self, catagory=None, week=False):
        url = f"{self.baseUrl}/trending{'-week' if week and not catagory else ''}{'/w/'+catagory.lower()+'/' if week and catagory else '/d/'+catagory.lower()+'/' if not week and catagory else ''}"
        
        response = requests.get(url, headers=self.headers)
        return torrentParser(response)
    
    #: Top 100 torrents
    def top100(self, catagory=None):
        url = f"{self.baseUrl}/top-100{'-'+catagory.lower() if catagory else ''}"
        
        response = requests.get(url, headers=self.headers)
        return torrentParser(response)
    
    #: Popular torrents
    def popular(self, catagory, week=False):
        url = f"{self.baseUrl}/popular-{catagory.lower()}{'-week' if week else ''}"

        response = requests.get(url, headers=self.headers)
        return torrentParser(response)

    #: Browse torrents by catagory type
    def browse(self, catagory, page=1):
        catagory = catagory.upper() if catagory.lower() in ['xxx', 'tv'] else catagory.capitalize()
        url = f'{self.baseUrl}/cat/{catagory}/{page}/'

        response = requests.get(url, headers=self.headers)
        return torrentParser(response)

    #: Info of torrent
    def info(self, link):
        response = requests.get(link, headers=self.headers)

        return infoParser(response)