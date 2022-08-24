from bs4.element import Tag
import logging
class Toc():
    def __init__(self, base_url: str, idx:int) -> None:
        pass
        self.articles = []
    
class Article():
    def __init__(self, title: str, author: str, url: str, date: str) -> None:
        """_summary_

        Args:
            title (str): The title of the article
            author (str): The author of the article
            url (str): The url of the article
            date (str): The date of the article
        """
        self.author = author
        self.title =  title
        self.url =  url
        self.date = date

    
