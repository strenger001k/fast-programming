import time

import asyncio_worker, multiprocessing, thread_worker
import create_txt


def timer(method):
    def get():
        print("RESET")
        create_txt.reload()
        start = time.time()
        function = method()
        print("time: %f" % (time.time()-start))
        return function
    return get


@timer
def function1():
    asyncio_worker.start()


@timer
def function2():
    multiprocessing.start()


@timer
def function3():
    thread_worker.start()


if __name__ == '__main__':
    function1()  # асинхронно

    function2()  # многопроцессорно

    function3()  # многопоточно
