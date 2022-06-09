def ensino_superior(ensino_superior):
    info1 = '', 'nenhum para', 'cursando/concluído'
    info2 = '', 'cursando', 'concluído'
    ensino_superior = ''
    while True: # while de segurança
        adicionar_curso = '' # Condição para sair
        while True:
            print('-' * 30)
            superior = str(input('\033[2;32mSobre o Ensino Superior\033[m, [1] nenhum/nunca cursado, [2] está cursando/concluído: ')).strip().upper()[0]
            superior_confirma = ''
            if superior.isnumeric() == True and superior == '1' or superior == '2':
                superior = int(superior)
                while True:
                    print('-' * 30)
                    superior_confirma = str(input(f'Posso confirmar {info1[superior]} o ensino superior? [S/N]: ')).strip().upper()[0]
                    if superior_confirma == 'S':
                        break
                    elif superior_confirma == 'N':
                        print('-' * 30)
                        print('Por favor, informe o status do ensino superior!')
                        break
                    else:
                        print('-' * 30)
                        print('Valor incorreto!')
            else:
                print('-' * 30)
                print('Valor incorreto, apenas número de 1 a 3')
            if superior_confirma == 'S':
                superior = int(superior)
            curso = f'{info1[superior]}' # Se o usuário escolher opção '1'
            if superior == 2: # Se o usuário escolher a opção '2' ou '3'
                curso = '' # Salva todos os dados coletados instituição, curso, cursando/concluído
                while True: # while de segurança
                    while True: # Nome da instituição
                        print('-' * 30)
                        nome_instituição_ensino_superior = str(input('Informe o nome da instituição do curso superior ou [0] não informar: ')).strip().capitalize()
                        while True:
                            print('-' * 30)
                            nome_instituição_ensino_superior = 'Não relatado' if nome_instituição_ensino_superior == '0' else nome_instituição_ensino_superior
                            nome_instituição_ensino_superior_confirma = str(input(f'Instituição {nome_instituição_ensino_superior}, posso confirmar [S/N]: ')).strip().upper()[0]
                            if nome_instituição_ensino_superior_confirma == 'S':
                                break
                            elif nome_instituição_ensino_superior_confirma == 'S':
                                print('-' * 30)
                                print('Por favor, informe o novo nome da instituição!')
                                break
                            else:
                                print('-' * 30)
                                print('Valor incorreto!')
                        if nome_instituição_ensino_superior_confirma == 'S': # Condição de sair 'Nome da instituição'
                            break
                    while True: # Nome do curso
                        print('-' * 30)
                        nome_ensino_superior = str(input('Informe o nome do curso: ')).strip().title()
                        while True:
                            print('-' * 30)
                            nome_ensino_superior_confirma = str(input(f'Curso de {nome_ensino_superior}, posso confirmar [S/N]: ')).strip().upper()[0]
                            if nome_ensino_superior_confirma == 'S':
                                break
                            elif nome_ensino_superior_confirma == 'N':
                                print('-' * 30)
                                print('Por favor, informe o novo nome do curso superior!')
                                break
                            else:
                                print('-' * 30)
                                print('Valor incorreto!')
                        if nome_ensino_superior_confirma == 'S': # Condição de sair 'Nome do curso'
                            break
                    while True: # Se esta cursando ou concluído
                        print('-' * 30)
                        status = str(input(f'O curso {nome_ensino_superior}, esta [1] cursando, [2] concluído: ')).strip().upper()[0]
                        status_confirma = ''
                        if status.isnumeric() == True and status == '1' or status == '2':
                            status = int(status)
                            while True:
                                print('-' * 30)
                                status_confirma = str(input(f'Posso confirmar que {info2[status]}, [S/N]: ')).strip().upper()[0]
                                if status_confirma == 'S':
                                    break
                                elif status_confirma == 'N':
                                    break
                                else:
                                    print('Valor incorreto!')
                        else:
                            print('-' * 30)
                            print('Valor incorreto, apenas número 1 ou 2!')
                        if status_confirma == 'S':
                            status0 = f'{info2[status]}'
                            break
                    curso = f'Nome Instituição:{nome_instituição_ensino_superior}, Nome Curso:{nome_ensino_superior}, Situação:{status0};'
                    ensino_superior += curso
                    while True: # Pergunta se quer adicionar mais um curso
                        print('-' * 30)
                        adicionar_curso = str(input('Quer adicionar mais um curso, [S/N]: ')).strip().upper()[0]
                        if adicionar_curso == 'S':
                            break
                        elif adicionar_curso == 'N':
                            break
                        else:
                            print('-' * 30)
                            print('Valor incorreto!')
                    if adicionar_curso == 'N':
                        break
                if adicionar_curso == 'N':
                    break
            else:
                ensino_superior += curso
                adicionar_curso = 'N'
                break
        if adicionar_curso == 'N':
            break
    return ensino_superior
