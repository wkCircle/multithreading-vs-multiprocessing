# gil.py
# Adapt script from https://www.youtube.com/watch?v=mvxR6_G4yLQ by 2MinutesPy as some code no longer works

import sys
import math
import time
import threading
import multiprocessing


def compute_factorial(n):
    return math.factorial(n)


def single_threaded_compute(n):
    for num in n:
        compute_factorial(num)
    print("Single-threaded Factorial Computed.")


def multi_threaded_compute(n):
    threads = []
    # create 5 threads
    for num in n:
        thread = threading.Thread(target=compute_factorial, args=(num,))
        threads.append(thread)
        thread.start()
    
    # wait for all threads to complete
    for thread in threads:
        thread.join()
    print("Multi-threaded Factorial Computed.")


def multi_processing_compute(n):
    processes = []
    # create a process for each number in the list
    for num in n:
        process = multiprocessing.Process(target=compute_factorial, args=(num,))
        processes.append(process)
        process.start()
    
    # wait for all processes to complete
    for process in processes:
        process.join()
    print("Multi-processing Factorial Computed.")


def main():
    # checking version
    print("sys info:")
    print(sys.version)
    print(sys.version_info)

    # GIL status
    # original code: import sysconfig; sysconfig.get_config_var("Py_GIL_DISABLED")  --- no longer works
    status = sys._is_gil_enabled()  # only works since python 3.13+
    if status:
        print("Running in GIL mode 🔒")
    else:
        print("Running in NO-GIL mode 🧵")

    numlist = [100000, 200000, 300000, 400000, 500000]

    # single-threaded execution
    start = time.time()
    single_threaded_compute(numlist)
    end = time.time() - start
    print(f"Single-threaded time taken : {end:.2f} seconds")

    # multi-threaded execution
    start = time.time()
    multi_threaded_compute(numlist)
    end = time.time() - start
    print(f"Multi-threaded time taken : {end:.2f} seconds")

    # multi-process execution
    start = time.time()
    multi_processing_compute(numlist)
    end = time.time() - start
    print(f"Multi-process time taken : {end:.2f} seconds")

if __name__ == "__main__":
    main()

