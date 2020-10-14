from Servicos import ConversorPeso as ARS

def RetornarCambio(moedaDestino, Valor): 
    if moedaDestino == 1  : 
        return ARS.PesoParaDollar(Valor)
    elif moedaDestino == 2  : 
        return ARS.PesoParaReal(Valor)
    elif moedaDestino == 3  : 
        return Valor
    elif moedaDestino == 4 : 
        return ARS.PesoParaEuro(Valor)
    elif moedaDestino == 5  : 
        return ARS.PesoParaLibra(Valor)
    elif moedaDestino == 6  : 
        return ARS.PesoParaBitcoin(Valor)