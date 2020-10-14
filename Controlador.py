import ControladorBitcoin as ControlBitcoin
import ControladorDollar as ControlDollar
import ControladorEuro as ControlEuro
import ControladorLibraEsterlina as ControlLibraEsterlina
import ControladorPeso as ControlPeso
import ControladorReal as ControlReal

ValorConversao = 0

def Controller(moedaOrigem, moedaDestino, Valor):
    if moedaOrigem == 1  : 
        ValorConversao = ControlDollar.RetornarCambio(moedaDestino, Valor)
    elif moedaOrigem == 2  : 
        ValorConversao = ControlReal.RetornarCambio(moedaDestino, Valor)    
    elif moedaOrigem == 3  : 
        ValorConversao = ControlPeso.RetornarCambio(moedaDestino, Valor)    
    elif moedaOrigem == 4 : 
        ValorConversao = ControlEuro.RetornarCambio(moedaDestino, Valor)    
    elif moedaOrigem == 5  : 
        ValorConversao = ControlLibraEsterlina.RetornarCambio(moedaDestino, Valor) 
    elif moedaOrigem == 6  : 
        ValorConversao = ControlBitcoin.RetornarCambio(moedaDestino, Valor)
       
    return print('Resultado da conversão::  %4.2f'%ValorConversao)              
