from json_post_request_ex2 import *


def test_004_vetor_todos_elementos():
    vetor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    resultado_esperado = {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1,
                          '6': 1, '7': 1, '8': 1, '9': 1, '10': 1, '11': 1,
                          '12': 1, '13': 1, '14': 1, '15': 1}
    resp = json_post_request_ex2(vetor)
    if resp.status_code != 200:
        print('Teste 004 - Ex2 - falhou com status code da resposta %s'
              % resp.status_code)
        return 'fail', resp.elapsed.total_seconds()
    else:
        assert resp.json()["resultado"] == resultado_esperado
        print('Teste 004 - Ex2 - passou.')
        return 'pass', resp.elapsed.total_seconds()


if __name__ == '__main__':
    test_004_vetor_todos_elementos()
