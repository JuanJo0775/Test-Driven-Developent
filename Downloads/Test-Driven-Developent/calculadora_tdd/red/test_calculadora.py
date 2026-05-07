import pytest
from calculadora import Calculadora


class TestCalculadora:
    @pytest.fixture
    def calc(self):
        return Calculadora()

    def test_sumar_dos_numeros_positivos(self, calc):
        resultado = calc.sumar(2, 3)
        assert resultado == 5

    def test_sumar_con_numero_negativo(self, calc):
        resultado = calc.sumar(-1, 4)
        assert resultado == 3

    def test_restar_dos_numeros(self, calc):
        resultado = calc.restar(10, 4)
        assert resultado == 6

    def test_restar_resultado_negativo(self, calc):
        resultado = calc.restar(2, 7)
        assert resultado == -5

    def test_multiplicar_dos_numeros(self, calc):
        resultado = calc.multiplicar(3, 4)
        assert resultado == 12

    def test_multiplicar_por_cero(self, calc):
        resultado = calc.multiplicar(5, 0)
        assert resultado == 0

    def test_dividir_dos_numeros(self, calc):
        resultado = calc.dividir(10, 2)
        assert resultado == 5.0

    def test_dividir_por_cero_lanza_excepcion(self, calc):
        with pytest.raises(ValueError):
            calc.dividir(5, 0)