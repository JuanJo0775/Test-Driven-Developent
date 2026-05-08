import sys
import os
import pytest

# Permite importar desde src/ sin instalar el paquete
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculadora import Calculadora


class TestCalculadora:

    def setup_method(self):
        self.calc = Calculadora()

    def test_sumar_positivos(self):
        assert self.calc.sumar(2, 3) == 5

    def test_sumar_negativo(self):
        assert self.calc.sumar(-1, 4) == 3

    def test_restar(self):
        assert self.calc.restar(10, 4) == 6

    def test_restar_resultado_negativo(self):
        assert self.calc.restar(2, 7) == -5

    def test_multiplicar(self):
        assert self.calc.multiplicar(3, 4) == 12

    def test_multiplicar_por_cero(self):
        assert self.calc.multiplicar(5, 0) == 0

    def test_dividir(self):
        assert self.calc.dividir(10, 2) == 5.0

    def test_dividir_por_cero(self):
        with pytest.raises(ValueError):
            self.calc.dividir(5, 0)