from Servicos import ConversorPeso as ARS
from Servicos import ConversorEuro as EUR
from Servicos import ConversorDollar as USD
from Servicos import ConversorBitcoin as BTC

def RealParaDollar(pValor):
    return pValor / 5.65

def RealParaPeso(pValor):
    return pValor / ARS.PesoParaReal(1)

def RealParaEuro(pValor):
    return pValor/ (EUR.EuroParaDollar(1) * USD.DollarParaReal(1)) 

def RealParaLibra(pValor):
    return pValor / 7.24

def RealParaBitcoin(pValor):
    return pValor / (BTC.BitcoinParaDollar(1) * USD.DollarParaReal(1))          




