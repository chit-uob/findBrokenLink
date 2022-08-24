import re

with open('data/CS100 Topic 1 Study Guide Summer Term 2022-23-final.txt', 'r', encoding='utf-8') as f:
    s = f.read()

# print(s)

urls = re.findall("(https?://\S+)", s)
print(', '.join(urls))