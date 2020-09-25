from typing import Any, List

from aiohttp import ClientSession

from ..utils import get_aio_session
from .util import ImageInfo

POST_JSON_API = "http://konachan.net/post.json"


async def get_post(
    keyword: str, login: str = None, password: str = None, api=POST_JSON_API
) -> List[ImageInfo]:
    """request https://konachan.com/post.json

    Args:
        keyword (str): tags, seperate by spaces
        login (str, optional): user name of konachan. Defaults to None.
        password (str, optional): password hash of konachan. Defaults to None.
        api (str, optional): specify http api url. Defaults to POST_JSON_API.

    Raises:
        RuntimeError: when request failed

    Returns:
        List[ImageInfo]: images list
    """
    session: ClientSession = get_aio_session()
    headers = {"Accept": "application/json"}
    params = {"limit": 100, "tags": keyword.strip(), "page": 1}
    if login and password:
        params["login"] = login
        params["password_hash"] = password

    try:
        async with session.post(POST_JSON_API, params=params, headers=headers) as resp:
            imgs: List[Any] = await resp.json()

            return list(map(_parse_images, imgs))
    except ConnectionError:
        raise RuntimeError("found nothing")


def _parse_images(image_element) -> ImageInfo:
    return ImageInfo(
        image_id=image_element.get("id"),
        large=str(image_element.get("sample_url")),
        source=str(image_element.get("source", "null")),
        original=str(image_element.get("file_url")),
        rating=image_element.get("rating", "s"),
        score=int(image_element.get("score", 0)),
        image_copyright="Powered by Konachan.net (konachan.com)",
    )
