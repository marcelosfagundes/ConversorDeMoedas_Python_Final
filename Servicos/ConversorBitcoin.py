from Servicos import ConversorDollar as USD
from Servicos import ConversorPeso as ARS
from Servicos import ConversorEuro as EUR
from Servicos import ConversorLibraEsterlina as GBP


def BitcoinParaDollar(pValor):
    return pValor * 10700.00       

def BitcoinParaReal(pValor):
    return pValor * (BitcoinParaDollar(1) * USD.DollarParaReal(1))

def BitcoinParaPeso(pValor):
    return pValor * ( BitcoinParaDollar(1) * USD.DollarParaReal(1) * ARS.PesoParaReal(1))  

def BitcoinParaEuro(pValor):
    return pValor * ( BitcoinParaDollar(1) / EUR.EuroParaDollar(1))     

def BitcoinParaLibra(pValor):
    return pValor * (( BitcoinParaDollar(1)) / ( GBP.LibraParaReal(1) / USD.DollarParaReal(1) ))     

