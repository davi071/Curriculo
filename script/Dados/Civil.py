def estado_civil(civil):
    while True: # Coletar dados de Estado Civil
        print('-' * 30)
        civil = str(input('Informe o estado civil: ')).strip().title()
        while True:
            print('-' * 30)
            civil_confirmar = str(input(f'Posso confirmar para {civil}, [S/N]: ')).strip().upper()[0]
            if civil_confirmar == 'S':
                break
            elif civil_confirmar == 'N':
                print('-' * 30)
                print('Por favor, informe o novo estado civil!')
                break
            else:
                print('-' * 30)
                print('Valor incorreto!')
        if civil_confirmar == 'S':
            break
    return civil
