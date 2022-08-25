import asyncio
import time
import aiohttp

import use_docx2python
from urlextract import URLExtract
import re
import json


path = "data/WP200 Topic 2 Study Guide Spring Term 2022-23-incomplete.docx"


HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}


WELCOME_TEXT = """
Welcome to the link extractor (async version)

This program tests the links and see if the response code is 200, if not, the program reports the links.

This program may be inaccurate because of the following two reasons:

False positive:
1. Links may return 200 code, but the actually content is wrong

False negative:
1. Links may not return 200 code, maybe it is 300 code for you were redirected, but it might be the correct place
"""


def formaturl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return 'http://{}'.format(url)
    return url


async def download_site(session, url):
    try:
        async with session.get(url, headers=HEADERS) as response:
            response_code = response.status
            print("-", end="")
            return response_code
    except:
        return False


async def download_all_sites(sites):
    # print("entered async")
    site_dict = {}
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        responses = await asyncio.gather(*tasks, return_exceptions=True)

        for url, status_code in zip(sites, responses):
            site_dict[url] = status_code

    print()
    for number, (url, status_code) in enumerate(sorted(site_dict.items())):
        print(f"{number + 1}:")
        print(url)
        if status_code == 200:
            print("the above link should be valid")
        else:
            if status_code == 404:
                reason = "status code is 404"
            else:
                reason = "something went wrong accessing this page"
            print(f"the program thinks the link is NOT VALID, because of {reason}")


def main():
    print(WELCOME_TEXT)
    print(f"We are checking {path}\n")
    s = use_docx2python.get_text_by_docx2python(path)
    extractor = URLExtract()
    urls = extractor.gen_urls(s)
    urls = [formaturl(url) for url in urls]
    sites = sorted(list(set(urls)))
    print("Progress")
    start_time = time.time()
    # print('before async')
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"\nChecked {len(sites)} links in {duration} seconds")


if __name__ == "__main__":
    main()