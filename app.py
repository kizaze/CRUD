"""API REST para el CRUD de productos."""
from flask import Flask, request, jsonify
import crud

app = Flask(__name__)


@app.route("/products", methods=["GET"])
def get_products():
    """Obtiene todos los productos."""
    return jsonify(crud.read_products())


@app.route("/products", methods=["POST"])
def create_product():
    """Crea un nuevo producto."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos JSON requeridos"}), 400
    product = crud.create_product(data)
    return jsonify(product), 201


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """Actualiza un producto existente."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos JSON requeridos"}), 400
    result = crud.update_product(product_id, data)
    if result is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify(result)


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """Elimina un producto."""
    result = crud.delete_product(product_id)
    if not result:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify({"message": "Producto eliminado"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
