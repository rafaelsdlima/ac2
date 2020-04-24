import sys
from app.models import ParametrosCalculo


class Impressora(object):
    def formatar_resultado(self, parametros_calculos: ParametrosCalculo,
                           resultado: int) -> str:
        p = parametros_calculos
        return f'Calculo ({p.operacao}) para {p.parametro1} e {p.parametro2} efetuado. Resultado == {resultado}'


    def imprimir(self, texto):
        try:
            indice = list(sys.argv).index("-v")
            if(indice > -1):
                print(texto)
        except:
            pass
