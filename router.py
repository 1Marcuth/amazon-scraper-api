from fastapi.responses import JSONResponse
from fastapi import APIRouter, Request

from amazon_scraper.product import ProductScraper
from amazon_scraper.utils import parse_url

router = APIRouter(prefix="/v1")

@router.get("/product_data")
async def product_data(request: Request, url: str = None):
    if not url:
        try:
            body = await request.json()
            url = body["url"]
        except:
            return JSONResponse({
                "message": "Not valid product URL."
            }, 400)

    if not url:
        return JSONResponse({
            "message": "Not valid product URL."
        }, 400)

    product_props = parse_url(url)
    scraper = ProductScraper(**product_props)
    data = scraper.scrape()
    return data