def criar_currículo():
    from script.configuração import config1
    from script.passo2 import complementar
    while True:
        caminho = config1(1) # Caminho da pasta do currículo
        nomes = config1(7)
        print('-' * 30)
        usuário = str(input('Nome completo: ')).strip().title()
        if usuário in nomes:
            while True:
                print('-' * 30)
                print(f'{usuário}, já tem um nome igual!')
                usuário0 = str(input('Deseja salvar mesmo assim,[S/N]: ')).strip().upper()[0]
                if usuário0 == 'S':
                    print('-' * 30)
                    print(f'Vamos separar {usuário}, apenas pelo número do ID!')
                    break
                elif usuário0 == 'N':
                    break
                else:
                    print('-' * 30)
                    print('Valor incorreto!')
        else:
            while True:
                usuário0 = str(input(f'O nome esta correto [S/N], {usuário}: ')).strip().upper()[0]
                if usuário0 == 'S':
                    break
                elif usuário0 == 'N':
                    break
                else:
                    print('-' * 30)
                    print('Valor incorreto!')
        if usuário0 == 'S':
            print(f'\nO nome de usuário agora é {usuário}')
            break
    id1 = int(config1(6)) # Menor ID para ser registrado valido
    id0 = 1 # ID do currículo, se não tiver nenhum
    while id0 <= id1:
        id0 += 1
    with open(f'{caminho}/#ID{id0}@{usuário}.txt', 'w') as adicionar: # Gerar arquivos .txt, já nomeados
        adicionar.write(f'ID:{id0}\nNome:{usuário}\n') # Dentro do arquivo sera adicionado ID e Nome
        print('-' * 30)
        print('\033[32mCurrículo criado com sucesso\033[m') # Confirmação que foi criado
    adicionar.close() # Fecha o arquivo .txt (precalçam)
    while True:
        print('-' * 30)
        opção1 = str(input('Continuar com os dados?\033[33m[S/N]\033[m: ')).strip().upper()[0] # Opção do usuário para continuar a escrever o currículo
        if opção1 == 'S':
            a = f'#ID{id0}@{usuário}.txt' # Nome de usuário 'Com #'
            b = f'{id0}' # ID gerado
            complementar(a,b)
            break
        elif opção1 == 'N':
            break
        else:
            print('-' * 30)
            print('Valor incorreto!')
#criar_currículo()
