#####################   TESTE CAIXA BRANCA  #####################

###O caminho do sys.path.append está estático para efetuar os testes.
###linha 7 os.path.dirname(os.path.realpath(__file__))

import sys
sys.path.append("/home/rafael/Área de Trabalho/Arquitetura_de_software/ac2/")
from app.models import ParametrosCalculo, Soma, Subtracao, Multiplicacao, Divisao
from app.utils import Impressora
import pytest


def teste_parametro_calculo():
    return ParametrosCalculo('soma', 1, 2)
    assert ParametrosCalculo('soma', 1, 2)


def teste_soma():
    assert Soma(2,2).calcular() == 4


def teste_subtracao():
    assert Subtracao(2,2).calcular() == 0


def teste_multiplicacao():
    assert Multiplicacao(1,2).calcular() == 2


def teste_divisao():
    assert Divisao(4,2).calcular() == 2
