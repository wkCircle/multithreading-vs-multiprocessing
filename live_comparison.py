import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import matplotlib.pyplot as plt
import numpy as np


def multithreading(func, args, workers):
    with ThreadPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)


def multiprocessing(func, args, workers):
    with ProcessPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)


def live_tracker(x):
    reference = time.time()
    l = []
    for i in range(10**6):
        l.append(time.time() - reference)
    return l


def visualize_live_runtimes(results, title):
    for i, exp in enumerate(results):
        print(i)
        plt.scatter(exp, np.ones(len(exp)) * i, alpha=0.8, c='red', edgecolors='none', s=1)

    plt.grid(axis='x')
    plt.ylabel("Tasks")
    ytks = range(len(results))
    plt.yticks(ytks, ['job {}'.format(exp) for exp in ytks])
    plt.xlabel("Seconds")
    plt.title(title)
    # Set finer x-axis ticks
    xmin, xmax = plt.xlim()
    plt.xticks(np.arange(0, xmax, 0.01))


if __name__ == "__main__":
    fig, axs = plt.subplots(2, 1, sharex=True)
    plt.sca(axs[0])
    visualize_live_runtimes(multithreading(live_tracker, range(4), 4), "Multithreading")
    plt.sca(axs[1])
    visualize_live_runtimes(multiprocessing(live_tracker, range(4), 4), "Multiprocessing")
    plt.show()

