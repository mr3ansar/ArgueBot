import requests
from bs4 import BeautifulSoup

def extract_content(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        content = " ".join([p.get_text() for p in paragraphs])
        print(f"Scraped Content: {content[:500]}...")  # Print first 500 characters for debugging
        return content
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None