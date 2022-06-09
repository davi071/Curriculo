def visualizar_currículo():
    from script.configuração import config1,config2
    caminho = config1(1) # Caminho da pasta dos currículos
    id_completo = config1(2) # Retorna todos os IDs completos (com ou sem #)
    id_completo1 = config1(3) # Retorna todos os IDs completos (Sem #)
    ids = config1(4)
    print('-' * 30)
    print('{:^30}'.format('Visualizador de currículo'))
    while True:
        print('-' * 30)
        opção = str(input('''[ 0 ] Voltar
[ Enter ] Mostrar todos os currículos disponíveis
[ F ] Filtrar currículos completos
[ ID ] Visualizar pelo ID
Digite aqui: ''')).strip().upper()
        if opção == '0': # Para sair
            break
        elif opção == '': # Se pressionar enter
            cont0 = len(id_completo) # Conta quantos currículos (Com ou sem #) tem
            if cont0 == 0:
                print('-' * 30)
                print('Nenhum currículo')
            elif cont0 > 0:
                print('-' * 30)
                print(id_completo)
        elif opção == 'F': # Filtrando currículos prontos 
            cont1 = len(id_completo1) # Conta quantos currículos prontos tem
            if cont1 == 0:
                print('-' * 30)
                print('Nenhum currículo')
            elif cont1 > 0:
                print('-' * 30)
                print(id_completo1)
        elif opção.isnumeric() == True:
            if opção in ids:
                usuário = config2(3,opção)
                with open(f'{caminho}/{usuário}', 'r', encoding='UTF-8') as arquivo:
                    currículo = arquivo.readlines()
                nome = '' # Armazena nome do usuário
                nacionalidade = '' # Armazena a nacionalidade
                estado_civil = '' # Armazena o estado civil do usuário
                idade = '' # Armazena a idade do usuário
                cnh = ''
                rua = ''
                número = ''
                cidade = ''
                estado = ''
                fone = ''
                email = ''
                médio = '' # Armazena a escolaridade do usuário
                for linha in currículo:
                    if 'Nome:' in linha: # Nome
                        a1 = linha.find('Nome:')
                        nome += linha[(a1 + 5):-1]
                    if 'Nacionalidade:' in linha:
                        a2 = linha.find('Nacionalidade:')
                        nacionalidade += linha[(a2 + 14):-1]
                    if 'Estado Civil:' in linha:
                        a3 = linha.find('Estado Civil:')
                        estado_civil += linha[(a3 + 13):-1]
                    if 'Idade:' in linha:
                        a4 = linha.find('Idade:')
                        idade += linha[(a4 + 6):-1]
                    if 'CNH:' in linha:
                        a41 = linha.find('CNH:')
                        cnh += linha[(a41 + 4):-1]
                    if 'Endereço' in linha:
                        a5 = linha.find('Rua:')
                        a6 = linha.find('N°:')
                        a7 = linha.find('Cidade:')
                        a8 = linha.find('Estado:')
                        rua += linha[(a5 + 4):(a6 - 2)]
                        número += linha[(a6):(a7 - 2)]
                        cidade += linha[(a7 + 7):(a8 - 2)]
                        estado += linha[(a8 + 7):-1]
                    if 'Telefone:' in linha:
                        a9 = linha.find('Telefone:')
                        fone += linha[(a9):-1]
                    if 'Email:' in linha:
                        a10 = linha.find('Email:')
                        email += linha[(a10):-1]
                    if 'Ensino Médio:' in linha:
                        a11 = linha.find('Ensino Médio:')
                        médio += linha[a11:-1]
                print('{:^60}'.format('\033[1mCURRÍCULO\033[m'))
                print('_' * 60)
                print(f'\033[1;4m{nome:^30}\033[m')
                print(f'{nacionalidade}, {estado_civil}, {idade} anos')
                print(f'CNH:{cnh}')
                print(f'{rua}, {número}')
                print(f'{cidade} - {estado}')
                print(f'{fone} - {email}\n')
                print('     \033[1;4mOBJETIVO\033[m')
                print('_' * 60)
                print('Todos os objetivos serão em branco.\n')
                print('     \033[1;4mFORMAÇÃO\033[m')
                print('_' * 60)
                print(f'{médio}')
                for linha in currículo:
                    if 'Ensino Superior:' in linha: # Ensino Superior coletar dados .txt
                        b1 = linha.count('Nome Instituição:') # Informa a quantidade de cursos superiores
                        if b1 == 0:
                            print(linha)
                        elif b1 > 0:
                            print('Ensino Superior:')
                            b2 = 0
                            for a in range(0, b1):
                                a12 = linha.find('Nome Instituição:', b2,)
                                a13 = linha.find('Nome Curso:', b2,)
                                a14 = linha.find('Situação:', b2,)
                                a15 = linha.find(';', (b2 + 1),)
                                superior1 = f'{linha[(a12 + 17):(a13 - 2)]}'
                                print(f'Instituição: {superior1} - ',end='')
                                superior2 = f'{linha[(a13 + 11):(a14 - 2)]}'
                                print(f'Curso: {superior2} - ', end='')
                                superior3 = f'{linha[(a14 + 9):a15]}'
                                print(f' {superior3}')
                                b2 += a15
                print('     \033[1;4mEXPERIÊNCIA PROFISSIONAL\033[m')
                print('_' * 60)
                for linha in currículo:
                    if 'Registro de Trabalho:' in linha:
                        b3 = linha.count('Nome da Empresa:')
                        if b3 == 0:
                            print(linha)
                        elif b3 > 0:
                            b4 = 0
                            for b in range(0, b3):
                                a16 = linha.find('Nome da Empresa:', b4,)
                                a17 = linha.find('Função:', b4,)
                                a18 = linha.find('Ano:', b4,)
                                a19 = linha.find(';', (b4 + 1),)
                                registro1 = f'{linha[(a16 + 16):(a17 - 2)]}'
                                print(f'Empresa: {registro1} - ', end='')
                                registro2 = f'{linha[(a17 + 7):(a18 - 2)]}'
                                print(f'Função: {registro2} - ', end='')
                                registro3 = f'{linha[(a18 + 4):a19]}'
                                print(f'Ano: {registro3}')
                                b4 += a19
                print('\n')
                print('     \033[1;4mQUALIFICAÇÕES E ATIVIDADE EXTRA CURRICULAR\033[m')
                print('_' * 60)
                for linha in currículo:
                    if 'Atividade Extra:' in linha:
                        b5 = linha.count('Nome da atividade:')
                        if b5 == 0:
                            print(linha)
                        elif b5 > 0:
                            b6 = 0
                            for c in range(0, b5):
                                a20 = linha.find('Nome da atividade:', b6,)
                                a21 = linha.find('Período:', b6,)
                                a22 = linha.find('Carga horaria:', b6,)
                                a23 = linha.find(';', (b6 + 1),)
                                atividade1 = f'{linha[(a20 + 18):(a21 - 1)]}'
                                print(f'Atividade: {atividade1} - ', end='')
                                atividade2 = f'{linha[(a21 + 8):(a22 - 2)]}'
                                print(f'Período: {atividade2} - ', end='')
                                atividade3 = f'{linha[(a22 + 14):a23]}'
                                print(f'Carga de {atividade3} horas')
                                b6 += a23
                print('\n')
                print('     \033[1;4mINFORMAÇÕES ADICIONAIS\033[m')
                for linha in currículo:
                    if 'Informação Adicional:' in linha:
                        b7 = linha.count('Ponto:')
                        if b7 == 0:
                            print(linha)
                        elif b7 > 0:
                            b8 = 0
                            for d in range(0, b7):
                                a24 = linha.find('Ponto:', b8,)
                                a25 = linha.find(';', (b8 + 1),)
                                adicional1 = f'{linha[(a24 + 6):a25]}'
                                print(f'• {adicional1}')
                                b8 += a25
                print('_' * 60)
            else:
                print('-' * 30)
                print(f'Não existe currículo com esse ID{opção}')
        else:
            print('-' * 30)
            print('Valor incorreto!')
#visualizar_currículo()
