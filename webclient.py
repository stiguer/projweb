

from urllib.request import urlopen
import bs4

class WebClient(object):
    """WebClient class"""
    def __init__(self):
        super(WebClient, self).__init__()

    def download_page(arg):
        # connect to the web site
        f = urlopen("https://www.banggood.com/es/Flashdeals.html")
        # get the download_page
        page = f.read()
        # close the connection
        f.close()
        return page

    def search_activities(self, page):
        tree = bs4.BeautifulSoup(page, "lxml")

        ul = tree.find("ul", "goodlist_1")
        li = ul.find_all("li")
        act_list = []

        for item in li:
            # process item
            price = item.find("span", "price").text
            title = item.find("span", "title").text
            act_list.append((title, price))
        return act_list


    def run(self):
        # download a web
        page = self.download_page()
        # search activities in web page
        data = self.search_activities(page)
        # print the activities
        print(data)

if __name__ == "__main__":
    c = WebClient()
    c.run()
