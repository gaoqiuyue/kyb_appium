import csv


def get_csv_data(csv_file, line):
    # 获取指定行数据
    with open(csv_file, 'r', encoding='utf-8')as fp:
        reader = csv.reader(fp)
        for index, row in (enumerate(reader, 1)):
            if index == line:
                return row

if __name__ == '__main__':
    csv_file = '../data/kybaccount.csv'
    data = get_csv_data(csv_file, 3)
    print(data)
    print(data[0])

