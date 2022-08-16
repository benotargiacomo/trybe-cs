def exists_word(word, instance):
    occurrences = []

    for index in range(instance.__len__()):
        for line_index, line in enumerate(
                instance.search(index)['linhas_do_arquivo']):
            if word.lower() in line.lower():
                if len(occurrences) > 0:
                    occurrences[-1]['ocorrencias'].append(
                        {'linha': line_index + 1}
                    )
                else:
                    occurrences.append({
                        'palavra': word,
                        'arquivo': instance.search(index)['nome_do_arquivo'],
                        'ocorrencias': [{'linha': line_index + 1}],
                    })

    return occurrences


def search_by_word(word, instance):
    occurrences = []

    for index in range(instance.__len__()):
        for line_index, line in enumerate(
                instance.search(index)['linhas_do_arquivo']):
            if word.lower() in line.lower():
                if len(occurrences) > 0:
                    occurrences[-1]['ocorrencias'].append(
                        {'linha': line_index + 1, 'conteudo': line}
                    )
                else:
                    occurrences.append({
                        'palavra': word,
                        'arquivo': instance.search(index)['nome_do_arquivo'],
                        'ocorrencias': [
                            {'linha': line_index + 1, 'conteudo': line}
                        ],
                    })

    return occurrences
