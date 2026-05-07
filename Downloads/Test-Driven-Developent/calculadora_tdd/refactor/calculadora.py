class Calculadora:
    """
    Calculadora simple con operaciones aritméticas básicas.
    Implementada con TDD: Red → Green → Refactor.
    """

    def _validar_numeros(self, a, b) -> None:
        """Valida que los argumentos sean valores numéricos."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Los operandos deben ser números")

    def sumar(self, a: float, b: float) -> float:
        """Retorna la suma de a y b."""
        self._validar_numeros(a, b)
        return a + b

    def restar(self, a: float, b: float) -> float:
        """Retorna la diferencia de a menos b."""
        self._validar_numeros(a, b)
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        """Retorna el producto de a por b."""
        self._validar_numeros(a, b)
        return a * b

    def dividir(self, a: float, b: float) -> float:
        """
        Retorna el cociente de a entre b.
        Lanza ValueError si b es cero.
        """
        self._validar_numeros(a, b)
        if b == 0:
            raise ValueError(f"División por cero: no se puede dividir {a} entre 0")
        return a / b