from Controladores import Controlador as Control

opçãoOrigem=0
while opçãoOrigem != 7:
    print('**************************************************')
    print('*            CONVERSOR DE MOEDAS                 *')
    print('**************************************************')
    print('*          ESCOLHA AS OPÇÕES ABAIXO:             *')
    print('**************************************************')
    print('''
    [ 1 ] DOLAR DOS ESTADOS UNIDOS - (USD) 
    [ 2 ] REAL - (BRL) 
    [ 3 ] PESO ARGENTINO - (ARS) 
    [ 4 ] EURO - (EUR) 
    [ 5 ] LIBRA ESTERLINA - (GBP) 
    [ 6 ] BITCOIN - (BTC) 
    [ 7 ] Sair''')

    try:
      opçãoOrigem  = int(input('Conversão de:'))

      if opçãoOrigem == 7:exit()
    
      opçãoDestino = int(input('Para: '))
      Valor = float(input('Valor a converter:'))
      
      if Valor > 0 :Control.Controller(opçãoOrigem, opçãoDestino, Valor)
      else:print('O Valor digitado é inválido!')
    except ValueError:
        print('ATENÇÃO: Ocorreu problema ao tentar realizar a conversão, \n verifique os parâmetros de entrada e tente novamente!')
      


