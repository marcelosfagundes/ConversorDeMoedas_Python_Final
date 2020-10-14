from Servicos import ConversorDollar as USD
from Servicos import ConversorReal as BRL
from Servicos import ConversorEuro as EUR
from Servicos import ConversorBitcoin as BTC

def LibraParaDollar(pValor):
    return (7.24 / USD.DollarParaReal(1)) * pValor   

def LibraParaReal(pValor):
     return pValor * 7.24

def LibraParaPeso(pValor):
    return pValor * (LibraParaReal(1) * BRL.RealParaPeso(1))  

def LibraParaEuro(pValor):
    return pValor * ((LibraParaReal(1) / USD.DollarParaReal(1) ) / EUR.EuroParaDollar(1))


def LibraParaBitcoin(pValor):
    return pValor / ((BTC.BitcoinParaDollar(1) * USD.DollarParaReal(1)) / LibraParaReal(1))

