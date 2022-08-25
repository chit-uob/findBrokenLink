import check_links

path = "data/TH300 Topic 2 Study Guide Spring Term 2022-23-incomplete.docx"

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
urls = list(set(urls))

# print(', '.join(urls))

for url in urls:
    is_valid = check_links.check_link(url)
    if is_valid:
        print("the above link should be valid")
    else:
        print("the program thinks the link is NOT VALID!")
