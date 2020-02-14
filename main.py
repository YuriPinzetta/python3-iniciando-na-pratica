import getpass
import os

clear = 'cls' if os.name == 'nt' else 'clear'

while True:
    account_typed = input('Digite o número da sua conta: ')
    password_typed = getpass.getpass('Digite a sua senha: ')
    print('**********************************************')
    print('****** School of Net - Caixa Eletrônico ******')
    print('**********************************************')
    print(account_typed)
    print(password_typed)

    account_list = {
        '0001-02': {
            'password': '123456',
            'name': 'Fulano da Silva',
            'value': 0,
            'admin': False
        },
        '0002-02': {
            'password': '123456',
            'name': 'Cicrano da Silva',
            'value': 0,
            'admin': False
        }
        ,
        '1111-11': {
            'password': '123456',
            'name': 'Admin da Silva',
            'value': 1000,
            'admin': True
        }
    }

    money_slips = {
        '20': 5,
        '50': 5,
        '100': 5,
    }

    if account_typed in account_list and password_typed == account_list[account_typed]['password']:
        os.system(clear)

        print('**********************************************')
        print('****** Bem Vindo - ' + account_list[account_typed]['name'] + ' ******')
        print('**********************************************')
        print('1 - Saldo')
        print('2 - Saque')
        if account_list[account_typed]['admin']:
            print('10 - Incluir cédulas')
        option_typed = input('Escolha uma das opções acima: ')
        if option_typed == '1':
            print('Seu saldo é %s' % account_list[account_typed]['value'])
        elif option_typed == '2':
            value_typed = input('Digite o valor a ser sacado: ')
            money_slips_user = {}
            value_int = int(value_typed)

            if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
                money_slips_user['100'] = value_int // 100
                value_int = value_int - value_int // 100 * 100

            if value_int // 50 > 0 and value_int // 50 <= money_slips['100']:
                money_slips_user['50'] = value_int // 50
                value_int = value_int - value_int // 50 * 50

            if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
                money_slips_user['20'] = value_int // 20
                value_int = value_int - value_int // 20 * 20

            if value_int != 0:
                print('O caixa não tem cédulas disponíveis para este valor')
            else:
                for money_bill in money_slips_user:
                    money_slips[money_bill] -= money_slips_user[money_bill]

                print('Pegue as notas:')
                print(money_slips_user)
        elif option_typed == '10' and account_list[account_typed]['admin']:
            amount_typed = input('Digite a quantidade de cédulas:')
            money_bill_typed = input('Digite a cédula a se incluida:')
            money_slips[money_bill_typed] += int(amount_typed)
            print(money_slips)
    else:
        print('Conta inválida')

    input('Precione <ENTER> para continuar...')

    os.system(clear)
