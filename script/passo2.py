def complementar1(a,b): # Para escolher um currículo se ele não foi escolhido
    while True:
        from script.configuração import config1
        from script.configuração import config2
        id_completo = config1(8) # ids_ com '#'
        ids = config1(9)
        print('-' * 30)
        print(id_completo)
        sair = 0
        while True:
            print('-' * 30)
            opção = str(input('Qual ID você que alterar, [0] voltar,[Enter] mostrar currículos para adicionar: ')).strip()
            if opção == '0':
                break
            elif opção == '':
                break
            elif opção.isnumeric() == True:
                if opção in ids:
                    nome = config2(1,opção)
                    nome_usuário = f'#ID{opção}@{nome}.txt' # Nome do usuário incompleto
                    nome_usuário1 = f'ID{opção}@{nome}.txt' # Nome do usuário pronto
                    sair = 1
                    break
                else:
                    print('-' * 30)
                    print(f'Este ID:{opção} não corresponde a lista de IDs')
            else:
                print('-' * 30)
                print('Valor incorreto, apenas números!')
        if opção == '0' or sair == 1:
            if sair == 1:
                return nome_usuário, nome_usuário1
#############################################################################################################
def complementar(a,b): # Se ja foi escolhido o currículo ele vai direto
    import os
    from script.configuração import config1,config2
    caminho = config1(1) # Caminho da pasta do currículo
    nome_usuário = a # Variável do Id_incompleto 'Com #' Str
    x = b # ID Número
    y = config2(1,x) # Variável do Id_completo 'Sem #'
    nome_usuário1 = f'ID{x}@{y}.txt' # Gerar ID completo
    if a == '' and b == '':
        d = complementar1(a,b)
        nome_usuário = d[0]
        nome_usuário1 = d[1]
    while True: # Entra no loop
        dados_concluído = ''
        while True: # Para cada atualização uma atualização na pagina
            with open(f'{caminho}/{nome_usuário}', 'r') as usuário: # Ler tudo
                dados = usuário.readlines() # Ler todas as linhas
                idade0 = 0 # Inicio da leitura de idade
                for linha in dados:
                    if 'Idade:' in linha:
                        c = linha.find('Idade:')
                        if c >= 0:
                            idade0 += 1
                if idade0 == 0:
                    from script.Dados import Idade
                    idade1 = Idade.idade('')
                    with open(f'{caminho}/{nome_usuário}', 'a') as usuário:
                        usuário.write(f'Idade:{idade1}\n')
                    usuário.close()
                    print('Idade adicionado com sucesso')
                    break
                cnh0 = 0 # Inicio da leitura da CNH
                for linha in dados:
                    if 'CNH:' in linha:
                        c = linha.find('CNH:')
                        if c >= 0:
                            cnh0 += 1
                if cnh0 == 0:
                    from script.Dados import CNH
                    cnh1 = CNH.cnh('')
                    with open(f'{caminho}/{nome_usuário}', 'a') as usuário:
                        usuário.write(f'CNH:{cnh1}\n')
                    usuário.close()
                    print('CNH adicionado com sucesso')
                    break
                nacionalidade = 0 # Inicio da leitura da nacionalidade
                for linha in dados:
                    if 'Nacionalidade:' in linha:
                        c = linha.find('Nacionalidade')
                        if c >= 0:
                            nacionalidade += 1
                if nacionalidade == 0:
                    from script.Dados import Nacionalidade
                    nacionalidade1 = Nacionalidade.nacionalidade('')
                    with open(f'{caminho}/{nome_usuário}', 'a') as usuário:
                        usuário.write(f'Nacionalidade:{nacionalidade1}\n')
                    usuário.close()
                    print('Nacionalidade adicionado com sucesso')
                    break
                civil = 0 # Inicio da leitura do estado civil
                for linha in dados:
                    if 'Estado Civil:' in linha:
                        c = linha.find('Estado Civil:')
                        if c >= 0:
                            civil += 1
                if civil == 0:
                    from script.Dados import Civil
                    civil1 = Civil.estado_civil('')
                    with open(f'{caminho}/{nome_usuário}', 'a') as usuário:
                        usuário.write(f'Estado Civil:{civil1}\n')
                    usuário.close()
                    print('Estado Civil adicionado com sucesso')
                    break
                fone = 0 # Inicio da leitura do telefone
                for linha in dados:
                    if 'Telefone:' in linha:
                        c = linha.find('Telefone:')
                        if c >= 0:
                            fone += 1
                if fone == 0:
                    from script.Dados import Telefone
                    fone1 = Telefone.telefone('')
                    with open(f'{caminho}/{nome_usuário}', 'a') as usuário:
                        usuário.write(f'Telefone:{fone1}\n')
                    usuário.close()
                    print('Telefone adicionado com sucesso')
                    break
                email = 0 # Inicio da leitura do email
                for linha in dados:
                    if 'Email:' in linha:
                        c = linha.find('Email:')
                        if c >= 0:
                            email += 1
                if email == 0:
                    from script.Dados import Email
                    email1 = Email.email('')
                    with open(f'{caminho}/{nome_usuário}', 'a') as usuário:
                        usuário.write(f'Email:{email1}\n')
                    usuário.close()
                    print('Email adicionado com sucesso')
                    break
                endereço = 0 # Inicio da leitura do Endereço
                for linha in dados:
                    if 'Endereço:' in linha:
                        c = linha.find('Endereço:')
                        if c >= 0:
                            endereço += 1
                if endereço == 0:
                    from script.Dados import Endereço
                    endereço1 = Endereço.endereço('')
                    with open(f'{caminho}/{nome_usuário}', 'a') as usuário:
                        usuário.write(f'Endereço:{endereço1}\n')
                    usuário.close()
                    print('Endereço adicionado com sucesso')
                    break
                médio = 0 # Inicio da leitura do Ensino Médio
                for linha in dados:
                    if 'Ensino Médio:' in linha:
                        c = linha.find('Ensino Médio:')
                        if c >= 0:
                            médio += 1
                if médio == 0:
                    from script.Dados import Ensino_médio
                    médio1 = Ensino_médio.ensino_médio('')
                    with open(f'{caminho}/{nome_usuário}', 'a') as usuário:
                        usuário.write(f'Ensino Médio:{médio1}\n')
                    usuário.close()
                    print('Ensino Médio adicionado com sucesso')
                    break
                superior = 0 # Inicio da leitura do Ensino Superior
                for linha in dados:
                    if 'Ensino Superior:' in linha:
                        c = linha.find('Ensino Superior:')
                        if c >= 0:
                            superior += 1
                if superior == 0:
                    from script.Dados import Ensino_superior
                    superior1 = Ensino_superior.ensino_superior('')
                    with open(f'{caminho}/{nome_usuário}', 'a') as usuário:
                        usuário.write(f'Ensino Superior:{superior1}\n')
                    usuário.close()
                    print('Ensino Superior ok')
                    break
                registro_trabalho = 0 # Inicio da leitura do registro de trabalho
                for linha in dados:
                    if 'Registro de Trabalho:' in linha:
                        c = linha.find('Registro de Trabalho:')
                        if c >= 0:
                            registro_trabalho += 1
                if registro_trabalho == 0:
                    from script.Dados import Registro_de_trabalho
                    registro_trabalho1 = Registro_de_trabalho.registro_de_trabalho('')
                    with open(f'{caminho}/{nome_usuário}', 'a') as usuário:
                        usuário.write(f'Registro de Trabalho:{registro_trabalho1}\n')
                    usuário.close
                    print('Registro de trabalho adicionado com sucesso')
                    break
                atividade_extra = 0 # Inicio da leitura da atividade extra
                for linha in dados:
                    if 'Atividade Extra:' in linha:
                        c = linha.find('Atividade Extra:')
                        if c >= 0:
                            atividade_extra += 1
                if atividade_extra == 0:
                    from script.Dados import Atividades_extra
                    atividade_extra1 = Atividades_extra.atividade_extra('')
                    with open(f'{caminho}/{nome_usuário}', 'a') as usuário:
                        usuário.write(f'Atividade Extra:{atividade_extra1}\n')
                    usuário.close()
                    print('Atividade Extra adicionado com sucesso')
                    break
                informação_adicional = 0 # Inicio da leitura de informações adicional
                for linha in dados:
                    if 'Informação Adicional:' in linha:
                        c = linha.find('Informação Adicional:')
                        if c >= 0:
                            informação_adicional += 1
                if informação_adicional == 0:
                    from script.Dados import Informações_adicionais
                    informação_adicional1 = Informações_adicionais.informações_adicionais('')
                    with open(f'{caminho}/{nome_usuário}', 'a') as usuário:
                        usuário.write(f'Informação Adicional:{informação_adicional1}\n')
                    usuário.close()
                    print('Informação adicional adicionada com sucesso')
                    break
                with open(f'{caminho}/{nome_usuário}', 'a') as usuário:
                    data = config1(11)
                    usuário.write(f'Currículo finalizado\nCriado em:{data}')
                usuário.close()
                print('Todos os dados coletados!')
                copiar = ''
                with open(f'{caminho}/{nome_usuário}', 'r') as usuário1:
                    copiar += usuário1.read()
                usuário1.close()
                with open(f'{caminho}/{nome_usuário1}', 'w', encoding='UTF-8') as usuário2:
                    usuário2.write(copiar)
                usuário2.close()
            usuário.close()
            if os.path.exists(f'{caminho}/{nome_usuário}'):
                os.remove(f'{caminho}/{nome_usuário}')
            dados_concluído = 'S'
            break
        if dados_concluído == 'S':
            break
#complementar()
