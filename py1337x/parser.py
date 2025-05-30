from bs4 import BeautifulSoup
from requests import Response

from py1337x import models


def torrent_parser(response: Response, base_url: str, page: int = 1) -> models.TorrentResult:
    """
    Parse the response from a torrent result page.

    Args:
        response (Response): The HTTP response object.
        base_url (str): The base URL for the API.
        page (int): The current page number.

    Returns:
        The parsed search results.
    """
    soup = BeautifulSoup(response.content, "html.parser")

    torrent_list = soup.select('a[href*="/torrent/"]')
    seeders_list = soup.select("td.coll-2")
    leechers_list = soup.select("td.coll-3")
    size_list = soup.select("td.coll-4")
    time_list = soup.select("td.coll-date")
    uploader_list = soup.select("td.coll-5")

    last_page = soup.find("div", {"class": "pagination"})

    if not last_page:
        page_count = page
    else:
        try:
            page_count = int(last_page.findAll("a")[-1]["href"].split("/")[-2])
        except Exception:
            page_count = page

    items = []

    if torrent_list:
        for count, torrent in enumerate(torrent_list):
            name = torrent.getText().strip()
            torrent_id = torrent["href"].split("/")[2]
            link = base_url + torrent["href"]
            seeders = seeders_list[count].getText()
            leechers = leechers_list[count].getText()
            size = size_list[count].contents[0]
            time = time_list[count].getText()
            uploader = uploader_list[count].getText().strip()
            uploader_link = base_url + "/" + uploader + "/"

            items.append(
                models.TorrentItem(
                    name=name,
                    torrent_id=torrent_id,
                    url=link,
                    seeders=seeders,
                    leechers=leechers,
                    size=size,
                    time=time,
                    uploader=uploader,
                    uploader_link=uploader_link,
                )
            )

    return models.TorrentResult(
        items=items, current_page=page or 1, item_count=len(torrent_list), page_count=page_count
    )


def info_parser(response: Response, base_url: str) -> models.TorrentInfo:
    """
    Parse the response from a torrent information page.

    Args:
        response (Response): The HTTP response object.
        base_url (str): The base URL for the API.

    Returns:
        The parsed torrent information.
    """
    soup = BeautifulSoup(response.content, "html.parser")

    name = soup.find("div", {"class": "box-info-heading clearfix"})
    name = name.text.strip() if name else None

    short_name = soup.find("div", {"class": "torrent-detail-info"})
    short_name = short_name.find("h3").getText().strip() if short_name else None

    description = soup.find("div", {"class": "torrent-detail-info"})
    description = description.find("p").getText().strip() if description else None

    genre = soup.find("div", {"class": "torrent-category clearfix"})
    genre = [i.text.strip() for i in genre.find_all("span")] if genre else None

    thumbnail = soup.find("div", {"class": "torrent-image"})
    thumbnail = thumbnail.find("img")["src"] if thumbnail else None

    if thumbnail and not thumbnail.startswith("http"):
        if thumbnail.startswith("//"):
            thumbnail = "https:" + thumbnail
        else:
            thumbnail = base_url + thumbnail

    magnet_link = soup.select('a[href^="magnet"]')
    magnet_link = magnet_link[0]["href"] if magnet_link else None

    info_hash = soup.find("div", {"class": "infohash-box"})
    info_hash = info_hash.find("span").getText() if info_hash else None

    images = soup.find("div", {"class": "tab-pane active"})
    images = [i["src"] for i in images.find_all("img")] if images else None

    description_list = soup.find_all("ul", {"class": "list"})

    if len(description_list) > 2:
        first_list = description_list[1].find_all("li")
        second_list = description_list[2].find_all("li")

        category = first_list[0].find("span").getText()
        species = first_list[1].find("span").getText()
        language = first_list[2].find("span").getText()
        size = first_list[3].find("span").getText()
        uploader = first_list[4].find("span").getText().strip()
        uploader_link = base_url + "/" + uploader + "/"

        downloads = second_list[0].find("span").getText()
        last_checked = second_list[1].find("span").getText()
        date_uploaded = second_list[2].find("span").getText()
        seeders = second_list[3].find("span").getText()
        leechers = second_list[4].find("span").getText()
    else:
        category = species = language = size = uploader = uploader_link = downloads = last_checked = date_uploaded = (
            seeders
        ) = leechers = None

    return models.TorrentInfo(
        name=name,
        short_name=short_name,
        description=description,
        category=category,
        type=species,
        genre=genre,
        language=language,
        size=size,
        thumbnail=thumbnail,
        images=images if images else None,
        uploader=uploader,
        uploader_link=uploader_link,
        downloads=downloads,
        last_checked=last_checked,
        date_uploaded=date_uploaded,
        seeders=seeders,
        leechers=leechers,
        magnet_link=magnet_link,
        info_hash=info_hash.strip() if info_hash else None,
    )
