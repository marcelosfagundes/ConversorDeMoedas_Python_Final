from Servicos import ConversorReal as BRL

def RetornarCambio(moedaDestino, Valor): 
    if moedaDestino == 1  : 
        return BRL.RealParaDollar(Valor)
    elif moedaDestino == 2  : 
        return Valor
    elif moedaDestino == 3  : 
        return BRL.RealParaPeso(Valor)
    elif moedaDestino == 4 : 
        return BRL.RealParaEuro(Valor)
    elif moedaDestino == 5  : 
        return BRL.RealParaLibra(Valor)
    elif moedaDestino == 6  : 
        return BRL.RealParaBitcoin(Valor)