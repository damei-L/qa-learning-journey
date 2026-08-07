import time

import requests


def get_response_time(url):
    start = time.time()
    response = requests.get(url,timeout=10)
    end = time.time()
    duration = end - start
    return {
        "url": url,
        "start_code": response.status_code,
        "response_time": round(duration, 3)
    }

result = get_response_time("https://jsonplaceholder.typicode.com/posts/1")
print(result)
