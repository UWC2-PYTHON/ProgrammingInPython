#!/usr/bin/env python

import urllib.request
import multiprocessing
from decorators import timer


results = multiprocessing.Queue()
url = "http://localhost:37337"


def worker(*args):
    conn = urllib.request.urlopen(url)
    result = conn.read()
    conn.close()
    results.put(result)


@timer
def threading_client(number_of_requests=10):
    for i in range(number_of_requests):
        proc = multiprocessing.Process(target=worker, args=())
        proc.start()
        print("Process %s started" % proc.name)

    for i in range(number_of_requests):
        print(results.get(timeout=2))

    print("made %d requests" % number_of_requests)


if __name__ == "__main__":
    number_of_requests = 100
    threading_client(number_of_requests=number_of_requests)
