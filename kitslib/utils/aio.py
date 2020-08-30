import aiohttp
from typing import Any, Optional, List

session: Optional[aiohttp.ClientSession] = None


def get_aio_session() -> aiohttp.ClientSession:
    global session
    if session is None:
        session = aiohttp.ClientSession()
    return session
