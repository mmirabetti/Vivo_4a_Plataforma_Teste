def ex2_Vivo(vetor):
    """
    Telefônica Vivo - 4th Plataforma – Versão 2.0 - 2020
    Teste para novos Desenvolvedores
    Exercício 2
    """
    min = 0
    max = 15
    d = {k: 0 for k in range(min, max+1)}
    for i in vetor:
        try:
            d[i] += 1
        except LookupError as error:
            print(f'Erro: Valor do elemento do vetor não está entre {min} e \
                  {max}! ' + repr(error))
    return d
