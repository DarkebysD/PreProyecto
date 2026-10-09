# Proyecto de Automatización con Pytest y Selenium

Este proyecto automatiza pruebas funcionales del sitio **SauceDemo** usando **Python**, **pytest** y **Selenium WebDriver**.

## 🚀 Tecnologías utilizadas
- Python 3.11+
- pytest
- Selenium
- pytest-html

## ⚙️ Instalación
1. Clonar el repositorio o abrir la carpeta del proyecto.
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt

## 📂 Estructura del proyecto   

PreProyecto/
│── tests/
│   ├── test_carrito.py
│   ├── test_credenciales.py
│   ├── test_filtroProducto.py
│   ├── test_ingreso.py
│   ├── test_menu.py
│   ├── test_Principal.py
│   └── test_titulo.py
│── requirements.txt
│── report.html
└── README.md

## 🧪 Ejecución de pruebas

pytest --html=report.html --self-contained-html

## 📑 Casos de Prueba Automatizados

El proyecto incluye un total de **19 pruebas automatizadas** ejecutadas con **pytest** y **Selenium WebDriver**. Todas pasaron exitosamente según el último reporte (`report.html`).

### test_Principal.py
- `test_ingreso_credenciales`: Verifica el login con credenciales válidas.
- `test_validar_url`: Comprueba que la URL sea la esperada tras el ingreso.
- `test_validar_titulo`: Valida el título de la página principal.
- `test_validar_menu`: Confirma que el menú de navegación esté disponible.
- `test_validar_carrito`: Verifica que el carrito esté accesible.
- `test_agregar_producto_al_carrito`: Añade un producto al carrito.
- `test_validar_carrito_con_producto`: Comprueba que el carrito contenga el producto agregado.
- `test_validar_filtros`: Valida los filtros de productos.
- `test_validar_productos`: Confirma que los productos se muestran correctamente.

### test_carrito.py
- `test_ingreso_credenciales`: Login antes de interactuar con el carrito.
- `test_agregar_producto_al_carrito`: Añade un producto al carrito.
- `test_validar_carrito_con_producto`: Verifica que el carrito contenga el producto.

### test_credenciales.py
- `test_ingreso_credenciales`: Valida el ingreso con credenciales correctas.

### test_filtroProducto.py
- `test_ingreso_credenciales`: Login previo a la validación de filtros.
- `test_validar_productos`: Comprueba que los productos se muestran según los filtros.

### test_ingreso.py
- `test_ingreso_credenciales`: Verifica el login.
- `test_validar_url`: Comprueba la URL tras el ingreso.

### test_menu.py
- `test_ingreso_credenciales`: Login previo a la validación del menú.

### test_titulo.py
- `test_ingreso_credenciales`: Login previo a la validación del título.

## 📝 NOTAS

Este Proyecto fue desarrollado como pre-entrega para el curso de Automatizacion de testing. todas las pruebas estan diseñadas para funcionar con el sitio web SauceDemo en su version actual.

## 👤 Autor

**Nombre:** Darkebys Diaz 
**Rol:** Estudiante de Desarrollo de pruebas automatizadas con Python, Pytest y Selenium  
**Ubicación:** Buenos Aires, Argentina  
**Fecha del proyecto:** Octubre 2026  

### 📫 Contacto
- GitHub: [github.com/darkebys](https://github.com/darkebys)
- Email: darkebys@gmail.com
