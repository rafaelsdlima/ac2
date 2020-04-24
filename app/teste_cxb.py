#####################   TESTE CAIXA BRANCA  #####################
import sys
from .models import ParametrosCalculo, Operacao, Soma, Subtracao, Multiplicacao, Divisao, FabricaOperacoes

def test_soma():
    assert Soma(1,1) == 2

def test_subtracao():
    assert Subtracao(1,1) == 0

def test_multiplicacao():
    assert Multiplicacao(1,2) == 2

def test_divisao():
    assert Divisao(10,5) == 2