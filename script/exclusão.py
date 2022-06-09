def excluir():
    while True:
        import os
        from script.configuração import config1,config2
        caminho = config1(1) # Caminho da pasta do currículo
        ids_currículos = config1(2) # Mostra uma listas de todos os currículos
        opção = ''
        while True:
            print('-' * 30)
            print(ids_currículos)
            print('-' * 30)
            opção = str(input('Digite o ID a ser apagado, [0] Voltar: ')).strip()
            id_currículo = config2(3,opção)
            if opção == '0':
                break
            elif opção.isnumeric() == True and opção in id_currículo:
                print('-' * 30)
                opção_confirma = str(input(f'Posso confirmar para apagar o currículo [S/N], \'{id_currículo}\': ')).strip().upper()[0]
                if opção_confirma == 'S':
                    if os.path.exists(f'{caminho}/{id_currículo}'):
                        os.remove(f'{caminho}/{id_currículo}')
                        print(f'{id_currículo}, currículo removido com sucesso')
                        break
                elif opção_confirma == 'N':
                    print('-' * 30)
                    print('Escolha outro ID')
                    break
            else:
                print('-' * 30)
                print(f'Valor incorreto, não tem ID com esse número {opção}!')
        if opção == '0':
            break
#excluir()
def excluir1(a):
    import os
    from script.configuração import config1,config2
    caminho = config1(1) # Caminho da pasta do currículo
    ids_currículos = config1(2) # Mostra uma listas de todos os currículos
    if a in ids_currículos:
        if os.path.exists(f'{caminho}/{a}'):
            os.remove(f'{caminho}/{a}')
