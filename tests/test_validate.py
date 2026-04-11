import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from validate import validar_nombre, validar_edad, validar_correo

def test_nombre_vacio() -> None:
    """Verifica que un nombre vacío retorne False."""
    ok, _ = validar_nombre("")
    assert ok == False


def test_nombre_valido() -> None:
    """Verifica que un nombre válido retorne True."""
    ok, _ = validar_nombre("Sebastián Zuleta Echavarría")
    assert ok == True


def test_edad_invalida() -> None:
    """Verifica que una edad con letras retorne False."""
    ok, _ = validar_edad("abc")
    assert ok == False


def test_correo_invalido() -> None:
    """Verifica que un correo sin formato válido retorne False."""
    ok, _ = validar_correo("correosinformato")
    assert ok == False


