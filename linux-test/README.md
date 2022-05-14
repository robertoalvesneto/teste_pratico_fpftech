## 1- programas utilizados
Como o objetivo era testar a experiência em linux, tudo dessa questão foi feito usando
o terminal com os seguintes programas:
- **tilix:** emulador de terminal
- **vim:** para a criar e editar os arquivos de texto, tanto o readme.md quanto os scripts
- **cfiles:** para simplificar a visualização dos diretórios

![Isso é uma imagem](/assets/terminal.png)

## 2- Como rodar
Existem dois scripts diferentes, ambos fazem a mesma coisa, mas de formas diferentes:
- `simplescript.sh`: executa apenas os comandos solicitados, de forma simples e objetiva faz o que foi pedido;
- `script.sh`: script um pouco mais complexo e organizado, apresentando as seguintes diferenças:
	- organiza as tarefas a fazer em funções, para deixar o entendimento mais organizado;
	- apresenta mensagens para o usuário para ele saber o que está sendo feito a cada momento;
	- tenta verificar se o unzip está instalado, se não estiver, ele mesmo instala (funciona com distros derivadas do debian e redhat);
	- faz uma busca pelos nomes de arquivos nos diretorios, para conseguir extrair e mover qualquer arquivo, não só os com nomes presetadoss;

Confira se os arquivos possuem permissão de execução `chmod +x *.sh`

Depois basta digitar no terminal `./[script_name]`

## 3- Importante:
### 3.1. ERRO COM O LINK:
O link para download do zip:
> https://vanilton.net/v1/download/zip.zip

Não estava funcionando, estava exibindo mensagem de erro ao acessar, então usei o site
do google fonts e escolhi o arquivo zip da fonte **Roboto** para baixar e descompactar por terminal

### 3.2. RESTRIÇÕES DO SCRIPT:
Os scripts criados e descritos nas seções seguintes criaram os diretorios a partir do seu path original de onde foi invocado,
ou seja, se digitar `./~/Documentos/test-fpf/linux-test/simplescript.sh` o diretorio *roberto* sera criado na raiz, já se rodar
dentro do ultimo dir `./simplescript.sh` sera criado em *linux-test* mesmo.
