# Pre-Entrega QA Automation - SauceDemo

## Descripción

Este proyecto corresponde a la pre-entrega del curso de Automatización QA.

Se desarrolló una suite de pruebas automatizadas utilizando Python, Selenium WebDriver y Pytest sobre el sitio de práctica SauceDemo.

El objetivo es validar funcionalidades esenciales de la aplicación, incluyendo autenticación, navegación por catálogo de productos e interacción con el carrito de compras.

## Tecnologías utilizadas

- Python 3.13
- Selenium WebDriver
- Pytest
- WebDriver Manager
- Pytest HTML
- Git
- GitHub

## Sitio bajo prueba

https://www.saucedemo.com/

## Casos automatizados

### Login

- Login exitoso con credenciales válidas.
- Login con usuario inválido.
- Login con contraseña inválida.
- Login con campos vacíos.

### Navegación y catálogo

- Verificación de redirección a inventario.
- Validación del título de la página.
- Validación de la sección "Products".
- Verificación de productos visibles.
- Validación de cantidad de productos.
- Verificación de elementos principales de la interfaz.

### Carrito de compras

- Agregado de producto al carrito.
- Validación del badge del carrito.
- Navegación al carrito.
- Verificación de nombre y precio del producto.

## Estructura del proyecto

```text
AutomationQA
│
├── assets/
│
├── preLabQA/
│   └── tests/
│       └── test_saucedemo.py
│
├── reporte.html
├── requirements.txt
└── README.md
```

## Instalación

Instalar las dependencias necesarias:

```bash
pip install selenium
pip install pytest
pip install webdriver-manager
pip install pytest-html
```

O utilizar:

```bash
pip install -r requirements.txt
```

## Ejecución de pruebas

Ejecutar todos los casos de prueba:

```bash
pytest -v
```

## Generación de reporte HTML

Generar reporte de ejecución:

```bash
pytest -v --html=reporte.html
```

El archivo `reporte.html` contendrá el detalle de los resultados obtenidos durante la ejecución de la suite de pruebas.

## Autor

Ma. Florencia Rodríguez Varangot

Talento Tech - Automatización QA
