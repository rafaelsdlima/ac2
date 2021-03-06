from app.models import ParametrosCalculo, Calculadora
from app.utils import Impressora
import sys

def main():
    print('Bem vindo a calculadora')
    operacao = input('Insira a operação que deseja realizar: ')
    param1 = int(input('Insira o parametro 1 para sua operação: '))
    param2 = int(input('Insira o parametro 1 para sua operação: '))

    parametros = ParametrosCalculo(operacao, param1, param2)
    resultado = Calculadora().preparar(parametros).calcular()

    impr = Impressora()
    resultado_formatado = impr.formatar_resultado(parametros, resultado)
    print(resultado_formatado)


if __name__ == '__main__':
    main()


'''if __name__ == '__main__':
    operacao = sys.argv[1]
    if operacao == '+':
        print()
    if operacao == '-':
        print(1-1)
    if operacao == '*':
        print(1*1)
    if operacao == '/':
        print(2//1)
'''