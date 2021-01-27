Usei este algoritmo para criar 122 docx diferentes com base em uma planilha no excel. Censurei os dados por uma questão de segurança e privacidade da empresa.

![](https://github.com/LeonardoWaldomiro/redesigned-chainsaw/blob/main/download.png)

Basicamente o algoritmo cria um docx a partir de um template onde estão marcados os locais chaves que devem ser substituidos. Por exemplo como podemos ver abaixo há uma parte escrita "{{CNPJ}}". O script identifica essas partes(no meu caso foram 3), formata conforme o padrão que foi estabelecido por mim e substitui conforme a linha da planilha que ele está trabalhando. O mesmo funciona para "{{Endereço}}".

![](https://github.com/LeonardoWaldomiro/redesigned-chainsaw/blob/main/download%20(1).png)

Após realizar esse processo, o arquivo é salvo no formato "CNPJ tal - Declarações". 

Por trabalhar linha a linha da planilha, usei a estrutura de repetição for indo de 0 a 122 e um except com print do cnpj caso dê problema ao salvar o arquivo. 


