import requests

r = requests.get("https://www.thegospelcoalition.org/essay/liberation-theology/")

print(r.status_code)