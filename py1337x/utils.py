from typing import Optional


class URLBuilder:
    """
    A class to build and sanitize URLs.
    """

    def __init__(self, base_url: str):
        """
        Initialize the URLBuilder with the base URL.

        Args:
            base_url (str): The base URL for the API.
        """
        self.base_url = base_url

    def sanitize_query(self, query: str) -> str:
        """
        Sanitize the search query.

        Args:
            query (str): The search query.

        Returns:
            str: The sanitized query.
        """
        return "+".join(query.split())

    def sanitize_category(self, category: Optional[str]) -> Optional[str]:
        """
        Sanitize the category string.

        Args:
            category (Optional[str]): The category string.

        Returns:
            Optional[str]: The sanitized category string or None if no category is provided.
        """
        if category:
            if category.lower() in ["xxx", "tv"]:
                return category.upper()
            return category.capitalize()
        return None

    def build_search_url(
        self, query: str, page: int, category: Optional[str], sort_by: Optional[str], order: str
    ) -> str:
        """
        Build the URL for searching torrents.

        Args:
            query (str): The search query.
            page (int): The page number.
            category (Optional[str]): The category string.
            sort_by (Optional[str]): The sort by string.
            order (str): The order string ('asc' or 'desc').

        Returns:
            str: The constructed search URL.
        """
        query = self.sanitize_query(query)
        category_part = ""
        category_type = ""
        sort_part = ""
        sort_type = ""
        order_part = ""

        if category:
            category_part = "category-"
            category_type = f"{self.sanitize_category(category)}/"

        if sort_by:
            sort_part = "sort-"
            sort_type = f"{sort_by.lower()}/"
            order_part = f"{order.lower()}/"

        url = f"{self.base_url}/{sort_part}{category_part}search/{query}/{category_type}{sort_type}{order_part}{page}/"
        return url

    def build_trending_url(self, category: Optional[str], weekly: bool) -> str:
        """
        Build the URL for trending torrents.

        Args:
            category (Optional[str]): The category string.
            week (bool): Whether to get weekly trending torrents.

        Returns:
            str: The constructed trending URL.
        """
        if weekly and category:
            return f"{self.base_url}/trending/w/{category.lower()}/"
        elif weekly:
            return f"{self.base_url}/trending-week/"
        elif category:
            return f"{self.base_url}/trending/d/{category.lower()}/"
        return f"{self.base_url}/trending"

    def build_top_url(self, category: Optional[str]) -> str:
        """
        Build the URL for top 100 torrents.

        Args:
            category (Optional[str]): The category string.

        Returns:
            str: The constructed top 100 URL.
        """
        if category:
            if category.lower() == "apps":
                category = "applications"
            elif category.lower() == "tv":
                category = "television"
            return f"{self.base_url}/top-100-{category.lower()}"
        return f"{self.base_url}/top-100"

    def build_popular_url(self, category: str, weekly: bool) -> str:
        """
        Build the URL for popular torrents.

        Args:
            category (str): The category string.
            weekly (bool): Whether to get weekly popular torrents.

        Returns:
            str: The constructed popular URL.
        """
        return f"{self.base_url}/popular-{category.lower()}{'-week' if weekly else ''}"

    def build_browse_url(self, category: str, page: int) -> str:
        """
        Build the URL for browsing torrents by category.

        Args:
            category (str): The category string.
            page (int): The page number.

        Returns:
            str: The constructed browse URL.
        """
        if category.lower() in ["xxx", "tv"]:
            category = category.upper()
        else:
            category = category.capitalize()
        return f"{self.base_url}/cat/{category}/{page}/"

    def build_info_url(self, link: Optional[str], torrent_id: Optional[str]) -> Optional[str]:
        """
        Build the URL for fetching torrent info.

        Args:
            link (Optional[str]): The direct link to the torrent.
            torrent_id (Optional[str]): The torrent ID.

        Returns:
            str: The constructed info URL.

        Raises:
            TypeError: If neither link nor torrent_id is provided, or if both are provided.
        """
        if not link and not torrent_id:
            raise TypeError("Missing 1 required positional argument: link or torrent_id")
        elif link and torrent_id:
            raise TypeError("Got an unexpected argument: Pass either link or torrent_id")

        return f"{self.base_url}/torrent/{torrent_id}/-/" if torrent_id else link
