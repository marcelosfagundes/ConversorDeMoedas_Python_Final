from Controladores import  ControladorBitcoin as ControlBitcoin
from Controladores import ControladorDollar as ControlDollar
from Controladores import ControladorEuro as ControlEuro
from Controladores import ControladorLibraEsterlina as ControlLibraEsterlina
from Controladores import ControladorPeso as ControlPeso
from Controladores import ControladorReal as ControlReal

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
