from bs4 import BeautifulSoup
from bs4.element import Tag
from typing import List
import requests

def create_soup(url: str) -> BeautifulSoup:
    """ Create bs4 obj from url

    Args:
        url (str): url

    Returns:
        BeautifulSoup: bs4 object
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def extract_article_tag(soup: BeautifulSoup) -> List[Tag]:
    return soup.find_all("div", "r-ent")