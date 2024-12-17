## Installation

Install 1337x with pip

```console
pip install 1337x
```

## Example

### Non Async Py1337x

```python
from py1337x import Py1337x

torrents = Py1337x()
results = torrents.search("Arch Linux")

for item in results.items:
    print(item.name)
```

### Async Py1337x

```python
import asyncio

from py1337x import AsyncPy1337x

async def main():
    torrents = AsyncPy1337x()
    vlc_media = await torrents.search('Arch Linux')
    print(vlc_media)

asyncio.run(main())
```

## Detailed Documentation

### ::: py1337x.Py1337x
