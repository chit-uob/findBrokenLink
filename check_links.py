import requests
from urllib import parse



def check_link(url):

    print(f"checking {url}")

    # Try and see if url have inherit problem
    try:
        response = requests.get(url)
    except:
        return False

    # See if not 200
    if not response.status_code == 200:
        return False

    return True

