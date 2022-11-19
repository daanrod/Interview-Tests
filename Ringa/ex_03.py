### Retornar quantas vezes a letra se repete em um bloco de strings
### Filtrar as strings para somente letras
### Se o numero de repetição for maior que 9, deverá reocmeçar a conta
### Exemplo: 'AAAAAAAAAAAA' return '9A3A' serão 12 'A' no total



def func(strings):
    clean_list = []
    list_complete = []
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    current_string = ''
    count = 0

    for n in strings:
        if n in abc:
            clean_list.append(n)

    clean_strings = ''.join(clean_list)

    while clean_strings != '':
        current_string = clean_strings[0]
        count = clean_strings.count(current_string)
        clean_strings = clean_strings.replace(current_string, '')

        if count > 9:
            rest = count % 9
            count = 9
            list_complete.append(f'{count}{current_string}')
            count = rest
            list_complete.append(f'{count}{current_string}')
            count = 0
        else:
            list_complete.append(f'{count}{current_string}')
            count = 0

    return str(''.join(list_complete))


if __name__ == '__main__':
    func('AAAAAAAAAAAAAB~]aweq123BbCCC')
    print(func('AAAAAAAAAAAAAB~]aweq123BbCCC'))