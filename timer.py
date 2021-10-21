import time

import main1, main2, main3
import create_txt


def timer(method):
    def get():
        start = time.time()
        function = method()
        print("time: %f" % (time.time()-start))
        return function

    return get


@timer
def function1():
    main1.start()


@timer
def function2():
    main2.start()


@timer
def function3():
    main3.start()


if __name__ == '__main__':
    print("RESET")
    create_txt.reload()
    function1()  # асинхронно

    print("RESET")
    create_txt.reload()
    function2()  # многопроцессорно

    print("RESET")
    create_txt.reload()
    function3()  # многопоточно
