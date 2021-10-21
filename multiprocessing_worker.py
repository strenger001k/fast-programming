from multiprocessing import Pool
from process_file import replace_symbol


def process_file(filename):
    with open(filename, 'r+') as f:
        content = f.read()
        text = replace_symbol(content)
        f.seek(0)
        f.write(''.join(text))
        print(filename)


def main_multiprocessing():
    with Pool(5) as p:
        p.map(process_file, ([(f"{i}.txt") for i in range(1, 11)]))
        for j in range(11, 100, 10):
            p.map(process_file, ([(f"{i}.txt") for i in range(j, j+10)]))


def start_multiprocessing():
    print("multiprocessing")
    main_multiprocessing()
