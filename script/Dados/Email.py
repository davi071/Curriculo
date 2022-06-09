def email(email):
    while True: # Coletar dados de Email
        print('-' * 30)
        email = str(input('Informe o seu Email, ou opção [0] não tem: ')).strip().lower()
        while True:
            print('-' * 30)
            email = 'Não tenho' if email == '0' else email
            email_confirmar = str(input(f'Posso confirmar para {email}, [S/N]: ')).strip().upper()[0]
            if email_confirmar == 'S':
                email = 0 if email == 'Nenhum' else email
                break
            elif email_confirmar == 'N':
                print('-' * 30)
                print(f'Por favor, informe o novo Email!')
                break
            else:
                print('-' * 30)
                print('Valor incorreto!')
        if email_confirmar == 'S':
            break
    return email
