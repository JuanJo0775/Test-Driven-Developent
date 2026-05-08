class Calculadora:
    """Calculadora simple con operaciones aritméticas básicas."""

    def sumar(self, a: float, b: float) -> float:
        """Retorna la suma de a y b."""
        return a + b

    def restar(self, a: float, b: float) -> float:
        """Retorna la diferencia de a menos b."""
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        """Retorna el producto de a por b."""
        return a * b

    def dividir(self, a: float, b: float) -> float:
        """
        Retorna el cociente de a entre b.
        Lanza ValueError si b es cero.
        """
        if b == 0:
            raise ValueError(f"División por cero: no se puede dividir {a} entre 0")
        return a / b