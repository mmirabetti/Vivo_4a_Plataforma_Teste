from os.path import dirname, realpath, sep, pardir
import sys
sys.path.append(dirname(realpath(__file__)) + sep + ".." + sep)
from algoritmo_ex1 import *


def test_008_vetor_elem_misturados_II():
    A = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15,
         15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 0, 1]
    resultado_esperado = str({0: 1, 1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,
                              8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0,
                              15: 27})
    str_resultado = ex1_Vivo(A)
    assert str_resultado == resultado_esperado
