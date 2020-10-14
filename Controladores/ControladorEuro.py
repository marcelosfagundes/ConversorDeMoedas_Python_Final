from Servicos import ConversorEuro as EUR

def RetornarCambio(moedaDestino, Valor): 
    if moedaDestino == 1  : 
        return EUR.EuroParaDollar(Valor)
    elif moedaDestino == 2  : 
        return EUR.EuroParaReal(Valor)
    elif moedaDestino == 3  : 
        return EUR.EuroParaPeso(Valor)
    elif moedaDestino == 4 : 
        return Valor
    elif moedaDestino == 5  : 
        return EUR.EuroParaLibra(Valor)
    elif moedaDestino == 6  : 
        return EUR.EuroParaBitcoin(Valor)