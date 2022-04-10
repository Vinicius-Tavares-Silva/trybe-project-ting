import sys


def txt_importer(path_file):
    try:
        if path_file.endswith('.txt'):
            news = read_txt_file(path_file)
            return news
        else:
            print('Formato inválido', file=sys.stderr)
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)


def read_txt_file(path_file):
    file = open(path_file, 'r')
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]
    return lines
