Usei este algoritmo para criar 122 docx diferentes com base em uma planilha no excel. Censurei os dados por uma questão de segurança e privacidade da empresa.

![](https://github.com/LeonardoWaldomiro/redesigned-chainsaw/blob/main/download.png)

Basicamente o algoritmo cria um docx a partir de um template onde estão marcados os locais chaves que devem ser substituidos. Por exemplo como podemos ver abaixo há uma marcação para os campos {{CNPJ}} e {{endereço}}. O script identifica essas marcações, busca na planilha os dados para substituição, formata conforme o padrão que foi estabelecido e reescreve no template. Em seguida ele salva o documento com o nome sendo "{cnpj} - Declarações". Após realizar esse procedimento ele passa para a proxima linha da planilha e faz o mesmo até acabar.

![](https://github.com/LeonardoWaldomiro/redesigned-chainsaw/blob/main/download%20(1).png)

