import requests
from bs4 import BeautifulSoup


class Site:
    def __init__(self, url:str, parent):
        self.url = url
        self.parent = parent
        self.link_sites = []
        self.update_level()

    def parse_links(self):
        r = requests.get(url=self.url)
        soup = BeautifulSoup(r.content, "lxml")
        links = []
        for a in soup.find_all('a', href=True):
            if a['href'][0:8] == 'https://':
                links.append(a['href'])
        return links[0:10]


    def update_level(self):
        if self.parent:
            self.level = self.parent.level + 1
        else:
            self.level = 0

def get_links(url:str, n:int):
    root = Site(url, None)

    def get_links_helper(site:Site):
        if site.level == n:
            return
        for link in site.parse_links():
            cur_site = Site(link, site)
            get_links_helper(cur_site)
            site.link_sites.append(cur_site)
    get_links_helper(root)
    return root


def pretty_print_Graph(root:Site):
    print(root.url)
    for l in root.link_sites:
        pretty_print_Graph(l)


if __name__ == '__main__':
    root = get_links('https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic', 3)
    pretty_print_Graph(root)