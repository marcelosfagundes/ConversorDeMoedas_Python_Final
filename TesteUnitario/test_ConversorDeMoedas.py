import unittest 
from Servicos import ConversorDollar as USD
from Servicos import ConversorReal as BRL
from Servicos import ConversorPeso as ARS
from Servicos import ConversorEuro as EUR
from Servicos import ConversorLibraEsterlina as GBP
from Servicos import ConversorBitcoin as BTC
import math as Math

class test_ValidarConversorDeMoedas(unittest.TestCase):
   #test das fórmulas de conversão do Dollar 
   def test_DollarParaReal(self):
      result = USD.DollarParaReal(2)
      expected = 11.30
      
      self.assertEqual(result, expected) 

   def test_DollarParaPeso(self):
      result = round(USD.DollarParaPeso(2),2)
      expected = 161.43
      
      self.assertEqual(result, expected)       

   def test_DollarParaEuro(self):
      result = USD.DollarParaEuro(3)
      expected = 3.54
      
      self.assertEqual(result, expected)       

   def test_DollarParaLibra(self):
      result = round(USD.DollarParaLibra(1.28),2)
      expected = 1
      
      self.assertEqual(result, expected)       

   def test_DollarParaBitcoin(self):
      result = round(USD.DollarParaBitcoin(21400),2)
      expected = 2.00

      self.assertEqual(result, expected)       

   #test das fórmulas de conversão do Real 
   def test_RealParaDollar(self):
      result = round(BRL.RealParaDollar(50.30),2)
      expected = 8.90

      self.assertEqual(result, expected)   

   def test_RealParaPeso(self):
      result = round(BRL.RealParaPeso(10.00),2)
      expected = 142.86

      self.assertEqual(result, expected)   

   def test_RealParaEuro(self):
      result = round(BRL.RealParaEuro(5.00),2)
      expected = 0.75      

      self.assertEqual(result, expected)           

   def test_RealParaLibra(self):
      result = round(BRL.RealParaLibra(60.00),2)
      expected = 8.29      

      self.assertEqual(result, expected)     

   def test_RealParaBitcoin(self):
      result = round(BRL.RealParaBitcoin(60455))
      expected = 1      

      self.assertEqual(result, expected)     

   #test das fórmulas de conversão do Peso 

   def test_PesoParaDollar(self):
      result = round(ARS.PesoParaDollar(60.00),2)
      expected = 0.74      

      self.assertEqual(result, expected)    


   def test_PesoParaReal(self):
      result =round( ARS.PesoParaReal(10.00),2)
      expected = 0.70      

      self.assertEqual(result, expected)    

   def test_PesoParaEuro(self):
      result = round(ARS.PesoParaEuro(100.00),2)
      expected = 1.05      

      self.assertEqual(result, expected)    

   def test_PesoParaLibra(self):
      result = round(ARS.PesoParaLibra(200.00),2)
      expected = 1.93      

      self.assertEqual(result, expected)  

   def test_PesoParaBitcoin(self):
      result = round(ARS.PesoParaBitcoin(800000),2)
      expected = 1.89      

      self.assertEqual(result, expected)   

   #test das fórmulas de conversão do Euro  
                   
   def test_EuroParaDollar(self):
      result = EUR.EuroParaDollar(1.00)
      expected = 1.18      

      self.assertEqual(result, expected)   

   def test_EuroParaReal(self):
      result = round(EUR.EuroParaReal(4.50), 2)
      expected = 30.00     

      self.assertEqual(result, expected)   

   def test_EuroParaLibra(self):
      result = round(EUR.EuroParaLibra(2),2)
      expected = 1.84     

      self.assertEqual(result, expected)  

   def test_EuroParaBitcoin(self):
      result = round(EUR.EuroParaBitcoin(60000),2)
      expected = 6.62    

      self.assertEqual(result, expected)   

   #test das fórmulas de conversão da Libra Esterlina  

   def test_LibraParaDollar(self):
      result =round(GBP.LibraParaDollar(1.00),2)
      expected = 1.28      

      self.assertEqual(result, expected)   

   def test_LibraParaReal(self):
      result = GBP.LibraParaReal(1.00)
      expected = 7.24     

      self.assertEqual(result, expected)        

   def test_LibraParaPeso(self):
      result =round(GBP.LibraParaPeso(5.00),2)
      expected = 517.14     

      self.assertEqual(result, expected)           

   def test_LibraParaEuro(self):
      result = round(GBP.LibraParaEuro(1.00),2)
      expected = 1.09     

      self.assertEqual(result, expected) 

   def test_LibraParaBitcoin(self):
      result = round(GBP.LibraParaBitcoin(10000),2)
      expected = 1.20     

      self.assertEqual(result, expected)    

   #test das fórmulas de conversão da Bitcoin

   def test_BitcoinParaDollar(self):
      result = BTC.BitcoinParaDollar(1.00)
      expected = 10700.00      

      self.assertEqual(result, expected)  

   def test_BitcoinParaReal(self):
      result = round(BTC.BitcoinParaReal(1.00),2)
      expected = 60455.00      

      self.assertEqual(result, expected) 

   def test_BitcoinParaPeso(self):
      result = round(BTC.BitcoinParaPeso(1.00),2)
      expected = 4231.85     

      self.assertEqual(result, expected) 

   def test_BitcoinParaEuro(self):
      result = round(BTC.BitcoinParaEuro(1.00),2)
      expected = 9067.80      

      self.assertEqual(result, expected)    

   def test_BitcoinParaLibra(self):
      result =round(BTC.BitcoinParaLibra(1.00),2)
      expected = 8350.14      

      self.assertEqual(result, expected)                                     

if __name__ == '__main__':
    unittest.main()
