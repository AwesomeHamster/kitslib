from typing import List

from ..utils import get_aio_session
from .util import ImageInfo

POST_JSON_API = 'http://konachan.net/post.json'

async def get_post(keyword: str, login: str = None, password: str = None) -> List[ImageInfo]:
    session = get_aio_session()
    params = {
        "limit": 100,
        "tags": keyword.strip(),
        "page": 1
    }
    if login and password:
        params['login'] = login
        params['password_hash'] = password

    try:
        async with session.post(POST_JSON_API, params=params, headers={
            "Accept": "application/json"
        }) as resp:
            imgs: List = await resp.json(content_type=None)

            return map(parse_images, imgs)
    except:
        raise RuntimeError('found nothing')

def parse_images(image_element) -> ImageInfo:
    return ImageInfo(
        image_id=image_element.get("id"),
        large=str(image_element.get("sample_url")),
        source=str(image_element.get("source", "null")),
        original=str(image_element.get("file_url")),
        rating=image_element.get("rating", "s"),
        score=int(image_element.get("score", 0)),
        image_copyright="Powered by Konachan.net (konachan.com)"
    )
