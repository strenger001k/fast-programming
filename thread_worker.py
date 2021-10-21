from concurrent.futures import ThreadPoolExecutor
from process_file import replace_symbol


def process_file(filename):
    with open(filename, 'r+') as f:
        content = f.read()
        text = replace_symbol(content)
        f.seek(0)
        f.write(''.join(text))
        print(filename)


def main_thread():
    with ThreadPoolExecutor(max_workers=5) as th:
        th.map(process_file, ([(f"{i}.txt") for i in range(1, 11)]))
        for j in range(11, 100, 10):
            th.map(process_file, ([(f"{i}.txt") for i in range(j, j+10)]))


def start_thread():
    print("threadpool")
    main_thread()
