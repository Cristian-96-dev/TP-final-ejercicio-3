import unittest
from utils import calcular_emisiones_carbono

class TestCalculoEmisiones(unittest.TestCase):
    
    def test_exactitud_valores_nominales(self):
        consumo_nominal = 300
        emision_esperada = 120.0

        resultado_obtenido = calcular_emisiones_carbono(consumo_nominal)
        self.assertEqual(resultado_obtenido, emision_esperada, "El calculo de emisiones es incorrecto.")

    def test_excepcion_consumo_fuera_rango(self):
            consumo_invalido = -50  
            with self.assertRaises(ValueError):
                calcular_emisiones_carbono(consumo_invalido)
    


