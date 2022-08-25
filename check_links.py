import requests
from urllib import parse


global_counter = 1


def check_link(url):
    global global_counter

    print(f"{global_counter}: checking {url}")
    global_counter += 1

    # Try and see if url have inherit problem
    try:
        response = requests.get(url)
    except:
        return False

    # See if not 200
    if not response.status_code == 200:
        return False

    return True

