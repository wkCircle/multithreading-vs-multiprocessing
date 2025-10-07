import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

urls = ['http://www.discovertunisia.com',
        'https://www.youtube.com/watch?v=sHORcz5nqIc',
        'https://www.youtube.com/watch?v=dyHjCwKoNn8',
        'http://www.discovertunisia.com',
        'https://www.youtube.com/watch?v=sHORcz5nqIc',
        'https://www.youtube.com/watch?v=dyHjCwKoNn8',
        ]


def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)


def multiprocessing(func, args, workers):
    with ProcessPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)


def load_url(x):
    # print('I am', x)
    with urllib.request.urlopen(urls[x], timeout=20) as conn:
        return conn.read()

if __name__ == "__main__":
    n_jobs = len(urls)

    marker = time.time()
    for i in range(n_jobs):
        load_url(i)
    print("Serial spent", time.time() - marker)
    for n_threads in [4, 8, 16]:
        marker = time.time()
        multithreading(load_url, range(n_jobs), n_threads)
        print("Multithreading {} spent".format(n_threads), time.time() - marker)


    marker = time.time()
    for i in range(n_jobs):
        load_url(i)
    print("Serial spent", time.time() - marker)
    for n_threads in [4, 8, 16]:
        marker = time.time()
        multiprocessing(load_url, range(n_jobs), n_threads)
        print("Multiprocessing {} spent".format(n_threads), time.time() - marker)

