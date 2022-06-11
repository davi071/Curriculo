import os # Importa o sistema
def config(): # Configurando caminhos
    while True:
        while True: # Para cada atualização
            fim = 0 # Para manter sempre nesse while para sempre atualizar
            pasta_config = 0 # Variável de se houver a pasta 'Configuração' = 1, se não = 0
            caminho_absoluto = os.getcwd() # Mostra aonde esta o caminho da raiz do programa
            pasta0 = os.listdir(f'{caminho_absoluto}\script') # Gera uma lista dos arquivos e pasta neste caminho
            for arquivos in pasta0: # Lista de arquivos e pasta dentro do 'script'
                if 'Configuração' in arquivos: # Procura a pasta Configuração
                    pasta_config = 1 # Se tiver a pasta ele retorna '1'
            if pasta_config == 0: # Ele vai gerar a pasta se não tiver
                os.makedirs(f'{caminho_absoluto}\script\Configuração') # Criando a pasta vazia
                break
            elif pasta_config == 1: # Ele vai verificar se tem o arquivo 'configuração.txt'
                pasta = f'{caminho_absoluto}\script\Configuração' # O nome do novo caminho agora é \script\Configuração
                dir_config = os.listdir(pasta) # Gera arquivos dentro da pasta 'Configuração'
                arquivo_config = 0 # Variável de se houver o arquivo 'configuração.txt' = 1, se não = 0
                for arquivos in dir_config:
                    if 'configuração.txt' in arquivos:
                        arquivo_config = 1 # Confirma que tem um arquivo chamado 'configuração.txt' dentro da pasta de Configuração
                if arquivo_config == 0: # Se não tiver ele vai criar
                    with open(f'{pasta}\configuração.txt', 'w', encoding='utf-8') as criar_config:
                        criar_config.close()
                elif arquivo_config == 1: # Se tiver o arquivo ele vai ler o diretório da pasta currículo
                    arquivo_config1 = 0
                    for arquivos in dir_config: # Gera uma lista de arquivos dentro da pasta 'Configuração'
                        if 'configuração.txt' in arquivos: # Procura o arquivo 'configuração'
                            with open(f'{pasta}\configuração.txt', 'r', encoding='utf-8') as config:
                                texto = config.readlines()
                            for linha in texto:
                                if 'Versão:' in linha:
                                    arquivo_config1 += 1
                                if 'Diretório01:' in linha:
                                    arquivo_config1 += 1
                    if arquivo_config1 == 0: # Se não houver nada ele vai verificar se existe a pasta onde sera armazenado os currículos e pegar o caminho
                        armazenamento_currículo = os.listdir(caminho_absoluto) # Gera uma lista raiz
                        if 'currículos' in armazenamento_currículo:
                            variável = 'ok'
                        else:
                            os.makedirs(f'{caminho_absoluto}\currículos') # Gerando pasta
                            break
                        with open(f'{pasta}\configuração.txt', 'a', encoding='utf-8') as add:
                            add = add.write(f'Versão:4.0.2\n')
                    pasta1 = 'script\Configuração'
                    fim = 1 # Ultima variável de confirmação de que tudo esta ok
            break
        if fim == 1:
            break
    return pasta1  # Retorna o caminho da pasta 'Configuração'
#config()
###############################################################################################
def config1(code): # Tratamento de dados dos currículos
    code # Valor a receber
    from datetime import date
    a = config() # Pedido do caminho do arquivo 'configuração.txt' dentro da pasta 'Configuração'
    with open(f'{a}/configuração.txt', 'r', encoding='utf-8') as config1:
        config2 = config1.readlines() # Usando para o tratamentos de linhas individuais
    # Coletando dados dentro do arquivo configuração.txt
    versão = '' # Armazena a versão atual
    caminho = os.getcwd()
    dir1_config = f'{caminho}\currículos' # Armazena o diretório dos currículos
    for arquivos in config2:
        if 'Versão:' in arquivos: # Copiar a versão
            versão += arquivos[7:-1]
    # Dados dentro da pasta de currículos
    id_completo = '' # Retorna todos os IDs (Com e sem #)
    id_completo0 = '' # Nome do ultimo ID (Com ou sem #)
    id_completo1 = '' # Nome de todos os Ids (Sem #)
    id_completo2 = '' # Nome de todos os Ids (Com #)
    id_completo3 = '' # Nome do ultimo ID (Com #)
    ids = sorted([]) # Armazena todos os 'Ids' em uma lista
    ids0 = sorted([]) # Armazena todos os 'Ids' com '#'
    ids1 = sorted([]) # Armazena todos os 'IDs' sem '#'
    maior = 0 # Armazena o maior 'ID' gerado
    menor = 0 # Armazena o menor 'ID' para gerar
    nomes = '' # Armazena apenas os nomes dos usuários (Com ou sem #)
    data = f'{date.today().day}/{date.today().month}/{date.today().year}'
    # Coleta dados dentro da pasta currículos
    lista_arquivos = os.listdir(dir1_config) # Gera uma lista com todos os arquivos da pasta currículo
    for arquivos in lista_arquivos: # Pega o ultimo nome do currículo (Com ou sem #)
        if 'ID' in arquivos:
            id_completo0 = arquivos
    for arquivos in lista_arquivos: # Pega o ultimo nome do currículo (Com #)
        if '#ID' in arquivos:
            id_completo3 = arquivos
    for arquivos in lista_arquivos: # Retorna listas de ids conforme o pedido
        if 'ID' in arquivos: # Coleta todos os nomes de IDS (Com ou sem #)
            barra = '\n' if arquivos != id_completo0 else '' # Ultimo faz com que não pule linha ids com ou sem #
            id_completo += f'{arquivos}{barra}' # Soma todos os nomes de currículos
            dado0 = arquivos.find('ID') # Mostra a posição do incio do 'ID'
            dado1 = arquivos.find('@') # Mostra a posição do inicio do '@'
            dado2 = arquivos.find('.txt') # Mostra a posição do incio do '.txt'
            ids += [arquivos[(dado0 + 2):dado1]] # Soma todos os IDs em uma lista
            id0 = int(arquivos[(dado0 + 2):dado1]) # Coleta todos os IDs em números
            if id0 > maior: # Coleta o maior ID gerado
                maior = id0
            nomes += f'{arquivos[(dado1 + 1):dado2]}{barra}' # Coleta todos os nomes
        if '#' not in arquivos and 'ID' in arquivos: # Coleta todos os Ids sem '#'
            id_completo1 += f'{arquivos}{barra}'
            dado0 = arquivos.find('#ID')
            dado1 = arquivos.find('@')
            ids1 += [int(arquivos[(dado0 + 3):dado1])]
        if '#ID' in arquivos: # Coletas todos os nomes de IDs somente com '#'
            barra1 = '\n' if arquivos != id_completo3 else '' # Ultimo faz com que não pule linha ids com #
            id_completo2 += f'{arquivos}{barra1}'
            dado0 = arquivos.find('#ID')
            dado1 = arquivos.find('@')
            ids0 += [arquivos[(dado0 + 3):dado1]]
    
    n = maior # Armazena o menor número não registrado nos Ids
    for a in range(1, maior + 1):
        if str(a) not in ids: # Se tiver um número faltando ele registra o menor
            if a < n:
                menor1 = a
                menor = menor1 - 1 # Reajuste
                n = menor # A cada contagem reatualizar
        else:
            menor = n # Se não tiver nenhum número faltando ele continua com o ultimo
    biblioteca = f'{versão}',f'{dir1_config}',f'{id_completo}',f'{id_completo1}',f'{ids}',f'{maior}',f'{menor}',f'{nomes}',f'{id_completo2}',f'{ids0}',f'{ids1}',f'{data}' # Retorna para outros lugares com dados prontos
    # Biblioteca:(0 = versão),(1 = Caminho dos currículos),(2 = lista de todos os currículos (Com ou sem #)),(3 = lista de todos os currículos (Sem #)),
    #(4 = Mostra uma lista de todos os Ids),(5 = Mostra o maior ID registrado),( 6 = Mostra o menor número não registrado),(7 = Mostra apenas os nomes dos currículos),
    #(8 = lista de todos os currículos (Com #)),(9 = Lista de todos os 'IDs' somente com '#'),(10 = Lista de todos os 'IDs' sem nenhum '#'),(11 = Retorna a data do dia)
    #print(biblioteca[8]) # Para testes
    return biblioteca[code] # Valor a retornar
#config1('') # Para testes
###########################################################################################################
def config2(a,b): # Retorna IDs individuais
    # 'a' = O função que você quer 'b' o usuário quer você quer
    caminho = config1(1)
    lista_arquivos = os.listdir(caminho)
    nome_completo = '' # Armazena o nome completo (Com #)
    nome_completo1 = '' # Armazena o nome completo (Sem #)
    id_completo = '' # Armazena o ID completo (Com #)
    id_completo1 = '' # Armazena o ID completo (Sem #)
    for arquivos in lista_arquivos: # Arquivos com #
        if f'#ID{b}@' in arquivos:
            id_completo = arquivos # Retorna o ID completo
            dado0 = arquivos.find('@')
            dado1 = arquivos.find('.txt')
            nome_completo += arquivos[(dado0 + 1):dado1] # Retorna o nome completo
    for arquivos in lista_arquivos: # Arquivos sem #
        if f'ID{b}@' in arquivos:
            id_completo1 += arquivos # Retorna o ID completo
            dado0 = arquivos.find('@')
            dado1 = arquivos.find('.txt')
            nome_completo1 += arquivos[(dado0 + 1):dado1] # Retorna o nome completo
    biblioteca = f'{nome_completo}', f'{nome_completo1}', f'{id_completo}', f'{id_completo1}'
    # (0 = Retorna o nome com #)(1 = Retorna o nome com/sem #)(2 = Retorna ID completo com/sem #)(3 = Retorna ID completo com #)
    #print(biblioteca[a]) # Para testes
    return biblioteca[a]
#config2() # Para testes
