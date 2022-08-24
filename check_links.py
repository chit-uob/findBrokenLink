import requests

def check_link(url):

    print(f"checking {url}")

    # Base case, 404 response
    try:
        response = requests.get(url)
    except:
        return False

    if response.status_code == 404:
        return False

    return True

