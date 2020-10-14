from Servicos import ConversorDollar as USD
from Servicos import ConversorEuro as EUR
from Servicos import ConversorBitcoin as BTC
from Servicos import ConversorLibraEsterlina as GBP
from Servicos import ConversorReal as BRL

def PesoParaReal(pValor):
    return pValor * 0.07

def PesoParaDollar(pValor):
    return pValor / (USD.DollarParaReal(1) * BRL.RealParaPeso(1))

def PesoParaEuro(pValor):
    return (pValor / ((EUR.EuroParaDollar(1) * USD.DollarParaReal(1)) * BRL.RealParaPeso(1)))

def PesoParaLibra(pValor):
    return ( pValor / (GBP.LibraParaReal(1)  * BRL.RealParaPeso(1)))    

def PesoParaBitcoin(pValor):
    return (pValor / ((BTC.BitcoinParaDollar(1) * USD.DollarParaReal(1)) * PesoParaReal(1))/100)        
    