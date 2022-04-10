def exists_word(word, instance):
    output = []
    for index in range(len(instance)):
        found_at = []
        read_file = instance.search(index)
        for index, line in enumerate(read_file['linhas_do_arquivo']):
            if word.casefold() in line.casefold():
                found_at.append({'linha': index + 1})
        if len(found_at) > 0:
            output.append({
                'palavra': word,
                'arquivo': read_file['nome_do_arquivo'],
                'ocorrencias': found_at
            })
    return output


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
