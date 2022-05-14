# API de produtos
A API pode ser acessada em: `http://localhost:8000`

## ENDPOINTS
### LISTAR PRODUTOS
**GET** `/produtos`

Retorna todos os produtos


### PEGAR UM PRODUTO
**GET** `/produtos/:id`

Retorna um produto em especifico

parametros:
- 'format': 'json'

### ADICIONAR PRODUTO
**POST** `/produtos/`

Adiciona um novo produto

Corpo da requisição:
- `nome`: string - required
- `preco`: float - required,
- `quantidade`: int,
- `categoria`: int - [1 - 10]

exemplo:
``` json
{
	"nome": "Mouse",
	"preco": "3.00",
	"quantidade": 2,
	"categoria": 1
}
```
