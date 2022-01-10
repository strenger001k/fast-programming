import time
from asyncio_worker import start_asyncio
from multiprocessing_worker import start_multiprocessing
from thread_worker import start_thread
from create_txt import reload


def timer(method):
    def get():
        print("RESET")
        reload()
        start = time.time()
        function = method()
        print("time: %f" % (time.time()-start))
        return function
    return get


@timer
def asyncio():
    start_asyncio()


@timer
def multiprocessing():
    start_multiprocessing()


@timer
def thread():
    start_thread()


if __name__ == '__main__':
    asyncio()  # асинхронно

    multiprocessing()  # многопроцессорно

    thread()  # многопоточно
