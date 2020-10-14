from Servicos import ConversorLibraEsterlina as GBP

def RetornarCambio(moedaDestino, Valor): 
    if moedaDestino == 1  : 
        return GBP.LibraParaDollar(Valor)
    elif moedaDestino == 2  : 
        return GBP.LibraParaReal(Valor)
    elif moedaDestino == 3  : 
        return GBP.LibraParaPeso(Valor)
    elif moedaDestino == 4 : 
        return GBP.LibraParaEuro(Valor)
    elif moedaDestino == 5  : 
        return Valor
    elif moedaDestino == 6  : 
        return GBP.LibraParaBitcoin(Valor) 