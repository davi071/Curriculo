def inicio():
    from script import passo1 # Chama o import do def 'criar_currículo'
    from script import passo2 # Chama o import do def 'Pegar os dados do usuário'
    from script import visualizar # Chama o import do def 'visualizar'
    from script import modificação # Chama o import do def 'modificação'
    from script import exclusão # Chama o import do def 'exclusão'
    from script.configuração import config1
    versão = config1(0)
    print('-=-' * 20)
    print('{}{:^46}'.format(versão,'Bem Vindo'))
    while True:
        print('-' * 60)
        opção = str(input('''                  O que você deseja fazer?
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
[ 0 ] Sair                      [ 3 ] Adicionar dados currículo
[ 1 ] Criar um arquivo          [ 4 ] Modificar um currículo
[ 2 ] Visualizar um currículo   [ 5 ] Excluir um currículo
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Digite aqui: '''))
        if opção == '0':
            sair = 0
            while True:
                print('-' * 34)
                opção1 = str(input('Tem certeza que quer sair, [S/N]: ')).strip().upper()[0]
                if opção1 == 'S':
                    sair = 1
                    break
                elif opção1 == 'N':
                    break
                else:
                    print('-' * 30)
                    print('Valor incorreto!')
            if sair == 1:
                break
        elif opção.isnumeric() == True:
            opção = int(opção)
            if opção == 1: # Chama função para Criar um arquivo .txt
                while True:
                    print('-' * 47)
                    opção1 = str(input('Tem certeza que quer criar um currículo, [S/N]: ')).strip().upper()[0]
                    if opção1 == 'S':
                        passo1.criar_currículo()
                        break
                    elif opção1 == 'N':
                        break
                    else:
                        print('-' * 15)
                        print('Valor Incorreto!')
            elif opção == 2: # Para visualizar um currículo
                visualizar.visualizar_currículo()
            elif opção == 3: # Para complementar um arquivo .txt
                passo2.complementar('','')
            elif opção == 4: # Adicionar dados ao currículo
                modificação.modificação()
            elif opção == 5: # Para Excluir um currículo
                exclusão.excluir()
        else:
            print('-' * 15)
            print('Valor incorreto')
    print('-' * 59)
    print('Programa fechado com sucesso')
    print('-=-' * 20)
inicio()
