from Servicos import ConversorDollar as USD
from Servicos import ConversorReal as BRL
from Servicos import ConversorLibraEsterlina as GBP
from Servicos import ConversorBitcoin as BTC

def EuroParaDollar(pValor):
    return pValor * 1.18    

def EuroParaReal(pValor) :
    return pValor * (EuroParaDollar(1) * USD.DollarParaReal(1))   

def EuroParaPeso(pValor) :
    return pValor * (EuroParaDollar(1) * USD.DollarParaReal(1) * BRL.RealParaPeso(1))       

def EuroParaLibra(pValor) :
    return pValor * ((EuroParaDollar(1) * USD.DollarParaReal(1)) /  GBP.LibraParaReal(1)) 

def EuroParaBitcoin(pValor) :
    return pValor / (BTC.BitcoinParaDollar(1) / EuroParaDollar(1))