import time
import asyncio
import datetime
import requests
import json

def calc_time(fn):
    """decorator that measures the execution time of a function"""
    def wrapper(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print(f"[{fn.__name__}] elapsed time: {end - start}")
        return
    return wrapper

def make_request(url, headers):
    return requests.get(url=url, headers=headers)

async def get_request (url):
    headers = {'Accept': 'application/json'}
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, make_request, url, headers)
    print(response.json()['joke'])


@calc_time
def main_async():
    # Schedule the first call to get_joke()
    loop = asyncio.get_event_loop()
    tasks = asyncio.gather(
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
            get_request('https://icanhazdadjoke.com/'),
        )
    results = loop.run_until_complete(tasks)
    return results

if __name__ == "__main__":
    main_async()
