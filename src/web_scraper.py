import os
import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

def fetch_web_data():
    """Scrapes data from a configured webpage."""
    url = os.getenv("TARGET_URL")
    if not url:
        logger.warning("TARGET_URL not defined. Skipping web scrape.")
        return []

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Generic logic: extract title and count <a> tags metrics
        title = soup.title.string if soup.title else "No Title"
        links = len(soup.find_all('a'))
        headers = len(soup.find_all(['h1', 'h2', 'h3']))
        
        logger.info(f"Successfully scraped web data from {url}")
        return [{
            "Source": "Web",
            "URL": url,
            "Title": title,
            "LinkCount": links,
            "HeaderCount": headers
        }]
    except Exception as e:
        logger.error(f"Failed to scrape {url}: {e}")
        return [{"Source": "Web", "URL": url, "Error": str(e)}]
