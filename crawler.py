import requests
import urllib.parse
from basic import *
from bs4 import BeautifulSoup


class Crawler:
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    visited_file = ''
    queue = set()
    visited = set()

    # variable initialization
    def __init__(self, project_name, base_url, domain_name):
        Crawler.project_name = project_name
        Crawler.base_url = base_url
        Crawler.domain_name = domain_name
        Crawler.queue_file = project_name + '/queue.txt'
        Crawler.visited_file = project_name + '/visited.txt'
        self.boot()
        self.visit_page('first spider', Crawler.base_url)

    # create new directory with queue and visited file then read them to a set
    @staticmethod
    def boot():
        create_project_dir(Crawler.project_name)
        create_data_files(Crawler.project_name, Crawler.base_url)
        Crawler.queue = file_to_set(Crawler.queue_file)
        Crawler.visited = file_to_set(Crawler.visited_file)

    # read a link from queue, parse link and request page, then parse html of page to get all links from page
    @staticmethod
    def visit_page(thread_name, page_url):
        if page_url not in Crawler.visited:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue waiting: ' + str(len(Crawler.queue)) + ' | Crawled: ' + str(len(Crawler.visited)))
            Crawler.add_links_to_queue(Crawler.gather_links(page_url))
            Crawler.queue.remove(page_url)
            Crawler.visited.add(page_url)
            Crawler.update_files()

    # request a page, then parse through response html to gather all links
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        urls = set()
        try:
            response = requests.get(page_url)
            if 'text/html' in response.headers['Content-Type']:
                html_string = response.text  # .text returns html as a string
            parser = BeautifulSoup(html_string, 'html.parser')
            for link in parser.find_all('a'):
                url = urllib.parse.urljoin(Crawler.base_url, link.get('href'))
                urls.add(url)
        except Exception as e:
            print(type(e))
            print(e)
            print('Error: Cannot crawl page: ' + page_url)
            return set()
        return urls

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Crawler.queue:
                continue
            if url in Crawler.visited:
                continue
            if Crawler.domain_name not in urllib.parse.urlparse(url).netloc:
                continue
            Crawler.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Crawler.queue, Crawler.queue_file)
        set_to_file(Crawler.visited, Crawler.visited_file)
