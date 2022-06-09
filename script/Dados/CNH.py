def cnh(cnh):
    categoria = 'A','B','C','D','E','AB','AC','AD','AE'
    while True:
        cnh3 = ''
        print('-' * 30)
        cnh1 = str(input('Você tem Carteira Nacional de Habilitação (CNH), [S/N]: ')).strip().upper()[0]
        if cnh1 == 'S':
            while True:
                print('-' * 30)
                cnh2 = str(input('Informe quias categoria você têm, (A), (B), (C), (D), (E), ou (A+B,C,D,E): ')).strip().upper()
                if cnh2 in categoria:
                    print('-' * 30)
                    cnh3 = str(input(f'Posso confirmar a categoria {cnh2}, [S/N]: ')).strip().upper()[0]
                    if cnh3 == 'S':
                        cnh = cnh2
                        break
                    elif cnh3 == 'N':
                        break
                    else:
                        print('-' * 30)
                        print('Valor incorreto!')
                else:
                    print('-' * 30)
                    print('Categoria incorreto!')
        elif cnh1 == 'N':
            cnh = 'Não possuo CNH'
            break
        else:
            print('-' * 30)
            print('Valor incorreto!')
        if cnh3 == 'S':
            break
    return cnh
#cnh('')
