def nacionalidade(nacionalidade):
    while True: # Coletar dados de nacionalidade
        print('-' * 30)
        nacionalidade = str(input(f'Informe a sua nacionalidade: ')).strip().title()
        while True:
            print('-' * 30)
            nacionalidade_confirmar = str(input(f'Posso confirmar para {nacionalidade}, [S/N]: ')).strip().upper()[0]
            if nacionalidade_confirmar == 'S':
                break
            elif nacionalidade_confirmar == 'N':
                print('-' * 30)
                print(f'Por favor, informe a nova nacionalidade!')
                break
            else:
                print('-' * 30)
                print('Valor incorreto!')
        if nacionalidade_confirmar == 'S':
            break
    return nacionalidade