import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in range(instance.__len__()):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return

    file_imported = txt_importer(path_file)

    data = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(file_imported),
        'linhas_do_arquivo': file_imported
    }

    instance.enqueue(data)

    sys.stdout.write(f'{data}')


def remove(instance):
    if instance.__len__() == 0:
        sys.stdout.write('Não há elementos\n')
    else:
        file = instance.dequeue()

        sys.stdout.write(f'''
            Arquivo {file['nome_do_arquivo']} removido com sucesso\n
        ''')


def file_metadata(instance, position):
    try:
        file = instance.search(position)

        sys.stdout.write(f'{file}')
    except IndexError:
        sys.stderr.write('Posição inválida\n')
