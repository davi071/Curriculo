def modificação():
    while True:
        import os # Importação do sistema
        from script.configuração import config1,config2
        caminho = config1(1) # Configuração do caminho
        lista_currículos = config1(3) # Lista de todos os currículos
        opção1 = '' # Para poder sair la em baixo
        print('-' * 30)
        opção = str(input('''Qual o ID do currículo a ser modificado:
[ 0 ] Voltar menu
[ Enter ]Visualizar lista currículo
[ ID ] Currículo
Digite aqui: '''))
        if opção == '0':
            break
        elif opção == '':
            print('-' * 30)
            print(lista_currículos)
        elif opção.isnumeric() == True: # Confirma se é número e se existe o currículo
            id_0 = config2(3,opção) # Currículo escolhido
            continua = 0
            with open(f'{caminho}/{id_0}', 'r', encoding='UTF-8') as arquivo:
                currículo = arquivo.readlines()
            for linha in currículo:
                if 'Currículo finalizado' in linha:
                    continua = 1
            arquivo.close()
            if continua == 1:
                while True: # Verificar o que tem dentro do currículo
                    with open(f'{caminho}/{id_0}', 'r', encoding='UTF-8') as arquivo:
                        currículo = arquivo.readlines()
                    for linha in currículo: # Ele ira copiar todas as linhas referente a escolha do usuário
                        if 'ID:' in linha:
                            dado01 = linha[:-1] # Salva o ID
                        if 'Nome:' in linha:
                            dado02 = linha[:-1] # Salva o Nome
                        if 'Criado em:' in linha:
                            dado03 = linha[:-1] # Salva a data de criação
                        if 'Idade:' in linha:
                            dado0 = linha[:-1]
                        if 'CNH:' in linha:
                            dado1 = linha[:-1]
                        if 'Nacionalidade:' in linha:
                            dado2 = linha[:-1]
                        if 'Estado Civil:' in linha:
                            dado3 = linha[:-1]
                        if 'Telefone:' in linha:
                            dado4 = linha[:-1]
                        if 'Email:' in linha:
                            dado5 = linha[:-1]
                        if 'Endereço:' in linha:
                            dado6 = linha[:-1]
                        if 'Ensino Médio:' in linha:
                            dado7 = linha[:-1]
                        if 'Ensino Superior:' in linha:
                            dado8 = linha[:-1]
                        if 'Registro de Trabalho:' in linha:
                            dado9 = linha[:-1]
                        if 'Atividade Extra:' in linha:
                            dado10 = linha[:-1]
                        if 'Informação Adicional:' in linha:
                            dado11 = linha[:-1]
                    arquivo.close()
                    n = '1','2','3','4','5','6','7','8','9','10','11','12' # Opção disponíveis
                    print('-' * 30)
                    opção1 = str(input(f'''O que deseja modificar:
[ 0 ] Voltar          [ 7 ] Endereço
[ 1 ] Idade           [ 8 ] Ensino Médio
[ 2 ] CNH             [ 9 ] Ensino Superior
[ 3 ] Nacionalidade   [ 10 ] Registro de trabalho
[ 4 ] Estado Civil    [ 11 ] Atividade Extra
[ 5 ] Telefone        [ 12 ] Informação Adicional
[ 6 ] Email
Digite aqui: ''')).strip()
                    if opção1 == '0':
                        break
                    elif opção1.isnumeric() == True:
                        if opção1 in n: # Confirma se a opção escolhida para alterar tem no currículo
                            while True:
                                from script.exclusão import excluir1
                                opção1 = int(opção1)
                                if opção1 == 1: # Opção Idade
                                    print('-' * 30)
                                    opção2 = str(input('Deseja alterar a Idade [S/N]: ')).strip().upper()[0]
                                    if opção2 == 'S':
                                        from script.Dados.Idade import idade
                                        idade1 = idade('') # Variável que vai salvar a nova idade
                                        idade2 = f'Idade:{idade1}'
                                        excluir1(id_0) # Opção que ira excluir o currículo (id_0 é o nome do currículo completo)
                                        with open(f'{caminho}/{id_0}', 'w', encoding='utf-8') as adicionar:
                                            adicionar.write(f'{dado01}\n{dado02}\n{idade2}\n{dado1}\n{dado2}\n{dado3}\n{dado4}\n{dado5}\n{dado6}\n{dado7}\n{dado8}\n{dado9}\n{dado10}\n{dado11}\nCurrículo finalizado\n{dado03}')
                                        print('-' * 30)
                                        print('Alterado com sucesso')
                                        break
                                    elif opção2 == 'N':
                                        break
                                elif opção1 == 2: # Opção CNH
                                    print('-' * 30)
                                    opção2 = str(input('Deseja alterar a CNH [S/N]: ')).strip().upper()[0]
                                    if opção2 == 'S':
                                        from script.Dados.CNH import cnh
                                        cnh1 = cnh('')
                                        cnh2 = f'CNH:{cnh1}'
                                        excluir1(id_0)
                                        with open(f'{caminho}/{id_0}', 'w', encoding='utf-8') as adicionar:
                                            adicionar.write(f'{dado01}\n{dado02}\n{dado0}\n{cnh2}\n{dado2}\n{dado3}\n{dado4}\n{dado5}\n{dado6}\n{dado7}\n{dado8}\n{dado9}\n{dado10}\n{dado11}\nCurrículo finalizado\n{dado03}')
                                        print('-' * 30)
                                        print('Alterado com sucesso')
                                        break
                                    elif opção2 == 'N':
                                        break
                                elif opção1 == 3: # Opção Nacionalidade
                                    print('-' * 30)
                                    opção2 = str(input('Deseja alterar a Nacionalidade [S/N]: ')).strip().upper()[0]
                                    if opção2 == 'S':
                                        from script.Dados.Nacionalidade import nacionalidade
                                        nacionalidade1 = nacionalidade('')
                                        nacionalidade2 = f'Nacionalidade:{nacionalidade1}'
                                        excluir1(id_0)
                                        with open(f'{caminho}/{id_0}', 'w', encoding='utf-8') as adicionar:
                                            adicionar.write(f'{dado01}\n{dado02}\n{dado0}\n{dado1}\n{nacionalidade2}\n{dado3}\n{dado4}\n{dado5}\n{dado6}\n{dado7}\n{dado8}\n{dado9}\n{dado10}\n{dado11}\nCurrículo finalizado\n{dado03}')
                                        print('-' * 30)
                                        print('Alterado com sucesso')
                                        break
                                    elif opção2 == 'N':
                                        break
                                elif opção1 == 4: # Opção Estado Civil
                                    print('-' * 30)
                                    opção2 = str(input('Deseja alterar a Estado Civil [S/N]: ')).strip().upper()[0]
                                    if opção2 == 'S':
                                        from script.Dados.Civil import estado_civil
                                        civil1 = estado_civil('')
                                        civil2 = f'Estado Civil:{civil1}'
                                        excluir1(id_0)
                                        with open(f'{caminho}/{id_0}', 'w', encoding='utf-8') as adicionar:
                                            adicionar.write(f'{dado01}\n{dado02}\n{dado0}\n{dado1}\n{dado2}\n{civil2}\n{dado4}\n{dado5}\n{dado6}\n{dado7}\n{dado8}\n{dado9}\n{dado10}\n{dado11}\nCurrículo finalizado\n{dado03}')
                                        print('-' * 30)
                                        print('Alterado com sucesso')
                                        break
                                    elif opção2 == 'N':
                                        break
                                elif opção1 == 5: # Opção Telefone
                                    print('-' * 30)
                                    opção2 = str(input('Deseja alterar a Telefone [S/N]: ')).strip().upper()[0]
                                    if opção2 == 'S':
                                        from script.Dados.Telefone import telefone
                                        fone1 = telefone('')
                                        fone2 = f'Telefone:{fone1}'
                                        excluir1(id_0)
                                        with open(f'{caminho}/{id_0}', 'w', encoding='utf-8') as adicionar:
                                            adicionar.write(f'{dado01}\n{dado02}\n{dado0}\n{dado1}\n{dado2}\n{dado3}\n{fone2}\n{dado5}\n{dado6}\n{dado7}\n{dado8}\n{dado9}\n{dado10}\n{dado11}\nCurrículo finalizado\n{dado03}')
                                        print('-' * 30)
                                        print('Alterado com sucesso')
                                        break
                                    elif opção2 == 'N':
                                        break
                                elif opção1 == 6: # Opção Email
                                    print('-' * 30)
                                    opção2 = str(input('Deseja alterar a Email [S/N]: ')).strip().upper()[0]
                                    if opção2 == 'S':
                                        from script.Dados.Email import email
                                        email1 = email('')
                                        email2 = f'Email:{email1}'
                                        excluir1(id_0)
                                        with open(f'{caminho}/{id_0}', 'w', encoding='utf-8') as adicionar:
                                            adicionar.write(f'{dado01}\n{dado02}\n{dado0}\n{dado1}\n{dado2}\n{dado3}\n{dado4}\n{email2}\n{dado6}\n{dado7}\n{dado8}\n{dado9}\n{dado10}\n{dado11}\nCurrículo finalizado\n{dado03}')
                                        print('-' * 30)
                                        print('Alterado com sucesso')
                                        break
                                    elif opção2 == 'N':
                                        break
                                elif opção1 == 7: # Opção Endereço
                                    print('-' * 30)
                                    opção2 = str(input('Deseja alterar a Endereço [S/N]: ')).strip().upper()[0]
                                    if opção2 == 'S':
                                        from script.Dados.Endereço import endereço
                                        endereço1 = endereço('')
                                        endereço2 = f'Endereço:{endereço1}'
                                        excluir1(id_0)
                                        with open(f'{caminho}/{id_0}', 'w', encoding='utf-8') as adicionar:
                                            adicionar.write(f'{dado01}\n{dado02}\n{dado0}\n{dado1}\n{dado2}\n{dado3}\n{dado4}\n{dado5}\n{endereço2}\n{dado7}\n{dado8}\n{dado9}\n{dado10}\n{dado11}\nCurrículo finalizado\n{dado03}')
                                        print('-' * 30)
                                        print('Alterado com sucesso')
                                        break
                                    elif opção2 == 'N':
                                        break
                                elif opção1 == 8: # Opção Ensino Médio
                                    print('-' * 30)
                                    opção2 = str(input('Deseja alterar a Ensino Médio [S/N]: ')).strip().upper()[0]
                                    if opção2 == 'S':
                                        from script.Dados.Ensino_médio import ensino_médio
                                        médio1 = ensino_médio(int(1))
                                        médio2 = f'Ensino Médio:{médio1}'
                                        excluir1(id_0)
                                        with open(f'{caminho}/{id_0}', 'w', encoding='utf-8') as adicionar:
                                            adicionar.write(f'{dado01}\n{dado02}\n{dado0}\n{dado1}\n{dado2}\n{dado3}\n{dado4}\n{dado5}\n{dado6}\n{médio2}\n{dado8}\n{dado9}\n{dado10}\n{dado11}\nCurrículo finalizado\n{dado03}')
                                        print('-' * 30)
                                        print('Alterado com sucesso')
                                        break
                                    elif opção2 == 'N':
                                        break
                                elif opção1 == 9: # Opção Ensino Superior
                                    print('-' * 30)
                                    opção2 = str(input('Deseja alterar a Ensino Superior [S/N]: ')).strip().upper()[0]
                                    if opção2 == 'S':
                                        from script.Dados.Ensino_superior import ensino_superior
                                        superior1 = ensino_superior('')
                                        superior2 = f'Ensino Superior:{superior1}'
                                        excluir1(id_0)
                                        with open(f'{caminho}/{id_0}', 'w', encoding='utf-8') as adicionar:
                                            adicionar.write(f'{dado01}\n{dado02}\n{dado0}\n{dado1}\n{dado2}\n{dado3}\n{dado4}\n{dado5}\n{dado6}\n{dado7}\n{superior2}\n{dado9}\n{dado10}\n{dado11}\nCurrículo finalizado\n{dado03}')
                                        print('-' * 30)
                                        print('Alterado com sucesso')
                                        break
                                    elif opção2 == 'N':
                                        break
                                elif opção1 == 10: # Opção Registro de Trabalho
                                    print('-' * 30)
                                    opção2 = str(input('Deseja alterar a Registro de Trabalho [S/N]: ')).strip().upper()[0]
                                    if opção2 == 'S':
                                        from script.Dados.Registro_de_trabalho import registro_de_trabalho
                                        registro1 = registro_de_trabalho('')
                                        registro2 = f'Registro de Trabalho:{registro1}'
                                        excluir1(id_0)
                                        with open(f'{caminho}/{id_0}', 'w', encoding='utf-8') as adicionar:
                                            adicionar.write(f'{dado01}\n{dado02}\n{dado0}\n{dado1}\n{dado2}\n{dado3}\n{dado4}\n{dado5}\n{dado6}\n{dado7}\n{dado8}\n{registro2}\n{dado10}\n{dado11}\nCurrículo finalizado\n{dado03}')
                                        print('-' * 30)
                                        print('Alterado com sucesso')
                                        break
                                    elif opção2 == 'N':
                                        break
                                elif opção1 == 11: # Opção Atividade Extra
                                    print('-' * 30)
                                    opção2 = str(input('Deseja alterar a Atividade Extra [S/N]: ')).strip().upper()[0]
                                    if opção2 == 'S':
                                        from script.Dados.Atividades_extra import atividade_extra
                                        atividade1 = atividade_extra('')
                                        atividade2 = f'Atividade Extra:{atividade1}'
                                        excluir1(id_0)
                                        with open(f'{caminho}/{id_0}', 'w', encoding='utf-8') as adicionar:
                                            adicionar.write(f'{dado01}\n{dado02}\n{dado0}\n{dado1}\n{dado2}\n{dado3}\n{dado4}\n{dado5}\n{dado6}\n{dado7}\n{dado8}\n{dado9}\n{atividade2}\n{dado11}\nCurrículo finalizado\n{dado03}')
                                        print('-' * 30)
                                        print('Alterado com sucesso')
                                        break
                                    elif opção2 == 'N':
                                        break
                                elif opção1 == 12: # Opção Informação Adicional
                                    print('-' * 30)
                                    opção2 = str(input('Deseja alterar a Informação Adicional [S/N]: ')).strip().upper()[0]
                                    if opção2 == 'S':
                                        from script.Dados.Informações_adicionais import informações_adicionais
                                        informações1 = informações_adicionais('')
                                        informações2 = f'Informação Adicional:{informações1}'
                                        excluir1(id_0)
                                        with open(f'{caminho}/{id_0}', 'w', encoding='utf-8') as adicionar:
                                            adicionar.write(f'{dado01}\n{dado02}\n{dado0}\n{dado1}\n{dado2}\n{dado3}\n{dado4}\n{dado5}\n{dado6}\n{dado7}\n{dado8}\n{dado9}\n{dado10}\n{informações2}\nCurrículo finalizado\n{dado03}')
                                        print('-' * 30)
                                        print('Alterado com sucesso')
                                        break
                                    elif opção2 == 'N':
                                        break
                        else:
                            print('-' * 30)
                            print('Você não pode acessar essa opção!')
                    else:
                        print('-' * 30)
                        print('Valor incorreto!')
            else:
                print('-' * 30)
                print('Currículo não encontrado!')
        else:
            print('-' * 30)
            print('Valor incorreto!')
        if opção1 == '0':
            break
#modificação()
