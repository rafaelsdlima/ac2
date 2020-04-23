import sys
from app.models import ParametrosCalculo


class Impressora(object):
    def formatar_resultado(self, parametros_calculos: ParametrosCalculos,
                           resultado: int) -> str:
        p = parametros_calculos
        return f'Calculo ({p.operacao}) para {p.parametro1} e {p.parametro2} efetuado. Resultado == {Resultado}'


def imprimir(self, texto):
    try:
        indice = list(sys.argv).index("-v")
        if(indice > -1):
            print(texto)
        except:
            pass
