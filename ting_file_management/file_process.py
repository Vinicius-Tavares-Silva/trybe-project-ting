import sys
from .file_management import txt_importer


def process(path_file, instance):
    for index in range(len(instance)):
        read_file = instance.search(index)
        if read_file['nome_do_arquivo'] == path_file:
            return None

    news = txt_importer(path_file)
    output = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(news),
        'linhas_do_arquivo': news
    }
    instance.enqueue(output)
    print(str(output), file=sys.stdout)


def remove(instance):
    if len(instance) > 0:
        file = instance.dequeue()
        file_name = file['nome_do_arquivo']
        output = f'Arquivo {file_name} removido com sucesso'
    else:
        output = 'Não há elementos'

    print(str(output), file=sys.stdout)


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(str(file), file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
