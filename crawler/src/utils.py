import logging
from bs4 import BeautifulSoup
from bs4.element import Tag
from typing import Dict, List, Tuple
from logging import Logger
import requests

PTT_PREFIX = "https://www.ptt.cc/"

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

def extract_article_tags(soup: BeautifulSoup) -> List[Tag]:
    """ Extract all article tags from the index page

    Args:
        soup (BeautifulSoup): BS4 soup object

    Returns:
        List[Tag]: A list that contains BS4 tags with article info.
    """
    return soup.find_all("div", "r-ent")

def extract_article_meta(bs4_tag: Tag) -> Dict:
    """Extract article meta data from bs4 tag that contains article info.

    Args:
        bs4_tag (Tag): Soup that contains PTT's info (soup.find_all("div", "r-ent"))

    Returns:
        Dict:  author, title, url, date
    """
    try:
        author = bs4_tag.find("div","author").text
        title =  bs4_tag.find("div", "title").a.text
        url =  bs4_tag.find("div", "title").a['href']
        date = bs4_tag.find("div","date").text
        return {
            "author": author,
            "title": title,
            "url": url,
            "date": date
        }
    except AttributeError as e:
        logging.error(e)
        logging.error(bs4_tag)

def get_logger(file_name: str) -> Logger:
    """Create logger object

    Args:
        file_name (str): Current file name
    Returns:
        Logger: logging.Logger object
    """
    console_handler = logging.StreamHandler()
    console_format = logging.Formatter(
        '%(asctime)s - %(module)s - %(levelname)s - %(message)s'
    )

    console_handler.setFormatter(console_format)

    logger = Logger(file_name)
    logger.addHandler(console_handler)
    return logger