def endereço(endereço):
    endereço = ''
    while True: # Coletar dados de endereço
        while True: # Nome da Rua
            print('-' * 30)
            nome_rua = str(input('Informe o nome da Rua: ')).strip().title()
            while True:
                print('-' * 30)
                nome_rua_confirma = str(input(f'Posso confirmar esse endereço Rua, {nome_rua}\n[S/N] Digite aqui: ')).strip().upper()[0]
                if nome_rua_confirma == 'S':
                    break
                elif nome_rua_confirma == 'N':
                    print('-' * 30)
                    print('Por favor, informe o novo nome da Rua!')
                    break
                else:
                    print('-' * 30)
                    print('Valor incorreto!')
            if nome_rua_confirma == 'S':
                break 
        while True: # Número da casa
            while True:
                print('-' * 30)
                número_casa = str(input('Informe o número da casa: ')).strip()
                if número_casa.isnumeric() == True:
                    número_casa = int(número_casa)
                    break
                else:
                    print('-' * 30)
                    print('Valor incorreto, apenas números!')         
            while True:
                print('-' * 30)
                número_casa_confirma = str(input(f'Posso confirmar o N°{número_casa}, [S/N]: ')).strip().upper()[0]
                if número_casa_confirma == 'S':
                    break
                elif número_casa_confirma == 'N':
                    print('-' * 30)
                    print('Por favor, informe o novo número!')
                    break
                else:
                    print('-' * 30)
                    print('Valor incorreto!')
            if número_casa_confirma == 'S':
                break
        while True: # Nome da cidade
            print('-' * 30)
            nome_cidade = str(input('Informe o nome da cidade: ')).strip().title()
            print('-' * 30)
            while True:
                nome_cidade_confirma = str(input(f'Posso confirmar o nome da cidade {nome_cidade}, [S/N]: ')).strip().upper()[0]
                if nome_cidade_confirma == 'S':
                    break
                elif nome_cidade_confirma == 'N':
                    print('-' * 30)
                    print('Por favor, informe o novo nome da cidade!')
                    break
                else:
                    print('-' * 30)
                    print('Valor incorreto!')
            if nome_cidade_confirma == 'S':
                break
        while True: # Nome do estado
            print('-' * 30)
            nome_estado = str(input('Informe o nome do estado: ')).strip().title()
            print('-' * 30)
            while True:
                nome_estado_confirma = str(input(f'Posso confirmar o nome do estado {nome_estado}, [S/N]: ')).strip().upper()[0]
                if nome_estado_confirma == 'S':
                    break
                elif nome_estado_confirma == 'N':
                    print('-' * 30)
                    print('Por favor, informe o nome do novo estado!')
                    break
                else:
                    print('-' * 30)
                    print('Valor incorreto!')
            if nome_estado_confirma == 'S':
                break
        endereço += f'Rua:{nome_rua}, N°:{número_casa}, Cidade:{nome_cidade}, Estado:{nome_estado}'
        break
    return endereço
