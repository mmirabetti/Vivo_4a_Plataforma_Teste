from os.path import dirname, realpath, sep, pardir
import sys
sys.path.append(dirname(realpath(__file__)) + sep + ".." + sep)
from algoritmo_ex1 import *


def test_005_vetor_elem_fora_faixa():
    A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    resultado_esperado = str({0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1,
                             8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1,
                             15: 1})
    str_resultado = ex1_Vivo(A)
    assert str_resultado == resultado_esperado
