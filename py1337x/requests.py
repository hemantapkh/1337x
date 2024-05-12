import requests

def send_requests(url, method='GET', flare_solver=False):
    if flare_solver:
        requests.request(method, url)