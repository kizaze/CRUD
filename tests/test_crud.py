"""Pruebas unitarias para el módulo CRUD de productos."""
import crud


def test_create_product():
    """Verifica que se puede crear un producto correctamente."""
    product = {"id": 1, "name": "Laptop", "price": 1200}
    result = crud.create_product(product)
    assert result["name"] == "Laptop"
    assert result["id"] == 1
    assert result["price"] == 1200


def test_read_products():
    """Verifica que se pueden leer los productos."""
    products = crud.read_products()
    assert isinstance(products, list)


def test_read_products_after_create():
    """Verifica que los productos creados aparecen al leer."""
    product = {"id": 2, "name": "Mouse", "price": 25}
    crud.create_product(product)
    products = crud.read_products()
    assert len(products) >= 1
    assert any(p["name"] == "Mouse" for p in products)


def test_update_product():
    """Verifica que se puede actualizar un producto existente."""
    product = {"id": 1, "name": "Laptop", "price": 1200}
    crud.create_product(product)
    updated = crud.update_product(1, {"price": 1000})
    assert updated is not None
    assert updated["price"] == 1000


def test_update_product_not_found():
    """Verifica que update retorna None si el producto no existe."""
    result = crud.update_product(999, {"price": 500})
    assert result is None


def test_delete_product():
    """Verifica que se puede eliminar un producto."""
    product = {"id": 1, "name": "Laptop", "price": 1200}
    crud.create_product(product)
    result = crud.delete_product(1)
    assert result is True
    products = crud.read_products()
    assert not any(p["id"] == 1 for p in products)


def test_delete_product_not_found():
    """Verifica que delete retorna False si el producto no existe."""
    result = crud.delete_product(999)
    assert result is False
