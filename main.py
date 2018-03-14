from queue import Queue
from crawler import Crawler
from domain import *
from basic import *
import threading

PROJECT_NAME = 'tutorialspoint'
HOMEPAGE = 'https://www.tutorialspoint.com'
DOMAIN = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
VISITED_FILE = PROJECT_NAME + '/visited.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Crawler(PROJECT_NAME, HOMEPAGE, DOMAIN)


# create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# job for thread to crawl the next page in queue
def work():
    while True:
        url = queue.get()
        Crawler.visit_page(threading.current_thread().getName(), url)
        queue.task_done()


# for each link in queue file, add them to thread queue to be processed
def create_job():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# check if there is more links in queue file, if so create jobs to crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_job()


create_workers()
crawl()