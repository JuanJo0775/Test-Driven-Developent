# Casos de Prueba - Calculadora TDD

## Información General

| Campo | Valor |
|-------|-------|
| **Proyecto** | Calculadora Simple |
| **Enfoque** | Test-Driven Development (TDD) |
| **Framework de pruebas** | pytest |
| **Lenguaje** | Python |

---

## Casos de Prueba

### 1. test_sumar_dos_numeros_positivos

| Atributo | Descripción |
|----------|-------------|
| **ID** | TC-001 |
| **Nombre** | Sumar dos números positivos |
| **Método** | `sumar(2, 3)` |
| **Resultado esperado** | `5` |
| **Descripción** | Verifica que la calculadora pueda sumar correctamente dos números enteros positivos |

---

### 2. test_sumar_con_numero_negativo

| Atributo | Descripción |
|----------|-------------|
| **ID** | TC-002 |
| **Nombre** | Sumar con número negativo |
| **Método** | `sumar(-1, 4)` |
| **Resultado esperado** | `3` |
| **Descripción** | Verifica que la calculadora maneje correctamente números negativos en la suma |

---

### 3. test_restar_dos_numeros

| Atributo | Descripción |
|----------|-------------|
| **ID** | TC-003 |
| **Nombre** | Restar dos números |
| **Método** | `restar(10, 4)` |
| **Resultado esperado** | `6` |
| **Descripción** | Verifica que la calculadora pueda restar correctamente dos números |

---

### 4. test_restar_resultado_negativo

| Atributo | Descripción |
|----------|-------------|
| **ID** | TC-004 |
| **Nombre** | Restar con resultado negativo |
| **Método** | `restar(2, 7)` |
| **Resultado esperado** | `-5` |
| **Descripción** | Verifica que la calculadora maneje correctamente resultados negativos en la resta |

---

### 5. test_multiplicar_dos_numeros

| Atributo | Descripción |
|----------|-------------|
| **ID** | TC-005 |
| **Nombre** | Multiplicar dos números |
| **Método** | `multiplicar(3, 4)` |
| **Resultado esperado** | `12` |
| **Descripción** | Verifica que la calculadora pueda multiplicar correctamente dos números |

---

### 6. test_multiplicar_por_cero

| Atributo | Descripción |
|----------|-------------|
| **ID** | TC-006 |
| **Nombre** | Multiplicar por cero |
| **Método** | `multiplicar(5, 0)` |
| **Resultado esperado** | `0` |
| **Descripción** | Verifica que cualquier número multiplicado por cero sea cero |

---

### 7. test_dividir_dos_numeros

| Atributo | Descripción |
|----------|-------------|
| **ID** | TC-007 |
| **Nombre** | Dividir dos números |
| **Método** | `dividir(10, 2)` |
| **Resultado esperado** | `5.0` |
| **Descripción** | Verifica que la calculadora pueda dividir correctamente dos números |

---

### 8. test_dividir_por_cero_lanza_excepcion

| Atributo | Descripción |
|----------|-------------|
| **ID** | TC-008 |
| **Nombre** | Dividir por cero lanza excepción |
| **Método** | `dividir(5, 0)` |
| **Resultado esperado** | `ValueError` |
| **Descripción** | Verifica que la calculadora lance una excepción cuando se intenta dividir por cero |

---

## Matriz de Cobertura

| Operación | Casos positivos | Casos extremos | Casos de error |
|-----------|-----------------|----------------|----------------|
| Sumar | TC-001 | TC-002 | - |
| Restar | TC-003 | TC-004 | - |
| Multiplicar | TC-005 | TC-006 | - |
| Dividir | TC-007 | - | TC-008 |

---

## Cómo ejecutar las pruebas

```bash
# Ejecutar todas las pruebas con verbose
python -m pytest test_calculadora.py -v

# Ejecutar con coverage
python -m pytest test_calculadora.py --cov

# Ejecutar un test específico
python -m pytest test_calculadora.py::TestCalculadora::test_sumar_dos_numeros_positivos -v
```