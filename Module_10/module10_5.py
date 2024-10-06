import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break
    return all_data


if __name__ == '__main__':
    list_file = 'file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt'

    start = datetime.datetime.now()
    for i in list_file:
        read_info(i)
    end = datetime.datetime.now()

    print(f'Время, затраченное на линейный процесс: {end - start}')

    start_2 = datetime.datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, list_file)
    end_2 = datetime.datetime.now()

    print(f'Время, затраченное на многопроцессный подход: {end_2 - start_2}')
