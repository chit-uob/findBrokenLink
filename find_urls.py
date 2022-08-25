import time

import check_links

path = "C:/Users/User/Desktop/CS100 Topic 1 Study Guide Summer Term 2022-23-final.docx"

import use_docx2python

s = use_docx2python.get_text_by_docx2python(path)

from urlextract import URLExtract

urlextracter = URLExtract()
urls = urlextracter.gen_urls(s)

import re


def formaturl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return 'http://{}'.format(url)
    return url


urls = [formaturl(url) for url in urls]
urls = sorted(list(set(urls)))


WELCOME_TEXT = """
Welcome to the link extractor

This program tests the links and see if the response code is 200, if not, the program reports the links.

This program may be inaccurate because of the following two reasons:

False positive:
1. Links may return 200 code, but the actually content is wrong

False negative:
1. Links may not return 200 code, maybe it is 300 code for you were redirected, but it might be the correct place
"""
print(WELCOME_TEXT)
print(f"We are checking {path}\n")
start_time = time.time()

for url in urls:
    is_valid = check_links.check_link(url)
    if is_valid:
        print("the above link should be valid")
    else:
        print("the program thinks the link is NOT VALID!")

duration = time.time() - start_time
print(f"\nChecked {len(urls)} links in {duration} seconds")
