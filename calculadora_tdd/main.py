import subprocess
import sys
import os


def ejecutar_tests(fase: str):
    ruta_fase = os.path.join(os.path.dirname(__file__), fase)
    
    print(f"\n{'='*50}")
    print(f"  EJECUTANDO TESTS - FASE {fase.upper()}")
    print(f"{'='*50}\n")
    
    resultado = subprocess.run(
        [sys.executable, "-m", "pytest", "test_calculadora.py", "-v"],
        cwd=ruta_fase
    )
    
    return resultado.returncode


def menu():
    while True:
        print("\n" + "="*50)
        print("      CALCULADORA TDD - SELECCIONAR FASE")
        print("="*50)
        print("1. Fase RED   (pruebas fallan)")
        print("2. Fase GREEN (pruebas pasan - código mínimo)")
        print("3. Fase REFACTOR (pruebas pasan - código mejorado)")
        print("4. Salir")
        print("-"*50)
        
        opcion = input("Selecciona una opción [1-4]: ").strip()
        
        fases = {
            "1": "red",
            "2": "green",
            "3": "refactor"
        }
        
        if opcion in fases:
            ejecutar_tests(fases[opcion])
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()