This is a multithreading web crawler written in python using requests and beautifulSoup python modules.

main.py - driver, creates threads and run jobs.

basic.py - support methods that handles reading and writing to files

crawler.py - methods that requests webpage and process html live here

domain.py - process a url and get returns the domain url

The program creates a new directory with a queue.txt and a visited.txt, queue.txt stores links that needs to be crawl, visited.txt stores links that has been visited.


