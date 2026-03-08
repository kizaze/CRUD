"""Configuración de fixtures para las pruebas."""
import json
import pytest

FILE_PATH = "products.json"


@pytest.fixture(autouse=True)
def reset_products_file():
    """Resetea el archivo products.json antes y después de cada test."""
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump([], f)
    yield
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump([], f)
