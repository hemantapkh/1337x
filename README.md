
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
- [Detailed Documentation](#detailed-documentation)
   - [Available attributes](#available-attributes)
   - [Available methods](#available-methods)      
   - [Available category](#available-categories)
   - [Available sorting methods](#available-sorting-methods)
- [Contributing](#contributing)
- [Projects using this API](#projects-using-this-api)
- [License](#license)

## Installation
- Install via [PyPi](https://www.pypi.org/project/1337x)
    ```bash
    pip install 1337x
    ```

- Install from the source
    ```bash
    git clone https://github.com/hemantapkh/1337x && cd 1337x && python setup.py sdist && pip install dist/*
    ```

## Start guide

### Quick Examples

#### 1. Searching torrents
```python
>>> from py1337x import py1337x

# Using 1337x.tw and saving the cache in Desktop which expires after 500 seconds
>>> torrents = py1337x(proxy='1337x.tw', cache='/home/user/Desktop/cache', cacheTime=500)

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

## Detailed documentation

## Available attributes

```python
from py1337x import py1337x

torrents = py1337x(proxy='1337x.st', cookie='<cookie>', cache='py1337xCache', cacheTime=86400, backend='sqlite')
```

**Proxy**

If the default domain is banned in your country, you can use an alternative domain of 1337x. 

- [`1337x.to`](https://1337x.to) (**default**)
- [`1337x.tw`](https://www.1337x.tw)
- [`1377x.to`](https://www.1377x.to)
- [`1337xx.to`](https://www.1337xx.to)
- [`1337x.st`](https://1337x.st)
- [`x1337x.ws`](https://x1337x.ws)
- [`x1337x.eu`](https://x1337x.eu)
- [`x1337x.se`](https://x1337x.se)
- [`1337x.is`](https://1337x.is)
- [`1337x.gd`](https://1337x.gd)

**cookie**

Some of the proxies are protected with Cloudflare. For such proxies you need to pass a cookie value. To get a cookie go the the protected site from your browser, solve the captcha and copy the value of `cf_clearance`.

``Firefox: Inspect element > Storage > Cookies`` <br>
``Chrome: Inspect element > Application > Storage > Cookies``

**cache** 

Py1337x uses [requests-cache](https://pypi.org/project/requests-cache/) for caching to store data so that future requests for that data can be served faster. `cache` can be any of the following.

- A boolean value: `True` for using cache and `False` for not using cache. (**cache is not used by default**)
- Directory for storing the cache.

**cacheTime**

By default the cache expires after one day. You can change the cache expiration time by setting a custom `cacheTime`. 

- `-1` (to never expire)

- `0` (to “expire immediately,” e.g. bypass the cache)

- A positive number (in seconds [**defaults to 86400**])

- A [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta)

- A [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime)

**backend**

The backend for storing the cache can be any of the following.

- `'sqlite'`: SQLite database (**default**)

- `'redis'`: Redis cache (`requires redis`)

- `'mongodb'`: MongoDB database (`requires pymongo`)

- `'gridfs'`: GridFS collections on a MongoDB database (`requires pymongo`)

- `'dynamodb'`: Amazon DynamoDB database (`requires boto3`)

- `'memory'`: A non-persistent cache that just stores responses in memory

## Available methods

```python
from py1337x import py1337x

torrents = py1337x()
```

 Method   | Description | Arguments 
----------|-------------|-----------
torrents.search(query)  | Search for torrents | self,<br>query: `Keyword to search for`,<br>page (Defaults to 1): `Page to view`,<br>category (optional): [category](#available-categories),<br>sortBy (optional): [Sort by](#available-sorting-methods),<br>Order (optional): [order](#available-sorting-order)
torrents.trending()     | Get trending torrents | self,<br>category (optional): [category](#available-categories),<br>week (Defaults to False): `True for weekely, False for daily`
torrents.top()          | Get top torrents      | self,<br>category (optional): [category](#available-categories)
torrents.popular(category)          | Get popular torrents      | self,<br>category: [category](#available-categories),<br>week (Defaults to False): `True for weekely, False for daily`
torrents.browse(category)          | Browse browse of certain category      | self,<br>category: [category](#available-categories),<br>page (Defaults to 1): `Page to view`
torrents&#46;info(link or torrentId)          | Get information of a torrent      | self,<br>link: `Link of a torrent` or<br>torrentId: `ID of a torrent`

### Available categories

 - `'movies'`
 - `'tv'`
 - `'games'`
 - `'music'`
 - `'apps'`
 - `'anime'`
 - `'documentaries'`
 - `'xxx'`
 - `'others'`

### Available sorting methods

- `'time'`
- `'size'`
- `'seeders'`
- `'leechers'`

### Available sorting order

- `'desc'` (for descending order)
- `'asc'` (for ascending order)

## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


*Thanks to every [contributors](https://github.com/hemantapkh/1337x/graphs/contributors) who have contributed in this project.*

## Projects using this API

* [Torrent Hunt](https://github.com/hemantapkh/torrenthunt) - Telegram bot to search torrents.

Want to list your project here? Just make a pull request.
## License

Distributed under the MIT License. See [LICENSE](https://github.com/hemantapkh/1337x/blob/main/LICENSE) for more information.

-----
Author/Maintainer: [Hemanta Pokharel](https://github.com/hemantapkh/) | Youtube: [@H9Youtube](https://youtube.com/h9youtube)