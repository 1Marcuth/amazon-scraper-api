from urllib.parse import urlparse, urlunparse
from pydantic import validate_arguments
import re

@validate_arguments
def remove_query_params_from_url(url: str) -> str:
    parsed_url = urlparse(url)

    clean_url = urlunparse(
        parsed_url._replace(query="")
    )

    return clean_url

@validate_arguments
def parse_url(url: str) -> dict:
    id = None
    name = None

    url = remove_query_params_from_url(url)

    if "ref=" in url:
        url = url.split("ref=")[0]

    if url.startswith("http://"):
        url = url.replace("http://", "https://")

    elif not url.startswith("https://"):
        url = f"https://{url}"

    if not url.startswith("https://www."):
        url = url.replace("https://", "https://www.")

    if url.endswith("/"):
        url = url.removesuffix("/")

    if url.startswith("https://www.amazon.com.br/dp/"):
        match = re.match(r"https://www.amazon.com.br/dp/([^/]+)/?", url)
        id = match.group(1)

    else:
        match = re.match(r"https://www.amazon.com.br/(.*?)/dp/([^/]+)/?", url)
        name = match.group(1)
        id = match.group(2)

    return {
        "id": id,
        "name": name
    }