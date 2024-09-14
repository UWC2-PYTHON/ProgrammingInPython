#!/usr/bin/env python3

# TODO: update this with async / await

import asyncio
from urllib.request import urlopen
from decorators import timer


results = asyncio.Queue()
url = "http://localhost:37337"


async def producer():
    conn = urlopen(url)
    result = conn.read()
    return result


async def worker():
    result = await producer()
    results.put(result)


@timer
def threading_client(number_of_requests=10):
    loop = asyncio.new_event_loop()

    for i in range(number_of_requests):
        loop.run_until_complete(worker())

    print("made %d requests" % number_of_requests)


if __name__ == "__main__":
    number_of_requests = 100
    threading_client(number_of_requests=number_of_requests)
