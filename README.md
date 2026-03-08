# CRUD de Productos - Proyecto con Pipeline CI/CD

Proyecto Python que implementa un CRUD (Crear, Leer, Actualizar, Eliminar) de productos con persistencia en archivos JSON, integrado con un pipeline CI/CD completo usando GitHub Actions.

## Estructura del Proyecto

```
crud-products/
├── crud.py              # Módulo principal con operaciones CRUD
├── app.py               # API REST con Flask
├── products.json        # Archivo de persistencia
├── tests/
│   ├── conftest.py      # Fixtures de pytest
│   └── test_crud.py     # Pruebas unitarias
├── requirements.txt
├── Dockerfile
├── .flake8              # Configuración de linting
├── .github/workflows/
│   └── ci.yml           # Pipeline CI/CD
└── README.md
```

## Cómo funciona el CRUD

El módulo `crud.py` proporciona las siguientes funciones:

| Función | Descripción |
|---------|-------------|
| `create_product(product)` | Agrega un nuevo producto al archivo JSON |
| `read_products()` | Devuelve la lista completa de productos |
| `update_product(product_id, new_data)` | Actualiza un producto por su ID |
| `delete_product(product_id)` | Elimina un producto por su ID |

### Ejemplo de uso

```python
import crud

# Crear producto
producto = {"id": 1, "name": "Laptop", "price": 1200}
crud.create_product(producto)

# Leer productos
productos = crud.read_products()

# Actualizar producto
crud.update_product(1, {"price": 1000})

# Eliminar producto
crud.delete_product(1)
```

### API REST

La aplicación expone una API REST en el puerto 8000:

- `GET /products` - Listar todos los productos
- `POST /products` - Crear producto (body JSON)
- `PUT /products/<id>` - Actualizar producto
- `DELETE /products/<id>` - Eliminar producto

## Cómo ejecutar localmente

### Requisitos previos

- Python 3.10 o superior
- pip

### Instalación

```bash
pip install -r requirements.txt
```

### Ejecutar pruebas

```bash
pytest --maxfail=1 --disable-warnings -q
```

### Ejecutar linting

```bash
flake8 .
```

### Ejecutar la API

```bash
python app.py
```

La API estará disponible en `http://localhost:8000`

### Ejecutar con Docker

```bash
docker build -t crud-products .
docker run -p 8000:8000 crud-products
```

## Cómo funciona el Pipeline CI/CD

El pipeline se ejecuta automáticamente en cada **push** o **pull request** a las ramas `main` o `master`.

### Jobs del pipeline

1. **build-test** (primer job):
   - Checkout del repositorio
   - Instalación de Python 3.10
   - Instalación de dependencias (`pip install -r requirements.txt`)
   - Verificación de estilo con **flake8**
   - Ejecución de pruebas con **pytest**

2. **docker-deploy** (depende de build-test):
   - Construcción de la imagen Docker
   - Ejecución del contenedor en el puerto 8000
   - Verificación de que la API responde correctamente
   - Detención del contenedor

### Evidencia de ejecución exitosa

Para obtener evidencia del pipeline:

1. Sube el repositorio a GitHub
2. Realiza un push a la rama `main`
3. Ve a la pestaña **Actions** de tu repositorio
4. Haz clic en el workflow ejecutado
5. Toma capturas de pantalla de:
   - El job `build-test` en verde (✓)
   - El job `docker-deploy` en verde (✓)
   - Los logs de cada paso

### Ejemplo de logs exitosos

```
✓ Checkout repo
✓ Set up Python
✓ Install dependencies
✓ Lint with flake8
✓ Run tests
✓ Build Docker image
✓ Run container
✓ Verify API is running
```

## Rúbrica de evaluación

| Criterio | Puntos |
|----------|--------|
| Implementación correcta del CRUD en Python | 20 |
| Pruebas unitarias funcionales y completas | 20 |
| Configuración del pipeline CI/CD (lint + tests) | 25 |
| Construcción y despliegue automático (Docker) | 20 |
| Documentación clara en README.md | 15 |
| **Total** | **100** |

## Licencia

Proyecto educativo - Práctica S08 sobre Pipelines CI/CD
