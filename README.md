
<h2 align='center'>✖️Unofficial Python API Wrapper of 1337x</h2>
<p align="center">
<img src="https://github.com/hemantapkh/1337x/blob/main/images/1337x.png?raw=true" align="center" height=205 alt="1337x" />
</p>
<p align="center">
<a href="https://pypi.org/project/1337x">
<img src='https://img.shields.io/pypi/v/1337x.svg'>
</a>
<a href="https://pepy.tech/project/1337x">
<img src='https://pepy.tech/badge/1337x'>
</a>
<img src='https://visitor-badge.laobi.icu/badge?page_id=hemantapkh.1337x'>
<a href="https://github.com/hemantapkh/1337x/stargazers">
<img src="https://img.shields.io/github/stars/hemantapkh/1337x" alt="Stars"/>
</a>
<a href="https://github.com/hemantapkh/1337x/issues">
<img src="https://img.shields.io/github/issues/hemantapkh/1337x" alt="Issues"/>
</a>

<p align="center">
This is the unofficial API of 1337x. It supports all proxies of 1337x and almost all functions of 1337x. You can search, get trending, top and popular torrents. Furthermore, you can browse torrents of a certain category. It also supports filtering on result by category, supports sorting and caching.
<p align="center">

## Table of Contents
- [Installation](#installation)
- [Start Guide](#start-guide)
   - [Quick Examples](#quick-examples)    
     - [Searching Torrents](#1-searching-torrents)
     - [Getting Trending Torrents](#2-getting-trending-torrents)
     - [Getting information of a torrent](#3-getting-information-of-a-torrent)
- [Contributing](#contributing)
- [License](#license)

## Installation
- Install via [PyPi](https://www.pypi.org/project/1337x)
    ```bash
    pip install 1337x
    ```

- Install from the source
    ```bash
    pip install git+https://github.com/hemantapkh/1337x
    ```

## Start guide

### Quick Examples

#### 1. Searching torrents
```python
>>> from py1337x import py1337x

# Using 1337x.tw and saving the cache in sqlite database which expires after 500 seconds
>>> torrents = py1337x(proxy='1337x.to', cache='py1337xCache', cacheTime=500)

>>> torrents.search('harry potter')
{'items': [...], 'currentPage': 1, 'itemCount': 20, 'pageCount': 50}

# Searching harry potter in category movies and sort by seeders in descending order
>>> torrents.search('harry potter', category='movies', sortBy='seeders', order='desc') 
{'items': [...], 'currentPage': 1, 'itemCount': 40, 'pageCount': 50}

# Viewing the 5th page of the result
>>> torrents.search('harry potter', page=5) 
{'items': [...], 'currentPage': , 'itemCount': 20, 'pageCount': 50}
```

#### 2. Getting Trending Torrents

```python
>>> from py1337x import py1337x

# Using the default proxy (1337x.to) Without using cache
>>> torrents = py1337x() 

# Today's trending torrents of all category
>>> torrents.trending() 
{'items': [...], 'currentPage': 1, 'itemCount': 50, 'pageCount': 1}

# Trending torrents this week of all category
>>> torrents.trending(week=True) 
{'items': [...], 'currentPage': 1, 'itemCount': 50, 'pageCount': 1}

# Todays trending anime 
>>> torrents.trending(category='anime') 
{'items': [...], 'currentPage': 1, 'itemCount': 50, 'pageCount': 1}

# Trending anime this week
>>> torrents.trending(category='anime', week=True) 
{'items': [...], 'currentPage': 1, 'itemCount': 50, 'pageCount': 1}
```

#### 3. Getting information of a torrent
```python

>>> from py1337x import py1337x

# Using 11337x.st and passing the cookie since 11337x.st is cloudflare protected
>>> torrents = py1337x('11337x.st', cookie='<cookie>')

# Getting the information of a torrent by its link
>>> torrents.info(link='https://www.1337xx.to/torrent/258188/h9/') 
{'name': 'Harry Potter and the Half-Blood Prince', 'shortName': 'Harry Potter', 'description': "....", 'category': 'Movies', 'type': 'HD', 'genre': ['Adventure', 'Fantasy', 'Family'], 'language': 'English', 'size': '3.0 GB', 'thumbnail': '...', 'images': [...], 'uploader': ' ...', 'uploaderLink': '...', 'downloads': '5310', 'lastChecked': '44 seconds ago', 'uploadDate': '4 years ago', 'seeders': '36', 'leechers': '3', 'magnetLink': '...', 'infoHash': '...'}

# Getting the information of a torrent by its link
>>> torrents.info(torrentId='258188') 
{'name': 'Harry Potter and the Half-Blood Prince', 'shortName': 'Harry Potter', 'description': "....", 'category': 'Movies', 'type': 'HD', 'genre': ['Adventure', 'Fantasy', 'Family'], 'language': 'English', 'size': '3.0 GB', 'thumbnail': '...', 'images': [...], 'uploader': ' ...', 'uploaderLink': '...', 'downloads': '5310', 'lastChecked': '44 seconds ago', 'uploadDate': '4 years ago', 'seeders': '36', 'leechers': '3', 'magnetLink': '...', 'infoHash': '...'}
```

## Contributing

Any contributions you make are **greatly appreciated**.

*Thanks to every [contributors](https://github.com/hemantapkh/1337x/graphs/contributors) who have contributed in this project.*

## License

Distributed under the MIT License. See [LICENSE](https://github.com/hemantapkh/1337x/blob/main/LICENSE) for more information.

-----
Author/Maintainer: [Hemanta Pokharel](https://github.com/hemantapkh/)
