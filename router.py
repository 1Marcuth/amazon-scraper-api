from fastapi import APIRouter, Request

from amazon_scraper.item import ProductScraper
from amazon_scraper.utils import parse_url

router = APIRouter(prefix="/v1")

@router.get("/product_data")
async def product_data(request: Request):
    body = await request.json()
    print(body)
    product_props = parse_url(body["url"])
    scraper = ProductScraper(**product_props)
    data = scraper.scrape()
    return data