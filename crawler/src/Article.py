import logging
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
        self._extract_push_comments()
        print("test")

    def _extract_push_comments(self) -> None:
        successed, failed = 0, 0
        for tag in self._soup.find_all("div", "push"):
            try:
                author = tag.find("span", "push-userid").text
                content = tag.find("span", "push-content").text[2:] # The first two characters are ": "
                date = tag.find("span", "push-ipdatetime").text
                status = "push"
                comment_obj = Comment(
                    author=author,
                    status=status,
                    content=content,
                    date=date
                )
                self.comments.append(comment_obj)
                tag.decompose()
                successed += 1
            except Exception as e:
                logging.error(e)
                tag.decompose()
                failed += 1

        logging.info(f"{successed} comments (push) has been successfully extracted, {failed} has been failed.")

class Comment:
    def __init__(self, author: str, status: str, content: str, date: str) -> None:
        self.author = author
        self.status = status
        self.content = content
        self.date = date

    
