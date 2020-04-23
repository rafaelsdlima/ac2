from app.models import ParametrosCalculo, Calculadora


def main():
    print('Seja bem vindo à calculadora xyz')
    operacao = input('Insira a operação que deseja realizar: ')
    param1 = int(input('Insira o parametro 1 para sua operação: '))
    param2 = int(input('Insira o parametro 1 para sua operação: '))

    parametros = ParametrosCalculo(operacao, param1, param2)
    resultado = Calculadora().preparar(parametros).calcular()

    print(f'sucesso, resultado => {resultado}')


if __name__ == '__main__':
    main()
