from multiprocessing import Pool


def process_file(filename):
    with open(filename, 'r+') as f:
        content = f.read()
        text = list(content)
        for i in range(len(text)):
            if (i+1) % 5 == 0:
                text[i] = "*"
        f.seek(0)
        f.write(''.join(text))


def main():
    with Pool(5) as p:
        p.map(process_file, ([(f"{i}.txt") for i in range(1, 11)]))
        for j in range(11, 100, 10):
            p.map(process_file, ([(f"{i}.txt") for i in range(j, j+10)]))


def start():
    print("multiprocessing")
    main()
