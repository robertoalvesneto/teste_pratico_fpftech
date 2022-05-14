## Descrição:
O problema pede para testarmos as requisições para uma api feita em django.


## Análise do problema:
Primeiramente foi feita uma analise do problema e da API, a partir do qual, foi
gerado um relatório, disponível no caminho `relatorio/relatorio.pdf`, no qual
explico a minha estratégia de teste e o arquivo `documentacaoApi.md` com uma
documentação simples da API.

## Dependências:
1. POSTMAN

## Executar:
1. Subir o docker conforme foi ensinado no github `https://github.com/Vanilton18/loja-api.git`;
   - a API fica disponivel em: `http://localhost:8000`

2. Importar no Postman a coleção `store-api.postman_collection.json`;

3. Apertar em `run collection`

## Conclusão:
No arquivo log/store-api.postman_test_run.json pode ser encontrado um logo do
conjunto de teste realizado, nele vemos que apenas quem falhou foi as análises
de quantidade negativa e quantidade inteira:

![Isso é uma imagem](/assets/log_test_api.png)

Valores negativos e valores com casas decimais não estão sendo tratados.