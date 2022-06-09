def atividade_extra(atividade_extra):
    atividade_extra = ''
    while True: # Pergunta se usuário tem ou quer adicionar um atividade extra curricular
        print('-' * 30)
        atividade_extra0 = str(input('Informe se têm e quer adicionar atividades extra curricular, [S/N]: ')).strip().upper()[0]
        if atividade_extra0 == 'S':
            while True: # while de segurança
                while True: # Nome da atividade extra curricular
                    print('-' * 30)
                    nome_atividade0 = str(input('Informe o nome da atividade extra curricular a ser implementada: ')).strip().title()
                    while True: # Confirmar
                        print('-' * 30)
                        nome_atividade0_confirma = str(input(f'Posso confirmar {nome_atividade0}, [S/N]: ')).strip().upper()[0]
                        if nome_atividade0_confirma == 'S':
                            break
                        elif nome_atividade0_confirma == 'N':
                            print('Por favor informe a nova atividade!')
                            break
                        else:
                            print('-' * 30)
                            print('Valor incorreto!')
                    if nome_atividade0_confirma == 'S':
                        break
                while True: # Período da atividade extra curricular
                    print('-' * 30)
                    periodo_atividade0 = str(input(f'Gostaria de informar o período da atividade {nome_atividade0}, [S/N]: ')).strip().upper()[0]
                    if periodo_atividade0 == 'S': # Continua a perguntar se usuário confirmar 'S'
                        while True: # Início do período
                            while True:
                                print('-' * 30)
                                início_periodo_atividade = str(input('Informe a data/mês/ano do início período: ')).strip()
                                if início_periodo_atividade.isnumeric() == True:
                                    início_periodo_atividade = int(início_periodo_atividade)
                                    break 
                                else:
                                    print('-' * 30)
                                    print('Valor incorreto, apenas números!')
                            while True:
                                print('-' * 30)
                                fim_periodo_atividade = str(input('Informe a data/mês/ano do fim periodo: ')).strip()
                                if fim_periodo_atividade.isnumeric() == True:
                                    fim_periodo_atividade = int(fim_periodo_atividade)
                                    break
                                else:
                                    print('-' * 30)
                                    print('Valor incorreto, apenas números!')
                            while True: # Confirmar
                                print('-' * 30)
                                periodo_atividade_confirma = str(input(f'Posso confirmar que, começou em {início_periodo_atividade} e terminou em {fim_periodo_atividade} [S/N]: ')).strip().upper()[0]
                                if periodo_atividade_confirma == 'S':
                                    break
                                elif periodo_atividade_confirma == 'N':
                                    print('Por favor, informe o novo periodo!')
                                    break
                                else:
                                    print('-' * 30)
                                    print('Valor incorreto!')
                            if periodo_atividade_confirma == 'S':
                                break
                        periodo_extra = f'{início_periodo_atividade} até {fim_periodo_atividade}' # Armazena a informação do periodo extra
                    elif periodo_atividade0 == 'N':
                        periodo_extra = 'Não informado'
                    else:
                        print('-' * 30)
                        print('Valor incorreto!')
                    if periodo_atividade0 in 'SN': # Para sair do loop do periodo atividade
                        break
                while True: # Carga horaria da atividade
                    print('-' * 30)
                    carga_atividade0 = str(input(f'Informe quantas horas de atividade no {nome_atividade0}: ')).strip()
                    carga_atividade0_confirma = ''
                    if carga_atividade0.isnumeric() == True:
                        carga_atividade0 = int(carga_atividade0)
                        while True:
                            print('-' * 30)
                            carga_atividade0_confirma = str(input(f'Posso confirmar periodo {carga_atividade0} Horas, [S/N]: ')).strip().upper()[0]
                            if carga_atividade0_confirma == 'S':
                                break
                            elif carga_atividade0_confirma == 'N':
                                print('-' * 30)
                                print('Por favor, informe a nova carga horaria!')
                                break
                            else:
                                print('-' * 30)
                                print('Valor incorreto!')
                    else:
                        print('-' * 30)
                        print('Valor incorreto, apenas números!')
                    if carga_atividade0_confirma == 'S':
                        break
                while True: # Condição para adicionar mais atividades
                    print('-' * 30)
                    atividade_extra += f'Nome da atividade:{nome_atividade0}, Período:{periodo_extra}, Carga horaria:{carga_atividade0};'
                    adicionar_atividade_extra = str(input(f'Gostaria de adicionar mais uma atividade extra curricular: [S/N]: ')).strip().upper()[0]
                    if adicionar_atividade_extra == 'S':
                        break
                    elif adicionar_atividade_extra == 'N':
                        break
                    else:
                        print('-' * 30)
                        print('Valor incorreto!')
                if adicionar_atividade_extra == 'N':
                    break
        elif atividade_extra0 == 'N':
            atividade_extra = 'Nada a acrescentar'
            break
        else:
            print('-' * 30)
            print('Valor incorreto!')
        if atividade_extra0 in 'SN':
            break
    return atividade_extra
