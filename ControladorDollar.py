import ConversorDollar as USD

def RetornarCambio(moedaDestino, Valor): 
    if moedaDestino == 1  : 
        return Valor
    elif moedaDestino == 2  : 
        return USD.DollarParaReal(Valor)
    elif moedaDestino == 3  : 
        return USD.DollarParaPeso(Valor) 
    elif moedaDestino == 4 : 
        return USD.DollarParaEuro(Valor)
    elif moedaDestino == 5  : 
        return USD.DollarParaLibra(Valor)
    elif moedaDestino == 6  : #VERIFICAR O CALCULO PARA BITCOIN
        return USD.DollarParaBitcoin(Valor)
