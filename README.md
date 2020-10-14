ConversorDeMoedas_Python_Final

upload dos arquivos de conversão de moedas escrito em Python

O Projeto para conversão de moedas foi desenvolvido em python 3.8.3, tem como objetivo principal realizar a conversão do cambio sobre determinadas moedas, como:

Dolar Americano(USD)
Real (BRL)
Peso (ARS)
Euro (EUR)
Libra Esterlina (GBP)
Bitcoin (BTC)
O resultado da conversão está com base nas seguintes cotações:

1.0 USD = 5.65 BRL 1.0 ARS = 0.07 BRL 1.0 EUR = 1.18 USD 1.0 GBP = 7.24 BRL 1.0 BTC = 10700.0 USD

*** A conversão poderá ser feita entre qualquer moeda, mesmo que na base não haja a conversão direta, exemplo "obter 10 USD em GBP".

*************************************************************************************

Estrutura do projeto:

* Controladores - conjunto de pacotes responsáveis para fazer a ponte entre o input e output das informações.
* Serviços - pacotes responsáveis para devolver para o usuário a conversão
* TesteUnitario - TDD das funções de serviços.
* Principal - View

*************************************************************************************
Execução do sistema:

Para executar o conversor de moedas, baixe o projeto do github para sua máquina
No prompt de comando, digite : python principal.py
Foram criados os testes unitários das formulas das conversões, para executar digite: python -m unittest
