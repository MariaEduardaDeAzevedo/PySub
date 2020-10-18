# PySub 📨

[🇧🇷 Versão em português](#Guia-de-envio)  
[🇺🇸 English version](#Send-guide)

# Guia de Envio

### Visão geral 👀
Primeiramente, você tem que ter recebido do destinatário um projeto chamado **send**. Dentro desse diretório, você encontrará os seguintes arquivos:

1.   **pysub.py** é o arquivo que vai interagir com o usuário. É nele que se encontram todas as funcionalidades da aplicação.
2. **functions.py** tem a implementação das funcionalidades de envio.
3. **.to_config.json** é o arquivo de configuração que seu destinatário pré-configurou com as informações de envio.

### Como enviar?  📨
1.  Dentro do diretório **send**, chame o seguinte comando:
```
python3 pysub.py init from-config
```
A entrada irá pedir seu email e seu identificador. Atente para a seção [specification](#specification) para que os coloque no modelo que seu destinatário deseja.
Após isso, será criado um arquivo **.from_config.json** que irá armazenar suas informações.

2.  Atente para a criação de uma **pasta compactada (em .zip)** contendo o que é desejado submeter. O padrão de nome do arquivo compacado deve ser **seu_identificador.zip**, caso contrário, o PySub não encontrará seu arquivo de submissão.

3. Mova o seu arquivo .zip para o diretório **send** e chame o comando
   ```
   python3 pysub.py send
   ```
   Digite a senha do seu email colocado no .from-config.json. Sua submissão será concluída após esse passo.
   
   
# Send guide

### Overview 👀
First, you must have received from your recipient a project named **send**. Inside the directory you will find:

1.   **pysub.py** is the file who will interact with the user.
2. **functions.py** has all functionalities implementations.
3. **.to_config.json** is the recipien file config, with the information you need to submit your files.

### How to send? 📨
1.  Inside the **send** director, type the command:
```
python3 pysub.py init from-config
```
You must input your email and id. Check the [specification](#specification) section to see the recipient requirements.

A **.from_config.json** file will be created and keep all information you need to send.

2.  You must create a **zip file** with the submition content. The name template is **your_id.zip**, otherwise PySub can't find the submition file.

3. Move your file **your_id**.zip to the **send** directory and type the command:
   ```
   python3 pysub.py send
   ```
   Type your email password and the submition is finished. 

## specification
