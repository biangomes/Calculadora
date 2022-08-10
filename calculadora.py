def calculadora():   
    operation = input('''
    Digite a operação que deseja realizar:
    + para adição;
    - para subtração;
    * para multiplicação;
    / para divisão
    ''')


    x = int(input('Primeiro numero: '))
    y = int(input('Segundo numero: '))

    # Soma
    if operation == '+':
        print(f'{x} + {y} = {x + y}')

    # Diferenca
    elif operation == '-':   
        print(f'{x} - {y} = {x - y}')

    # Multiplicacao
    elif operation == '*':
        print(f'{x} x {y} = {x * y}')

    # Divisao
    elif operation == '/':
        print(f'{x} / {y} = {x + y}')

    else:
        print("Operação inválida! Por favor, tente novamente!")

    # Invoca a funcao novamente()
    novamente()


def novamente():
    calcular_novamente = input(''' 
    Você deseja calcular novamente?
    S - Sim
    N - Nao
    ''')

    if calcular_novamente.upper() == 'S':
        calculadora()
    elif calcular_novamente.upper() == 'N':
        print("FIM.")
    else:
        print("Opção inválida ......")
        novamente()

calculadora()