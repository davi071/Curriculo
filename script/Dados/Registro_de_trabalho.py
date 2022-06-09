def registro_de_trabalho(registro_de_trabalho):
    registro_de_trabalho = ''
    while True: # while de segurança
        while True: # Pergunta se já foi registrado alguma vez
            print('-' * 30)
            registro = str(input('Informe se tem registro de trabalho na carteira, [S/N]: ')).strip().upper()[0]
            if registro == 'S':
                registro = 'tenho'
                break
            elif registro == 'N':
                registro = 'não tenho'
                break
        if registro == 'tenho':
            while True: # Pergunta a quantidade de registros
                print('-' * 30)
                rt1 = str(input('Informe quantos registros você têm, contando o atual se estiver trabalhando: ')).strip()
                if rt1.isnumeric() == True:
                    rt1 = int(rt1)
                    break
                else:
                    print('-' * 30)
                    print('Valor incorreto, apenas números!')
            for a in range(0, rt1):
                while True: # Nome da impresa
                    print('-' * 30)
                    nome_empresa = str(input('Informe o nome da empresa, [0] para autônomo: ')).strip()
                    while True:
                        print('-' * 30)
                        nome_empresa = 'Autônomo' if nome_empresa == '0' else nome_empresa
                        nome_empresa_confirmar = str(input(f'Posso confirmar {nome_empresa}, [S/N]: ')).strip().upper()[0]
                        if nome_empresa_confirmar == 'S':
                            break
                        elif nome_empresa_confirmar == 'N':
                            print('-' * 30)
                            print('Por favor, informe o novo nome da empresa!')
                            break
                        else:
                            print('-' * 30)
                            print('Valor incorreto!')
                    if nome_empresa_confirmar == 'S':
                        break
                while True: # Função que fazia dentro da empresa uma ou mais
                    função0 = '' # Função principal
                    while True:
                        print('-' * 30)
                        função1 = str(input(f'Informer uma função da qual trabalha/trabalhava na {nome_empresa}: ')).strip().title()
                        while True:
                            print('-' * 30)
                            função1_confirmar = str(input(f'Posso confirmar a função {função1}, [S/N]: ')).strip().upper()[0]
                            if função1_confirmar == 'S':
                                função0 += f'Função:{função1}, '
                                break
                            elif função1_confirmar == 'N':
                                break
                            else:
                                print('-' * 30)
                                print('Valor incorreto!')
                        while True:
                            print('-' * 30)
                            função3 = str(input('Quer adicionar mais uma função [S/N]: ')).strip().upper()[0]
                            if função3 == 'S':
                                break
                            elif função3 == 'N':
                                break
                        if função3 == 'N':
                            break
                    break
                while True: # Tempo trabalhado
                    print('-' * 30)
                    tempo_trabalhado0 = str(input(f'informe em que ano começou a trabalhar na empresa {nome_empresa}: ')).strip()
                    if tempo_trabalhado0.isnumeric() == True:
                        tempo_trabalhado0 = int(tempo_trabalhado0)
                    else:
                        print('-' * 30)
                        print('Valor incorreto, apenas números!')
                    print('-' * 30)
                    tempo_trabalhado1 = str(input(f'Informe o ano que terminou de trabalhar, ou se trabalha ano atual: ')).strip()
                    if tempo_trabalhado1.isnumeric() == True:
                        tempo_trabalhado1 = int(tempo_trabalhado1)
                    else:
                        print('-' * 30)
                        print('Valor incorreto, apenas números!')
                    while True:
                        print('-' * 30)
                        tempo_trabalhado3 = str(input(f'Posso confirmar que iniciou em {tempo_trabalhado0} e terminou/trabalha em {tempo_trabalhado1}, na empresa {nome_empresa}, [S/N]: ')).strip().upper()[0]
                        if tempo_trabalhado3 == 'S':
                            break
                        elif tempo_trabalhado3 == 'N':
                            print('-' * 30)
                            print('Por favor, informer o novo ano de trabalho!')
                        else:
                            print('-' * 30)
                            print('Valor incorreto!')
                    tempo_trabalhado = f'{tempo_trabalhado0} - {tempo_trabalhado1}'
                    if tempo_trabalhado3 == 'S':
                        break
                registro_de_trabalho += f'Nome da Empresa:{nome_empresa}, {função0} Ano:{tempo_trabalhado};' # Última linha do registro de trabalho
        elif registro == 'não tenho':
            registro_de_trabalho = 'Nenhum registro de trabalho'
        break
    return registro_de_trabalho
