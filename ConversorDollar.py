import ConversorLibraEsterlina as GBP
import ConversorReal as BRL

def DollarParaReal(pValor):
    return pValor * 5.65

def DollarParaPeso(pValor): 
    return pValor * (DollarParaReal(1) * BRL.RealParaPeso(1))  

def DollarParaEuro(pValor):
    return  pValor * 1.18   

def DollarParaLibra(pValor):
    return pValor * (DollarParaReal(1) / GBP.LibraParaReal(1))

def DollarParaBitcoin(pValor):
    return (pValor/10700.00)


  