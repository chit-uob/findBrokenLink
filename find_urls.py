from urlextract import URLExtract

with open('data/CS100 Topic 1 Study Guide Summer Term 2022-23-final.txt', 'r', encoding='utf-8') as f:
    s = f.read()

# print(s)

extractor = URLExtract()
urls = extractor.find_urls(s)
print(', '.join(urls))