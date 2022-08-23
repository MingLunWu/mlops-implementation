from bs4.element import Tag
import logging
class Toc():
    def __init__(self, base_url: str, idx:int) -> None:
        pass
        self.articles = []
    
class Article():
    def __init__(self, bs4_tag: Tag) -> None:
        """_summary_

        Args:
            bs4_tag (Tag): bs4 tag (soup.find_all("div", "r-ent"))
        """
        try:
            self.author = bs4_tag.find("div","author").text
            self.title =  bs4_tag.find("div", "title").a.text
            self.url =  bs4_tag.find("div", "title").a['href']
            self.date = bs4_tag.find("div","date").text
        except AttributeError as e:
            logging.error(e)
            logging.error(bs4_tag.prettify())

    
