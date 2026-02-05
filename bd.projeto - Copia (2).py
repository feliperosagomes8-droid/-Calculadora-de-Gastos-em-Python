def menu():
     # São todas variáveis para somar os gastos saindo de um ponto de partida
    fixo = 0
    contas_aleatorias = 0
    lazer = 0
    todas_contas=0
     #É  um loop para o menu ficar rodando
    while True:
        print('\n--- CONTROLE FINANCEIRO ---')
        print('1. Contas fixas')
        print('2. Contas aleatórias')
        print('3. Lazer')
        print('4.somar contas')
        print('5. Sair')
     #É  uma variavel para saber qual operação o usuário irá querer realizar 
        escolha = input('Qual operação você deseja realizar? ')
     # É uma condição quando aperto a opção 1
        if escolha == '1':
            try:
                quantidade=int(input('Quantas contas fixas você quer somar agora?'))
                for i in range(quantidade):
                    valor = float(input(f"Digite o valor da conta{i+1}: R$"))
                    fixo += valor
                    print(f"O valor de contas fixas são {fixo:.2f}")
            except:
                print('Você digitou algo errado!!')
    # É uma condição quando aperto a opção 2
        elif escolha == '2':
            try:
                aleatórias=int(input('Quantas contas aleatórias você quer somar agora?'))
                for a in range(aleatórias):
                    valor2=float(input(f"Digite o valor da conta {a+1}: R$ "))
                    contas_aleatorias+=valor2
                    print(f"O valor de contas aleatórias são {contas_aleatorias:.2f} R$ ")
            except:
                print('Erro')

     # É uma condição quando aperto a opção 3
        elif escolha == '3':
            try:
                lazer_prazer = int(input('Quantas contas de lazer você quer somar agora?'))
                for b in range(lazer_prazer):
                    valor3=float(input(f"Digite o valor da conta {b+1}: R$"))
                    lazer+=valor3
                    print(f"O valor de contas de lazer são {lazer:.2f} R$ ")
            except:
                print('Você digitou algo errado!!')

    # É uma condição quando aperto a opção 4
        elif escolha == '4':
            total=fixo+contas_aleatorias+lazer
            print(f'\n--- RELATÓRIO TOTAL ---')
            print(f'Fixo: R$ {fixo:.2f} | Aleatório: R$ {contas_aleatorias:.2f} | Lazer: R$ {lazer:.2f}')
            print(f'>> TOTAL GERAL: R$ {total:.2f}')
            print(todas_contas)
        elif escolha=='5':
            print('Saindo do programa...')
            quit()
        else:
            print('Opção inválida! Escolha entre 0 e 4.')
    
            
menu()
                    