def ensino_médio(a):
    info1 = '', 'não cursa/terminou', 'cursando', 'concluído'
    ensino_médio = ''
    while True:
        while True: # Primeira pergunta sobre o ensino médio
            print('-' * 30)
            médio = str(input('\033[2;32mSobre o Ensino médio\033[m, [1] não cursa/terminou, [2] está cursando mas não terminou, [3] concluído: '))
            médio_confirma = ''
            if médio.isnumeric() == True and médio == '1' or médio == '2' or médio == '3':
                médio = int(médio)
                while True:
                    print('-' * 30)
                    médio_confirma = str(input(f'Posso confirmar para {info1[médio]}, [S/N]: ')).strip().upper()[0]
                    if médio_confirma == 'S':
                        break
                    elif médio_confirma == 'N':
                        break
                    else:
                        print('-' * 30)
                        print('Valor incorreto!')
            else:
                print('-' * 30)
                print('Valor incorreto, apenas número de 1 a 3!')
            if médio_confirma == 'S': # Para passar para a proxima etapa
                break
        a # Retorna uma opção
        if a == '':
            if médio == 1 or médio == 2:
                ensino_médio += f'{info1[médio]}\n'
                ensino_médio += 'Ensino Superior:Ensino Médio incompleto'
            elif médio == 3:
                ensino_médio += f'{info1[médio]}'
        elif a == 1:
            if médio == 1 or médio == 2:
                ensino_médio += f'{info1[médio]}'
            elif médio == 3:
                ensino_médio += f'{info1[médio]}'
        break
    return ensino_médio
#ensino_médio()
