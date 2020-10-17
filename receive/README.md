# PySub 📨

[🇧🇷 Versão em português](#Guia-de-recebimento)  

# Guia de Recebimento

###Visão geral 👀
Primeiramente, você tem que clonar todo esse repositório, do seguinte modo:

```
git clone https://github.com/MariaEduardaDeAzevedo/PySub.git
```

O diretório mais importante para você será o **receive**. Nele é possível encontrar o seguinte:

1.   **pysub.py** é o arquivo que vai interagir com o usuário. É nele que se encontram todas as funcionalidades da aplicação.
2. **functions.py** tem a implementação das funcionalidades de envio.
3. **files** é um diretório vazio que só será preenchido no momento que forem consultadas as submissões.

### Configurando o ambiente  📨
1.  Dentro do diretório **receive**, chame o seguinte comando:
```
python3 pysub.py init to-config
```
A entrada irá pedir seu email, o assunto que deverá nomear os emails dos remetentes e uma possível data limite de submissão. 
Após isso, será criado um arquivo** .to_config.json** no seu diretório atual e no diretório **send** que irá armazenar as informações de envio.

2.  Envie para seus remetentes o projeto da pasta **send**. Com isso, eles irão poder submeter os arquivos para seu endereço.

### Recebendo direto na sua máquina  📨

1. Na pasta **receive**, rode o seguinte comando:
```
python3 pysub.py received
```

2. Será pedido que sua senha para o email de submissão seja digitada. Com isso, você poderá receber de forma direta todas as submissões em seu email.

3. Haverá a criação de dois arquivos .txt: RECEIVED.txt e ERROR.txt. O primeiro listará todas as submissões que foram efetuadas com sucesso e a segunda as que deram errado. Na pasta files estarão listados todos os arquivos das submissões. 
