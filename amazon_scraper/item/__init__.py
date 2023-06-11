from pydantic import validate_arguments
from typing import Optional

from .fetcher import ProductFetcher
from .parser import ProductParser

class ProductScraper:
    @validate_arguments
    def __init__(
        self,
        id: str,
        name: Optional[str] = None
    ) -> None:
        self._id = id
        self._name = name

    def scrape(self) -> dict:
        fetcher = ProductFetcher(self._id, self._name)
        html = fetcher.fetch()
        parser = ProductParser(html)
        data = parser.parse()

        data["id"] = self._id
        data["name"] = self._name
        data["url"] = fetcher._url

        return data