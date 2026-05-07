# Plan de Implementación: TDD — Calculadora Simple en Python

> **Actividad académica teórico-práctica**
> Ciclo completo: Red → Green → Refactor

---

## Contexto y objetivo

Implementar una calculadora simple en Python siguiendo estrictamente el ciclo TDD:

1. **Red** — Escribir una prueba que falla (el código aún no existe).
2. **Green** — Escribir el mínimo código necesario para que la prueba pase.
3. **Refactor** — Mejorar el código sin cambiar su comportamiento, garantizando que las pruebas sigan pasando.

---

## Estructura de archivos

```
calculadora_tdd/
├── red/
│   ├── calculadora.py       # Código vacío (sin implementación)
│   └── test_calculadora.py  # Pruebas unitarias con pytest
├── green/
│   ├── calculadora.py       # Código mínimo funcional
│   └── test_calculadora.py  # Pruebas unitarias con pytest
└── refactor/
    ├── calculadora.py       # Código mejorado con type hints y validación
    └── test_calculadora.py  # Pruebas unitarias con pytest
```

---

## Operaciones a cubrir

| Operación   | Método         | Ejemplo               |
|-------------|----------------|-----------------------|
| Suma        | `sumar`        | `sumar(2, 3)` → `5`   |
| Resta       | `restar`       | `restar(5, 2)` → `3`  |
| Multiplicar | `multiplicar`  | `multiplicar(3, 4)` → `12` |
| Dividir     | `dividir`      | `dividir(10, 2)` → `5.0` |
| División por cero | `dividir` | `dividir(5, 0)` → `ValueError` |

---

## FASE 1 — RED (La prueba falla)

### Objetivo

En esta fase se escribe la prueba antes que el código. La prueba describe el comportamiento esperado, pero como el código no existe aún, **todas las pruebas deben fallar**.

### Instrucciones

1. Crear `test_calculadora.py` con las pruebas usando pytest
2. Crear `calculadora.py` vacío (solo la clase sin métodos)
3. Ejecutar las pruebas: `python -m pytest test_calculadora.py -v`
4. Confirmar que **8 pruebas fallan**

### Archivo: `test_calculadora.py` (RED)

```python
import pytest
from calculadora import Calculadora


class TestCalculadora:
    @pytest.fixture
    def calc(self):
        return Calculadora()

    def test_sumar_dos_numeros_positivos(self, calc):
        resultado = calc.sumar(2, 3)
        assert resultado == 5

    # ... (8 pruebas en total)
```

### Archivo: `calculadora.py` (RED — vacío)

```python
class Calculadora:
    pass
```

### Salida esperada

```
FAILED test_calculadora.py::TestCalculadora::test_sumar_dos_numeros_positivos
FAILED test_calculadora.py::TestCalculadora::test_sumar_con_numero_negativo
FAILED test_calculadora.py::TestCalculadora::test_restar_dos_numeros
...
8 failed, 0 passed
```

> ✅ **Verificación RED:** Todas las pruebas deben estar en estado FAILED antes de continuar.

---

## FASE 2 — GREEN (Código mínimo para pasar las pruebas)

### Objetivo

Escribir solo el código necesario para que las pruebas pasen. No se debe agregar funcionalidad extra, solo lo indispensable.

### Instrucciones

1. Reemplazar `calculadora.py` con la implementación mínima
2. Ejecutar las pruebas: `python -m pytest test_calculadora.py -v`
3. Confirmar que **8 pruebas pasan**

### Archivo: `calculadora.py` (GREEN — implementación mínima)

```python
class Calculadora:

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        return a / b
```

### Salida esperada

```
PASSED test_calculadora.py::TestCalculadora::test_sumar_dos_numeros_positivos
PASSED test_calculadora.py::TestCalculadora::test_sumar_con_numero_negativo
PASSED test_calculadora.py::TestCalculadora::test_restar_dos_numeros
...
8 passed, 0 failed
```

> ✅ **Verificación GREEN:** Todas las pruebas deben estar en estado PASSED antes de continuar.

---

## FASE 3 — REFACTOR (Mejorar sin romper nada)

### Objetivo

Mejorar la estructura interna del código (legibilidad, type hints, validación) sin cambiar el comportamiento externo. Las pruebas deben seguir pasando.

### Instrucciones

1. Reemplazar `calculadora.py` con la versión refactorizada
2. Ejecutar las pruebas **sin modificar `test_calculadora.py`**
3. Confirmar que **8 pruebas siguen pasando**

### Mejoras aplicadas

- **Type hints** para documentar tipos de entrada y salida
- **Docstrings** en cada método para claridad
- **Validación de tipos** en método privado (`_validar_numeros`)
- **Mensaje de excepción** más descriptivo

### Archivo: `calculadora.py` (REFACTOR)

```python
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
```

### Salida esperada

```
PASSED test_calculadora.py::TestCalculadora::test_sumar_dos_numeros_positivos
PASSED test_calculadora.py::TestCalculadora::test_sumar_con_numero_negativo
PASSED test_calculadora.py::TestCalculadora::test_restar_dos_numeros
...
8 passed, 0 failed
```

> ✅ **Verificación REFACTOR:** Todas las pruebas deben seguir en estado PASSED. El comportamiento externo no cambió.

---

## Resumen del ciclo TDD

| Fase      | Estado de pruebas | Objetivo                                      |
|-----------|-------------------|-----------------------------------------------|
| RED       | ❌ 8 FAILED       | La prueba existe, el código no               |
| GREEN     | ✅ 8 PASSED       | Código mínimo funciona                       |
| REFACTOR  | ✅ 8 PASSED       | Código limpio, tipado y documentado          |

> **Regla de oro del TDD:** `test_calculadora.py` **nunca se modifica** durante las fases GREEN y REFACTOR. Solo se modifica en RED para agregar nuevas pruebas.

---

## Conceptos clave demostrados

- **Red:** La prueba describe el comportamiento esperado antes de que exista implementación. Falla porque el código no existe aún.
- **Green:** Se escribe solo lo indispensable para satisfacer la prueba. No se anticipa lógica futura.
- **Refactor:** Se mejora la estructura interna (legibilidad, tipos, validación) sin alterar el contrato público de la clase. Las pruebas son el guardián del comportamiento.

---

## Comandos para ejecutar las pruebas

```bash
# En la carpeta de cada fase (red, green, refactor)
cd calculadora_tdd/red
python -m pytest test_calculadora.py -v
```