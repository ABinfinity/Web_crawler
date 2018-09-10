import threading 
from queue import Queue
from spider import Spider
from domain import *
from webc import *


PROJECT_NAME = "thenewboston" # python convention for declaring constant (all capitals)
HOMEPAGE = "https://thenewboston.com/"
DOMAIN_NAME = get_domain_name(HOMEPAGE)

QUEUE_FILE = PROJECT_NAME + "/queue.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawled.txt"
NUMBER_OF_THREADS = 4

queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# create worker threads(will die when main exits)
def create_workers():
	for _ in range(NUMBER_OF_THREADS): #when we just want it to go through the loops and nothing to do with numbers
		t = threading.Thread(target = work)
		t.daemon = True
		t.start()



# do the next job in the queue
def work():
	while True:
		url = queue.get()
		Spider.crawl_page(threading.current_thread().name, url)
		queue.task_done()


# each queued link is the new job
def create_jobs():
	for link in file_to_set(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()



#check if there are items in the queue, if so then crawl
def crawl():
	queued_links = file_to_set(QUEUE_FILE)
	if len(queued_links)>0:
		print(str(len(queued_links)) + " links in the queue")
		create_jobs()



create_workers()
crawl()