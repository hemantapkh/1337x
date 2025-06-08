from typing import Dict, Literal, Optional

import cloudscraper
from asyncer import asyncify

from py1337x import config, models, parser, utils


class Py1337x:
    """
    A class to interact with the py1337x API for searching and retrieving torrent information.

    Example:
        ```python
        from py1337x import Py1337x

        torrents = Py1337x()

        vlc_media = torrents.search('vlc media player')
        print(vlc_media)
        ```
    """

    def __init__(
        self,
        base_url: str = config.default_base_url,
        cloudscraper_kwargs: Dict = {},
        requests_kwargs: Dict = {}
    ):
        """
        Initialize the Py1337x class with base URL, headers, and requests session.

        Args:
            base_url (Optional[str]): The base URL for the API.
            cloudscraper_kwargs (Optional[dict]): Kwargs to pass in cloudscraper.
            requests_kwargs (Optional[dict]): Kwargs to pass in requests.
        """
        self.base_url = base_url
        self.requests = cloudscraper.create_scraper(**cloudscraper_kwargs)
        self.url_builder = utils.URLBuilder(base_url)
        self.requests_kwargs = requests_kwargs

    def search(
        self,
        query: str,
        page: int = 1,
        category: Optional[str] = None,
        sort_by: Optional[Literal["time", "size", "seeders", "leechers"]] = None,
        order: Literal["asc", "desc"] = "desc",
    ) -> models.TorrentResult:
        """
        Search for torrents based on a query.

        Args:
            query (str): The search query.
            page (int): The page number.
            category (Optional[str]): Category of the torrent.
            sort_by (Optional[str]): Sort by "time", "size", "seeders" or "leechers".
            order (str): The order string ('asc' or 'desc').

        Returns:
            Result from the query

        Example:
            Basic search
            ```python
            from py1337x import Py1337x

            results = torrents.search('ubuntu')
            print(results)
            ```

            Search with sorting by seeders
            ```python
            from py1337x.types import category, sort, order

            results = torrents.search('ubuntu', sort_by=sort.SEEDERS)
            print(results)
            ```

            Search within a category
            ```python
            results = torrents.search('ubuntu', category=category.APPS)
            print(results)
            ```

            Paginated search results, fetching page 2
            ```python
            results = torrents.search('ubuntu', page=2, order=order.ASC)
            print(results)
            ```
        """
        query = self.url_builder.sanitize_query(query)
        category = self.url_builder.sanitize_category(category)
        url = self.url_builder.build_search_url(query, page, category, sort_by, order)
        print(url)

        response = self.requests.get(url, **self.requests_kwargs)

        return parser.torrent_parser(response, base_url=self.base_url, page=page)

    def trending(self, category: Optional[str] = None, weekly: bool = False) -> models.TorrentResult:
        """
        Retrieve trending torrents.

        Args:
            category (Optional[str]): Category of the torrent.
            weekly (bool): Whether to get weekly trending torrents.

        Returns:
            Trending torrents

        Example:
            Get today's trending torrents
            ```python
            trending_today = torrents.trending()
            print(trending_today)
            ```

            Weekly trending torrents in the applications category
            ```python
            trending_weekly = torrents.trending(category=category.APPS, weekly=True)
            print(trending_weekly)
            ```
        """
        url = self.url_builder.build_trending_url(category, weekly)
        response = self.requests.get(url, **self.requests_kwargs)

        return parser.torrent_parser(response, base_url=self.base_url)

    def top(self, category: Optional[str] = None) -> models.TorrentResult:
        """
        Retrieve top 100 torrents.

        Args:
            category (Optional[str]): Category of the torrent.

        Returns:
            Top 100 torrents

        Example:
            Get top 100 torrents
            ```python
            top_torrents = torrents.top()
            print(top_torrents)
            ```

            Top torrents in specific category
            ```python
            top_movies = torrents.top(category=category.MOVIES)
            print(top_movies)
            ```
        """
        url = self.url_builder.build_top_url(category)
        response = self.requests.get(url, **self.requests_kwargs)

        return parser.torrent_parser(response, base_url=self.base_url)

    def popular(self, category: str, weekly: bool = False) -> models.TorrentResult:
        """
        Retrieve popular torrents.

        Args:
            category (str): Category of the torrent.
            weekly (bool): Whether to get weekly popular torrents.

        Returns:
            Popular torrents

        Example:
            Get popular torrents
            ```python
            popular = torrents.popular(category=category.GAMES)
            print(popular)
            ```

            Weekly popular torrents
            ```python
            popular_weekly = torrents.popular(category=category.APPS, weekly=True)
            print(popular_weekly)
            ```
        """
        url = self.url_builder.build_popular_url(category, weekly)
        response = self.requests.get(url, **self.requests_kwargs)

        return parser.torrent_parser(response, base_url=self.base_url)

    def browse(self, category: str, page: int = 1) -> models.TorrentResult:
        """
        Browse torrents by category.

        Args:
            category (str): Category of the torrent.
            page (int): The page number.

        Returns:
            Parsed browse results.

        Example:
            Browse torrents under the applications category
            ```python
            apps = torrents.browse(category=category.APPS, page=2)
            print(apps)
            ```
        """
        url = self.url_builder.build_browse_url(category, page)
        response = self.requests.get(url, **self.requests_kwargs)

        return parser.torrent_parser(response, base_url=self.base_url, page=page)

    def info(self, link: Optional[str] = None, torrent_id: Optional[str] = None) -> models.TorrentInfo:
        """
        Retrieve information of a torrent.

        Args:
            link (Optional[str]): The URL to the torrent.
            torrent_id (Optional[str]): The torrent ID.

        Returns:
            Parsed torrent information.

        Raises:
            TypeError: If neither link nor torrent_id is provided, or if both are provided.
        """
        url = self.url_builder.build_info_url(link, torrent_id)
        response = self.requests.get(url, **self.requests_kwargs)

        return parser.info_parser(response, base_url=self.base_url)


class AsyncPy1337x(Py1337x):
    """
    An experimental asynchronous version of the Py1337x class to interact with the py1337x
    asynchronously by calling the original methods in a worker thread.

    Example:
        ```python
        import asyncio

        from py1337x import AsyncPy1337x

        async def main():
            torrents = AsyncPy1337x()
            vlc_media = await torrents.search('vlc media player')
            print(vlc_media)

        asyncio.run(main())
        ```
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattribute__(self, name):
        # Get the attribute from the parent class
        attr = super().__getattribute__(name)

        if callable(attr):
            # If the attribute is callable, return an asyncified version of it
            return asyncify(attr)

        # Otherwise, return the attribute as is
        return attr
