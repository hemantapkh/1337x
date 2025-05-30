from dataclasses import asdict, dataclass
from typing import List, Optional


@dataclass
class TorrentItem:
    """Represents a single torrent item in the search results."""

    name: str
    torrent_id: str
    url: str
    seeders: str
    leechers: str
    size: str
    time: str
    uploader: str
    uploader_link: str

    def to_dict(self):
        return asdict(self)


@dataclass
class TorrentResult:
    """Represents the result of a torrent search."""

    items: List[TorrentItem]
    current_page: int
    item_count: int
    page_count: int

    def to_dict(self):
        return asdict(self)


@dataclass
class TorrentInfo:
    """Represents information about a torrent."""

    name: Optional[str]
    short_name: Optional[str]
    description: Optional[str]
    category: Optional[str]
    type: Optional[str]
    genre: Optional[List[str]]
    language: Optional[str]
    size: Optional[str]
    thumbnail: Optional[str]
    images: Optional[List[str]]
    uploader: Optional[str]
    uploader_link: Optional[str]
    downloads: Optional[str]
    last_checked: Optional[str]
    date_uploaded: Optional[str]
    seeders: Optional[str]
    leechers: Optional[str]
    magnet_link: Optional[str]
    info_hash: Optional[str]

    def to_dict(self):
        return asdict(self)
