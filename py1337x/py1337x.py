from typing import Optional, Dict, Literal

import cloudscraper

from py1337x import config, parser, utils, models

class Py1337x:
    """
    A class to interact with the py1337x API for searching and retrieving torrent information.
    
    from py1337x import Py1337x
    
    torrents = Py1337x()
    
    vlc_media = torrents.search('vlc media player')
    print(vlc_media)
    """

    def __init__(
        self, 
        base_url: str = config.default_base_url, 
        cloudscraper_kwargs: Dict ={},
        ):
        """
        Initialize the Py1337x class with base URL, headers, and requests session.

        Args:
            base_url (Optional[str]): The base URL for the API.
            headers (Optional[dict]): The request headers.
            cloudscraper_kwargs (Optional[dict]): Kwargs to pass in cloudscraper.
        """
        self.base_url = base_url
        self.requests = cloudscraper.create_scraper(**cloudscraper_kwargs)
        self.url_builder = utils.URLBuilder(base_url)

    def search(
        self,
        query: str, 
        page: int = 1, 
        category: Optional[str] = None, 
        sort_by: Optional[Literal["time", "size", "seeders", "leechers"]] = None, 
        order: Literal["asc", "desc"] = "desc"
    ) -> models.TorrentSearchResult:
        """
        Search for torrents based on a query.

        Args:
            query (str): The search query.
            page (int): The page number.
            category (Optional[str]): Category of the torrent.
            sort_by (Optional[str]): Sort by "time", "size", "seeders" or "leechers".
            order (str): The order string ('asc' or 'desc').

        Returns:
            models.TorrentSearchResult: Result from the query
        """
        query = self.url_builder.sanitize_query(query)
        category = self.url_builder.sanitize_category(category)
        url = self.url_builder.build_search_url(query, page, category, sort_by, order)

        response = self.requests.get(url)

        return parser.torrent_parser(response, base_url=self.base_url, page=page)

    def trending(
        self, 
        category: Optional[str] = None, 
        week: bool = False
    ) -> models.TorrentSearchResult:
        """
        Retrieve trending torrents.

        Args:
            category (Optional[str]): Category of the torrent.
            week (bool): Whether to get weekly trending torrents.

        Returns:
            models.TorrentSearchResult: Trending torrents
        """
        url = self.url_builder.build_trending_url(category, week)
        response = self.requests.get(url)

        return parser.torrent_parser(response, base_url=self.base_url)

    def top(
        self, 
        category: Optional[str] = None
    ) -> models.TorrentSearchResult:
        """
        Retrieve top 100 torrents.

        Args:
            category (Optional[str]): Category of the torrent.

        Returns:
            models.TorrentSearchResult: Top 100 torrents
        """
        url = self.url_builder.build_top_url(category)
        response = self.requests.get(url)

        return parser.torrent_parser(response, base_url=self.base_url)

    def popular(
        self, 
        category: str, 
        weekly: bool = False
    ) -> models.TorrentSearchResult:
        """
        Retrieve popular torrents.

        Args:
            category (str): Category of the torrent.
            weekly (bool): Whether to get weekly popular torrents.

        Returns:
            models.TorrentSearchResult: Popular torrents
        """
        url = self.url_builder.build_popular_url(category, weekly)
        response = self.requests.get(url)

        return parser.torrent_parser(response, base_url=self.base_url)

    def browse(
        self, 
        category: str, 
        page: int = 1
    ) -> models.TorrentSearchResult:
        """
        Browse torrents by category.

        Args:
            category (str): Category of the torrent.
            page (int): The page number.

        Returns:
            models.TorrentSearchResult: Parsed browse results.
        """
        url = self.url_builder.build_browse_url(category, page)
        response = self.requests.get(url)

        return parser.torrent_parser(response, base_url=self.base_url, page=page)

    def info(
        self, 
        link: Optional[str] = None, 
        torrent_id: Optional[str] = None
    ) -> models.TorrentInfo:
        """
        Retrieve information of a torrent.

        Args:
            link (Optional[str]): The URL to the torrent.
            torrent_id (Optional[str]): The torrent ID.

        Returns:
            models.TorrentInfo: Parsed torrent information.

        Raises:
            TypeError: If neither link nor torrent_id is provided, or if both are provided.
        """
        url = self.url_builder.build_info_url(link, torrent_id)
        response = self.requests.get(url)

        return parser.info_parser(response, base_url=self.base_url)
