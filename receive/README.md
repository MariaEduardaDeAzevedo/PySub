# PySub 📨

[🇧🇷 Versão em português](#Guia-de-recebimento)  
[🇺🇸 English version](#receive-guide)
# Guia de Recebimento

### Visão geral 👀
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

# Receive Guide

### Overview 👀
First, you have to clone this repository:

```
git clone https://github.com/MariaEduardaDeAzevedo/PySub.git
```
The most important directory for you will be **receive**. Inside it you will find: 

1.   **pysub.py** is the file that will interact with the user. All application features are on it.
2. **functions.py** has all send features implemented.
3. **files** is an empty directory that will only be filled in when the submission is consulted.

### Setting the environment  📨
1. Inside **receive** directory, type the following command:
```
python3 pysub.py init to-config
```
Input will ask you for your email, subject that should name the sender's emails, and a possible deadline submission.
So it will be created a file **.to_config.json** on your actual directory and on **send** directory that is going to store the send information.

2. Send to all your senders your project from the **send** folder. They will be able to submit the files to your email address.

### Receiving right on your machine  📨

1. On the **receive** folder, run the following command:
```
python3 pysub.py received
```

2. You will be asked to enter your password for the submission email. With that, you will be able to receive directly all submission in your email.

3. It will be created two new .txt files: RECEIVED.txt and ERROR.txt. The first one is going to show all submissions that were successful e the second those that went wrong. On the **files** folder, all submissions files is gonna be there.