from pydantic import validate_arguments
from bs4 import BeautifulSoup, Tag
from typing import Optional

class ProductParser:
    _validate_config = dict(arbitrary_types_allowed=True)

    @validate_arguments(config=_validate_config)
    def __init__(self, html: str) -> None:
        self._html = html
        self._soup = BeautifulSoup(self._html, "html.parser")

    @validate_arguments(config=_validate_config)
    def __init__(self, html: str) -> None:
        self._html = html
        self._soup = BeautifulSoup(self._html, "html.parser")

    @validate_arguments(config=_validate_config)
    def _parse_title(self, element: Tag) -> str:
        raw_title = element.text
        parsed_title = raw_title.strip()
        return parsed_title

    @validate_arguments(config=_validate_config)
    def _parse_current_price(self, element: Optional[Tag]) -> float:
        if element is None: return

        raw_price = element.text
        parsed_price = float(raw_price
            .replace("R$", "")
            .replace(".", "")
            .replace(",", "."))

        return parsed_price

    _parse_old_price = _parse_current_price

    @validate_arguments(config=_validate_config)
    def _parse_description(self, element: Optional[Tag]) -> Optional[str]:
        if element is None: return

        element_id = element.attrs["id"]
        description = ""

        if element_id == "bookDescription_feature_div":
            description = "\n".join(
                map(lambda child: child.text.strip(), element.select("p"))
            )

        elif element_id == "feature-bullets":
            description = "\n- ".join(
                map(lambda item: item.text.strip(), element.select("li"))
            )
        
        return description

    @validate_arguments(config=_validate_config)
    def _parse_image_source(self, element: Tag) -> str:
        image_source = element.attrs["src"]
        return image_source

    def parse(self) -> dict:
        data = {
            "title": self._parse_title(self._soup.select_one("#productTitle")),
            "price": {
                "current": self._parse_current_price(
                    self._soup.select_one("#price") or
                    self._soup.select_one("#corePrice_feature_div .a-offscreen")
                ),
                "old": self._parse_old_price(self._soup.select_one("#listPrice"))
            },
            "description": self._parse_description(
                self._soup.select_one("#bookDescription_feature_div") or 
                self._soup.select_one("#feature-bullets")
            ),
            "image_src": self._parse_image_source(
                self._soup.select_one("#imgBlkFront") or
                self._soup.select_one("#landingImage")
            )
        }

        return data