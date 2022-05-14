## Descrição:
O problema pede para utilizar o selenium para testar uma aplicação frontend
disponível em `http://www.vanilton.net/triangulo/#` cujo intuito é fazer os
devidos testes para saber se a aplicação consegue definir corretamente o tipo
do triângulo.

## Análise do problema:
Primeiramente foi feita uma analise do problema e do site, a partir do qual, foi
gerado um relatório, disponível no caminho `relatorio/relatorio.pdf`, no qual
explico a minha estratégia de teste.

## Dependências:
1. PYTHON 3

Para o python são necessárias as bibliotecas `selenium` e `unittest`

2. DOCKER

Esse projeto usa selenium dentro do docker. Para rodar use o seguinte comando
para preparar o ambiente com o docker compose

``` bash
docker-compose -fd docker-compose.yml up
```

Quando terminar, use o mesmo comando com `down` no lugar do `up para finalizar`

## Executar:
1. Subir o docker com o comando dito acima;

    - é possível ver os containers no link: `http://localhost:4444/ui#`

2. Dando no terminal o comando `python3 main.py` é possível ver um 'teste rápido',
onde o site sera aberto, alguns dados seram passados e então devemos ver no
terminal uma saída, antes do mesmo finalizar

3. Para rodar os testes propriamente dito temos o comando
`python3 -m tests.triangle_test`

## Conclusão:
Os testes que passaram foram para definir o tipo do triângulo e quando não
inserimos algum dado.

A aplicação não consegue tratar caracteres não numéricos e também não verifica
se é um triângulo de verdade.