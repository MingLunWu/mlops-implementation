from crawler.src.utils import create_soup, PTT_PREFIX
class Article:
    def __init__(self, title: str, author: str, url: str, date: str) -> None:
        """Constructor

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
        self.content = None
        self.comments = []
        
        self._soup = create_soup(PTT_PREFIX + self.url)

    def extract_comments(self) -> None:
        pass

class Comment:
    def __init__(self, author: str, status: str, content: str, date: str) -> None:
        self.author = author
        self.status = status
        self.content = content
        self.date = date

    
