from json import load

from fastapi import APIRouter

from app import __version__
from app.config import BASE_URL

router = APIRouter(prefix="/platform")


@router.get("")
def api_get_platform():
    data = load(open("platform.json", "r"))
    data["version"] = __version__
    data["server"] = BASE_URL.removeprefix("http://").removeprefix("https://").split(".")[0]
    return data
