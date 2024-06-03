from src.CONST import BASE_URL
from src.config import settings
from src.http_client import CMCHTTPClient


cmc_client = CMCHTTPClient(
    base_url=BASE_URL,
    api_key=settings.CMC_API_KEY,
)
