def informações_adicionais(info_adicional):
    info_adicional = ''
    while True: # Coletar dados de informações adicionais
        print('-' * 30)
        info_adicional0 = str(input('Gostaria de adicionar alguma informação adicional: [S/N]: ')).strip().upper()[0]
        if info_adicional0 == 'S':
            while True: # while de segurança
                while True:
                    print('-' * 30)
                    print('Escreva a informação adicional')
                    info_adicional1 = str(input('Digite aqui: ')).strip()
                    while True:
                        print('-' * 30)
                        print('Posso confirmar esta informação: ',end='')
                        print(f'{info_adicional1}')
                        print('-' * 30)
                        info_adicional1_confirma = str(input(f'Digite aqui [S/N]: ')).strip().upper()[0]
                        if info_adicional1_confirma == 'S':
                            break
                        elif info_adicional1_confirma == 'N':
                            print('-' * 30)
                            print('Por favor, informe o nova informação adicional!')
                            break
                        else:
                            print('-' * 30)
                            print('Valor incorreto!')
                    if info_adicional1_confirma == 'S':
                        break
                while True: # Pergunta ao usuário se quer adicionar mais uma informação
                    info_adicional += f'Ponto:{info_adicional1};'
                    print('-' * 30)
                    adicionar_info_adicional = str(input('Gostaria de adicionar mais uma informação adicional, [S/N]: ')).strip().upper()[0]
                    if adicionar_info_adicional == 'S':
                        break
                    elif adicionar_info_adicional == 'N':
                        break
                    else:
                        print('-' * 30)
                        print('Valor incorreto!')
                if adicionar_info_adicional == 'N':
                    break
        elif info_adicional0 == 'N':
            info_adicional = 'Nenhuma'
            break
        else:
            print('-' * 30)
            print('Valor incorreto!')
        if info_adicional0 in 'SN':
            break
    return info_adicional
