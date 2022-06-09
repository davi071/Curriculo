def idade(idade):
    while True:
        print('-' * 30)
        idade = str(input('Qual a sua idade: ')).strip()
        if idade.isnumeric() == True:
            while True:
                print('-' * 30)
                idade_confirma = str(input(f'Posso confirmar {idade} Anos, [S/N]')).strip().upper()[0]
                if idade_confirma == 'S':
                    break
                elif idade_confirma == 'N':
                    break
                else:
                    print('-' * 30)
                    print('Valor Incorreto!')
        else:
            print('-' * 30)
            print('Valor incorreto, apenas números!')
        if idade_confirma == 'S':
            break
    return idade
