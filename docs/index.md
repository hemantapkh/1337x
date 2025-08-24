<p align="center">
  <img src="https://github.com/hemantapkh/1337x/blob/main/images/1337x.png?raw=true" width="300" alt="1337x" />
</p>
<p align="center">
  <a href="https://pypi.org/project/1337x">
    <img src='https://img.shields.io/pypi/v/1337x.svg' alt="Pypi Version" />
  </a>
  <a href="https://pepy.tech/project/1337x">
    <img src='https://pepy.tech/badge/1337x' alt="Downloads" />
  </a>
  <a href='https://pypi.org/project/1337x'>
    <img src='https://visitor-badge.laobi.icu/badge?page_id=hemantapkh.1337x' alt="Visitors" />
  </a>
  <a href="https://github.com/hemantapkh/1337x/stargazers">
    <img src="https://img.shields.io/github/stars/hemantapkh/1337x" alt="Stars" />
  </a>
  <a href="https://github.com/hemantapkh/1337x/issues">
    <img src="https://img.shields.io/github/issues/hemantapkh/1337x" alt="Issues" />
  </a>
</p>


## Installation

Install with pip

```console
pip install 1337x
```

Install from source

```console
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

### Asynchronous Usage
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

## Next Steps

Now that you've seen the basics, you can explore the full API reference for a detailed guide to every available method.

- **API Reference:**
  - [Synchronous Client](sync_client.md)
  - [Asynchronous Client](async_client.md)
  - [Data Models](models.md)
- **License:** This project is licensed under the MIT License.
- **Contributing:** Contributions are welcome! Please see the project on [GitHub](https://github.com/hemantapkh/1337x).

