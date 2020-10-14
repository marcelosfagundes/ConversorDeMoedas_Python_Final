import ConversorBitcoin as Bitcoin

def RetornarCambio(moedaDestino, Valor): 
    if moedaDestino == 1  : 
        return Bitcoin.BitcoinParaDollar(Valor)
    elif moedaDestino == 2  : 
        return Bitcoin.BitcoinParaReal(Valor)
    elif moedaDestino == 3  : 
        return Bitcoin.BitcoinParaPeso(Valor)
    elif moedaDestino == 4 : 
        return Bitcoin.BitcoinParaEuro(Valor)
    elif moedaDestino == 5  : 
        return Bitcoin.BitcoinParaLibra(Valor)
    elif moedaDestino == 6  : 
        return Valor