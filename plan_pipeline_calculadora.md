# Plan de Implementación: CI Pipeline con GitHub Actions — Calculadora

> **Actividad académica teórico-práctica**
> Pipeline de Pruebas Continuas para el proyecto `calculadora_pipeline`

---

## Contexto

Este plan es independiente del ejercicio TDD anterior.
Se crea una nueva carpeta `calculadora_pipeline` con su propio código y pruebas, y se configura un pipeline de integración continua usando **GitHub Actions** que se activa en cada `push` o `pull_request`.

---

## Estructura de archivos a crear

```
tu-repositorio/
├── .github/
│   └── workflows/
│       └── pipeline.yml            # Definición del pipeline CI
└── calculadora_pipeline/
    ├── requirements.txt            # Dependencias del proyecto
    ├── src/
    │   └── calculadora.py          # Código fuente de la calculadora
    └── tests/
        └── test_calculadora.py     # Pruebas unitarias
```

---

## PASO 1 — Crear la carpeta y el código fuente

### Instrucciones para el agente

1. Crear la carpeta `calculadora_pipeline/src/`.
2. Crear la carpeta `calculadora_pipeline/tests/`.
3. Crear los archivos que se detallan a continuación.

---

### Archivo: `calculadora_pipeline/src/calculadora.py`

```python
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
```

---

### Archivo: `calculadora_pipeline/tests/test_calculadora.py`

```python
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
```

---

### Archivo: `calculadora_pipeline/requirements.txt`

```
pytest==8.1.1
pytest-cov==5.0.0
```

---

## PASO 2 — Crear el archivo `__init__.py` necesario

### Instrucciones para el agente

Crear los siguientes archivos vacíos para que Python reconozca los módulos correctamente:

```
calculadora_pipeline/src/__init__.py       # archivo vacío
calculadora_pipeline/tests/__init__.py     # archivo vacío
```

---

## PASO 3 — Crear el pipeline de GitHub Actions

### Instrucciones para el agente

1. Crear la carpeta `.github/workflows/` en la raíz del repositorio (si no existe).
2. Crear el archivo `pipeline.yml` con el contenido siguiente.

---

### Archivo: `.github/workflows/pipeline.yml`

```yaml
name: Pipeline de Pruebas Continuas

on: [push, pull_request]  # Se activa en cada push o PR

jobs:
  pruebas:
    runs-on: ubuntu-latest  # Máquina virtual limpia en la nube

    steps:
      - uses: actions/checkout@v3  # Descarga el código del repo

      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Instalar dependencias
        run: pip install -r calculadora_pipeline/requirements.txt  # Instala librerías

      - name: Ejecutar pruebas unitarias
        run: pytest --cov=calculadora_pipeline/src calculadora_pipeline/tests/  # Corre pytest y mide cobertura

      - name: Mostrar reporte de cobertura
        run: pytest --cov=calculadora_pipeline/src --cov-report=term-missing calculadora_pipeline/tests/
```

---

## PASO 4 — Verificación local antes de hacer push

### Instrucciones para el agente

Ejecutar los siguientes comandos desde la raíz del repositorio para confirmar que todo funciona antes de subir a GitHub:

```bash
# 1. Instalar dependencias localmente
pip install -r calculadora_pipeline/requirements.txt

# 2. Correr las pruebas con cobertura
pytest --cov=calculadora_pipeline/src calculadora_pipeline/tests/ -v

# 3. Ver reporte de líneas no cubiertas
pytest --cov=calculadora_pipeline/src --cov-report=term-missing calculadora_pipeline/tests/
```

### Salida esperada local

```
calculadora_pipeline/tests/test_calculadora.py::TestCalculadora::test_sumar_positivos     PASSED
calculadora_pipeline/tests/test_calculadora.py::TestCalculadora::test_sumar_negativo      PASSED
calculadora_pipeline/tests/test_calculadora.py::TestCalculadora::test_restar              PASSED
calculadora_pipeline/tests/test_calculadora.py::TestCalculadora::test_restar_resultado_negativo PASSED
calculadora_pipeline/tests/test_calculadora.py::TestCalculadora::test_multiplicar         PASSED
calculadora_pipeline/tests/test_calculadora.py::TestCalculadora::test_multiplicar_por_cero PASSED
calculadora_pipeline/tests/test_calculadora.py::TestCalculadora::test_dividir             PASSED
calculadora_pipeline/tests/test_calculadora.py::TestCalculadora::test_dividir_por_cero    PASSED

---------- coverage: calculadora_pipeline/src/calculadora.py ----------
Name                                Stmts   Miss  Cover
-------------------------------------------------------
calculadora_pipeline/src/calculadora.py    12      0   100%

8 passed in 0.XXs
```

---

## PASO 5 — Subir a GitHub y verificar el pipeline

### Instrucciones para el agente

```bash
# Desde la raíz del repositorio
git add .
git commit -m "feat: agrega calculadora_pipeline con CI/CD en GitHub Actions"
git push origin main
```

Luego, en GitHub:

1. Ir a la pestaña **Actions** del repositorio.
2. Confirmar que el workflow **"Pipeline de Pruebas Continuas"** aparece en ejecución.
3. Verificar que todos los pasos terminan con ✅ verde.

---

## Resumen de la estructura final

```
tu-repositorio/
├── .github/
│   └── workflows/
│       └── pipeline.yml            ← Pipeline CI (se ejecuta en GitHub)
│
├── calculadora_tdd/                ← Ejercicio TDD anterior (no se toca)
│   ├── calculadora.py
│   └── test_calculadora.py
│
└── calculadora_pipeline/           ← Nuevo proyecto con CI
    ├── requirements.txt
    ├── src/
    │   ├── __init__.py
    │   └── calculadora.py
    └── tests/
        ├── __init__.py
        └── test_calculadora.py
```

---

## Qué hace cada parte del pipeline

| Paso del pipeline              | Qué hace                                                         |
|-------------------------------|------------------------------------------------------------------|
| `on: [push, pull_request]`    | Se dispara automáticamente en cada push o apertura de PR        |
| `runs-on: ubuntu-latest`      | Levanta una máquina virtual Linux limpia en los servidores de GitHub |
| `actions/checkout@v3`         | Clona el código del repositorio en esa máquina                  |
| `actions/setup-python@v4`     | Instala Python 3.11 en la máquina virtual                       |
| `pip install -r requirements` | Instala pytest y pytest-cov                                     |
| `pytest --cov=src tests/`     | Corre todas las pruebas y mide cobertura de código              |
| `--cov-report=term-missing`   | Muestra qué líneas no están cubiertas por pruebas               |

> **Resultado esperado:** cada vez que se haga un `push` al repositorio, GitHub ejecuta automáticamente las pruebas. Si alguna falla, el pipeline reporta ❌ y bloquea el merge del PR.
