def telefone(telefone):
    while True: # Coletar dados de telefone
        while True:
            print('-' * 30)
            telefone = str(input('Informe o número do seu telefone com (DDD): ')).strip()
            if telefone.isnumeric() == True:
                #telefone = int(telefone)
                break
            else:
                print('-' * 30)
                print('Valor incorreto, apenas números!')
        while True:
            print('-' * 30)
            telefone_confirma = str(input(f'Posso confirmar esse número {telefone}, [S/N]: ')).strip().upper()[0]
            if telefone_confirma == 'S':
                break
            elif telefone_confirma == 'N':
                print('-' * 30)
                print(f'Por favor, informe o novo número!')
                break
            else:
                print('-' * 30)
                print('Valor incorreto!')
        if telefone_confirma == 'S':
            break
    return telefone
