# Teste para novos Desenvolvedores
## Telefônica Vivo - 4th Plataforma – Versão 2.0 - 2020
## Exercício 1
1. Enunciado: Uma imagem bitmap pode ser representada como uma matriz de dimensões M x N, em que cada posição da matriz pode assumir um valor inteiro dentro de um intervalo. Construa um algoritmo que receba como entrada um Vetor A[N] em que An ∈ { 0, 1, 2,..., 15 }. A saída do seu algoritmo deve ser uma String indicando a quantidade de vezes que cada An foi encontrado na matriz de bitmap. No caso em que algum elemento não tenha sido encontrado, o algoritmo deve retornar que a quantidade é zero para aquele elemento. O formato da String é livre.

2. Considerações
* O entendimento do enunciado sugere que o Vetor A[N] represente uma imagem de dimensões M x N (uma matriz "desenrolada" em formato de vetor), com codificação de cores em 4 bits (de 0 a 16), e que o algoritmo deve analisar a quantidade de cada elemento de cor (An) presente na imagem.
* O formato da String retornado é o mesmo da estrutura de dados dicionário, da linguagem Python, onde cada valor é associado a uma chave única. Neste caso, as chaves são cada um dos elementos da faixa de 0 a 15, e os valores, as quantidades de "pixels" da cor representada pela chave presentes na imagem

3. Requisitos: A implementação do algoritmo foi baseada unicamente no core da linguagem Python, sem uso de módulos externos. Para os testes funcionais, o único requisito é o pacote pytest.

4. Coding style: O código foi desenvolvido usando as regras PEP8

5. Testes funcionais: Para a realização dos testes, basta executar o comando
```shell
pytest testes
```
