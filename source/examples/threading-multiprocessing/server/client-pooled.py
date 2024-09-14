#!/usr/bin/env python

from multiprocessing.pool import ThreadPool
import urllib.request
import urllib.error
import urllib.parse
from decorators import timer


url = "http://localhost:37337"


def worker(*args):
    conn = urllib.request.urlopen(url)
    result = conn.read()
    conn.close()
    print(result)


@timer
def threading_client(number_of_requests=10, thread_count=2):
    pool = ThreadPool(processes=thread_count)
    pool.map(worker, list(range(number_of_requests)))


if __name__ == "__main__":
    number_of_requests = 100
    thread_count = 10
    threading_client(number_of_requests=number_of_requests,
                     thread_count=thread_count)
