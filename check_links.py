import requests
from urllib import parse

global_counter = 1

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}


def check_link(url):
    global global_counter

    print(f"{global_counter}: checking {url}")
    global_counter += 1

    # Try and see if url have inherit problem
    try:
        response = requests.get(url, headers=HEADERS, stream=True)
    except:
        print("try failed")
        return False

    # See if not 200
    if not response.status_code == 200:
        print(f"the response code was actually {response.status_code}")
        return False

    return True
