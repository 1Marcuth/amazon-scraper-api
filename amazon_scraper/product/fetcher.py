from pydantic import validate_arguments
from typing import Optional
import requests

class ProductFetcher:
    _headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "device-memory": "8",
        "downlink": "10",
        "dpr": "1",
        "ect": "4g",
        "pragma": "no-cache",
        "rtt": "50",
        "sec-ch-device-memory": "8",
        "sec-ch-dpr": "1",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-ua-platform-version": "\"10.0.0\"",
        "sec-ch-viewport-width": "1131",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "service-worker-navigation-preload": "true",
        "upgrade-insecure-requests": "1",
        "viewport-width": "1131",
        "Referer": "https://www.amazon.com.br/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    @validate_arguments
    def __init__(
        self,
        id: str,
        name: Optional[str] = None
    ) -> None:
        self._id = id
        self._name = name

        if self._name is None:
            self._url = f"https://www.amazon.com.br/dp/{self._id}/"
        else:
            self._url = f"https://www.amazon.com.br/{self._name}/dp/{self._id}/"

    def fetch(self) -> str:
        response = requests.get(
            url = self._url,
            headers = self._headers
        )

        html = response.text

        return html