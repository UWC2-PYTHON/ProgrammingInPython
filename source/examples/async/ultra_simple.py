#!/usr/bin/env python

"""
Ultra Simple async example
"""

import asyncio


async def say_lots(num):
    for i in range(num):
        print(f'This was run by the loop ({i}) :')
        await asyncio.sleep(1.0)


asyncio.run(say_lots(5))
print("done with loop")
