from json_post_request_ex2 import *


def test_006_vetor_1_elem_repetido():
    vetor = [3, 3, 3]
    resultado_esperado = {'0': 0, '1': 0, '2': 0, '3': 3, '4': 0, '5': 0,
                          '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0,
                          '12': 0, '13': 0, '14': 0, '15': 0}
    resp = json_post_request_ex2(vetor)
    if resp.status_code != 200:
        print('Teste 006 - Ex2 - falhou com status code da resposta %s'
              % resp.status_code)
        return 'fail', resp.elapsed.total_seconds()
    else:
        assert resp.json()["resultado"] == resultado_esperado
        print('Teste 006 - Ex2 - passou.')
        return 'pass', resp.elapsed.total_seconds()


if __name__ == '__main__':
    test_006_vetor_1_elem_repetido()
