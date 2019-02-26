

from urllib.request import urlopen
import bs4
import xmltodict
import pprint

class WebClient(object):
    """WebClient class"""
    def __init__(self):
        super(WebClient, self).__init__()

    def download_page(arg):
        # connect to the web site
        f = urlopen("https://api.openweathermap.org/data/2.5/weather?q=LLeida,es&appid=0c5943338e78117b61d5a9249ba17b82&mode=xml&unit=metric")
        # get the download_page
        page = f.read()
        # close the connection
        f.close()
        return page

    #def search_activities(self, page):
    #    tree = bs4.BeautifulSoup(page, "lxml")
    #
    #    ul = tree.find("ul", "goodlist_1")
    #    li = ul.find_all("li")
    #    act_list = []

    #    for item in li:
            # process item
    #        price = item.find("span", "price").text
    #        title = item.find("span", "title").text
    #        act_list.append((title, price))
    #    return act_list

    def search_activities(self, page):
        xml = xmltodict.parse(page)
        pprint.pprint(xml)
        temp = xml['current']['temperature']['@value']
        weather = xml['current']['weather']['@value']
        return temp+" and "+weather


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
