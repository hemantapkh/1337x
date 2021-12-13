from bs4 import BeautifulSoup

def torrentParser(response, baseUrl, page=1):
    soup = BeautifulSoup(response.content, 'html.parser')

    torrentList = soup.select('a[href*="/torrent/"]')
    seedersList = soup.select('td.coll-2')
    leechersList = soup.select('td.coll-3')
    sizeList = soup.select('td.coll-4')
    timeList = soup.select('td.coll-date')
    uploaderList = soup.select('td.coll-5')

    lastPage = soup.find('div', {'class': 'pagination'})

    if not lastPage:
        pageCount = page
    else:
        pageCount = int(lastPage.findAll('a')[-1].text)

    results = {'items': [], 'currentPage':page or 1, 'itemCount': len(torrentList), 'pageCount': pageCount}

    if torrentList:
        for count,torrent in enumerate(torrentList):
            name = torrent.getText().strip()
            torrentId = torrent['href'].split('/')[2]
            link = baseUrl+torrent['href']
            seeders = seedersList[count].getText()
            leechers = leechersList[count].getText()
            size = sizeList[count].contents[0]
            time = timeList[count].getText()
            uploader = uploaderList[count].getText().strip()
            uploaderLink = baseUrl+'/'+uploader+'/'
            
            results['items'].append({'name': name, 'torrentId': torrentId, 'link': link, 'seeders': seeders, 'leechers': leechers, 'size': size, 'time': time, 'uploader': uploader, 'uploaderLink': uploaderLink})

    return results

def infoParser(response, baseUrl):
    soup = BeautifulSoup(response.content, 'html.parser')

    name = soup.find('div', {'class': 'box-info-heading clearfix'})
    name = name.text.strip() if name else None
    
    shortName =  soup.find('div', {'class': 'torrent-detail-info'})
    shortName = shortName.find('h3').getText() if shortName else None

    description = soup.find('div', {'class': 'torrent-detail-info'})
    description = description.find('p').getText().strip() if description else None

    genre = soup.find('div', {'class': 'torrent-category clearfix'})
    genre = [i.text for i in genre.find_all('span')] if genre else None

    thumbnail = soup.find('div', {'class': 'torrent-image'})
    thumbnail = thumbnail.find('img')['src'] if thumbnail else None

    if thumbnail and not thumbnail.startswith(f'http'):
        thumbnail = f'{baseUrl}'+thumbnail

    magnetLink = soup.select('a[href^="magnet"]')
    magnetLink = magnetLink[0]['href'] if magnetLink else None

    infoHash = soup.find('div', {'class': 'infohash-box'})
    infoHash = infoHash.find('span').getText() if infoHash else None

    images = soup.find('div', {'class': 'tab-pane active'})
    images = [i['src'] for i in images.find_all('img')] if images else None

    descriptionList = soup.find_all('ul', {'class': 'list'})
    if len(descriptionList) > 2: 
        firstList = descriptionList[1].find_all('li')
        secondList = descriptionList[2].find_all('li')
        
        category = firstList[0].find('span').getText()
        species = firstList[1].find('span').getText()
        language = firstList[2].find('span').getText()
        size = firstList[3].find('span').getText()
        uploader = firstList[4].find('span').getText().strip()
        uploaderLink = baseUrl+'/'+uploader+'/'
        
        downloads = secondList[0].find('span').getText()
        lastChecked = secondList[1].find('span').getText()
        uploadDate = secondList[2].find('span').getText()
        seeders = secondList[3].find('span').getText()
        leechers = secondList[4].find('span').getText()
    
    else:
        category = species = language = size = uploader = uploaderLink = downloads = lastChecked = uploadDate = seeders = leechers = None
    
    return {'name': name, 'shortName': shortName, 'description': description, 'category': category, 'type': species, 'genre': genre, 'language': language, 'size': size, 'thumbnail': thumbnail, 'images': images if images else None, 'uploader': uploader, 'uploaderLink': uploaderLink, 'downloads': downloads, 'lastChecked': lastChecked, 'uploadDate': uploadDate, 'seeders': seeders, 'leechers': leechers, 'magnetLink': magnetLink, 'infoHash': infoHash.strip() if infoHash else None}