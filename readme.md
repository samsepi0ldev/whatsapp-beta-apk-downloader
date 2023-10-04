## Descrição

Este é um script Python que automatiza o processo de download da versão beta do WhatsApp a partir do site APKMirror. Ele utiliza várias bibliotecas Python, incluindo `requests`, `BeautifulSoup`, e `clint.textui`, para realizar essa tarefa. Abaixo, explicamos como usar o script e detalhamos seu funcionamento.

## Uso

1. Certifique-se de que você possui as bibliotecas necessárias instaladas. Você pode instalá-las executando o seguinte comando:
   ```shell
   pip install -r requirements.txt
   python wa_downloader.py
3. Execute o script Python. Ele iniciará o processo de download da versão beta do WhatsApp a partir do site APKMirror.

## Funcionamento
1. O script começa definindo a URL base (host) e os cabeçalhos de usuário para simular um navegador.

2. Em seguida, ele faz uma solicitação HTTP para a página inicial do WhatsApp Beta no APKMirror, analisa o conteúdo HTML da página com BeautifulSoup e encontra os links para diferentes versões do WhatsApp.

3. O script procura pelo link da versão beta do WhatsApp, identificando-o com a palavra-chave "beta" no texto do link.

4. Uma vez encontrado o link da versão beta, o script obtém a versão do WhatsApp a partir do texto do link.

5. O script segue para a página de download da versão beta do WhatsApp e extrai o link para fazer o download do arquivo APK.

6. Após obter o link de download, o script o analisa para encontrar o link direto para o arquivo APK.

7. Em seguida, ele inicia o processo de download do arquivo APK, mostrando o progresso com uma barra de progresso.

8. O arquivo APK é baixado para a pasta de trabalho com um nome que inclui a versão da aplicação.

Nota: Este script é específico para o site APKMirror e a estrutura das páginas desse site. Qualquer alteração na estrutura do site pode quebrar o funcionamento do script. Certifique-se de usá-lo de acordo com os termos de serviço do site APKMirror e para fins legais e éticos.