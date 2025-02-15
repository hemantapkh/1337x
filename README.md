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
The ultimate Python API wrapper for 1337x.

<p align="center">

## Table of Contents
- [Installation](#installation)
- [Getting Started](#getting-started)
   - [Examples](#examples)
   - [Asynchronous Usage](#asynchronous-usage)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Installation
Install via [PyPi](https://www.pypi.org/project/1337x):
```bash
pip install 1337x
```

Or install from the source:
```bash
pip install git+https://github.com/hemantapkh/1337x
```


## Examples

### Searching Torrents
```python
import py1337x

torrents = py1337x.Py1337x()

# Basic search
results = torrents.search('ubuntu', page=1)
for result in results.items:
  print(f"Title={result.name} Seeders={result.seeders}")

# Search with sorting by seeders
results = torrents.search('vlc', sort_by=py1337x.sort.SEEDERS, category=py1337x.category.APPS)
print(results)

# Get today's trending torrents
results = torrents.trending()
print(results)
```

### Getting Torrent Information
To get magnetlink and other information of the torrent.
```python
# Getting info the the first result of the above search
torrent_id = results.items[0].torrent_id
info = torrents.info(torrent_id=torrent_id)
print(info)

# Convert the result to dictionary
info_dict = info.to_dict()
print(info_dict)
```

## Asynchronous Usage
For asynchronous usage, all functionalities are the same; use `AsyncPy1337x` instead of `Py1337x`:

```python
import asyncio
from py1337x import AsyncPy1337x

async def main():
    torrents = AsyncPy1337x()
    results = await torrents.search('vlc media player')
    print(results)

asyncio.run(main())
```

## Documentation

The detailled documentation of the project is available [here](https://1337x.readthedocs.org/en/latest/).

## Contributing

Any contributions you make are **greatly appreciated**.

*Thanks to every [contributors](https://github.com/hemantapkh/1337x/graphs/contributors) who have contributed in this project.*

## License

Distributed under the MIT License. See [LICENSE](https://github.com/hemantapkh/1337x/blob/main/LICENSE) for more information.

-----
Author/Maintainer: [Hemanta Pokharel](https://github.com/hemantapkh/)
