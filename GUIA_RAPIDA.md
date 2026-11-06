# 🍹 Guía Rápida - Smoothie Paradise

## 🚀 Inicio Rápido

### Opción 1: Usar el script automático (Windows)
Simplemente haz doble clic en `run.bat` y la aplicación se iniciará automáticamente.

### Opción 2: Inicio manual

```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual
venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Iniciar la aplicación
python app.py
```

Luego abre tu navegador en: **http://localhost:5000**

## 📱 Navegación de la App

### Página Principal (/)
- Hero section con llamadas a la acción
- Smoothies destacados con fotos reales
- Características del negocio
- Acceso rápido al menú y creador de smoothies

### Menú (/menu)
- Catálogo completo de 8 smoothies
- Fotos reales de cada smoothie
- Información de calorías y categoría
- Ingredientes y beneficios
- Botón para crear smoothie personalizado

### Crear Tu Smoothie (/crear-smoothie)
**¡La característica estrella!**

1. **Paso 1:** Elige tus frutas (mínimo 1 requerido)
2. **Paso 2:** Agrega verduras (opcional)
3. **Paso 3:** Selecciona tu base líquida (obligatorio)
4. **Paso 4:** Agrega extras y superfoods (opcional)
5. **Paso 5:** Elige el tamaño (Regular, Grande, Extra Grande)

El sistema calcula automáticamente:
- Precio total basado en ingredientes y tamaño
- Calorías aproximadas
- Lista completa de ingredientes

### Resumen del Smoothie (/resumen-smoothie)
- Visualización del smoothie personalizado
- Precio y calorías totales
- Desglose de ingredientes por categoría
- Información nutricional
- Opciones para ordenar o crear otro

### Detalle de Smoothie (/smoothie/<id>)
- Foto real del smoothie
- Información nutricional detallada
- Lista completa de ingredientes
- Beneficios para la salud
- Botón para ordenar

### Contacto (/contacto)
- Formulario de contacto funcional
- Información de la tienda
- Horarios de atención
- Redes sociales

### Sobre Nosotros (/sobre-nosotros)
- Historia del negocio
- Valores y misión
- Por qué elegirnos
- Compromiso con la calidad

## 🎨 Características Principales

### ✅ Diseño Responsive
- Adaptado para móviles, tablets y escritorio
- Menú hamburguesa en dispositivos móviles
- Imágenes optimizadas

### ✅ Fotos Reales
- Imágenes de alta calidad de Unsplash
- Visualización atractiva de smoothies
- Badges de calorías y categorías

### ✅ Creador de Smoothies
- Más de 25 ingredientes disponibles
- Cálculo dinámico de precio
- Cálculo de calorías
- 3 tamaños disponibles
- Validación de formulario

### ✅ Información Nutricional
- Calorías por smoothie
- Beneficios para la salud
- Ingredientes orgánicos
- Categorías (tropical, detox, proteína, etc.)

## 💡 Tips de Uso

### Para Desarrolladores

**Agregar un nuevo smoothie:**
```python
# En app.py, agrega a la lista smoothies:
{
    'id': 9,
    'nombre': 'Tu Smoothie',
    'descripcion': 'Descripción atractiva',
    'precio': 6.99,
    'imagen': 'https://images.unsplash.com/photo-xxxxx',
    'ingredientes': ['Ingrediente 1', 'Ingrediente 2'],
    'calorias': 200,
    'categoria': 'tu-categoria',
    'beneficios': ['Beneficio 1', 'Beneficio 2']
}
```

**Agregar un ingrediente al creador:**
```python
# En app.py, en ingredientes_disponibles:
'frutas': [
    {'id': 'tu-fruta', 'nombre': 'Tu Fruta', 'precio': 0.50, 'calorias': 20}
]
```

**Cambiar colores del tema:**
```css
/* En static/css/style.css */
:root {
    --primary-color: #tu-color;
    --secondary-color: #tu-color;
}
```

### Para Usuarios del Negocio

**Actualizar precios:**
- Edita los precios en `app.py` en la lista de smoothies
- Edita los precios de ingredientes en `ingredientes_disponibles`

**Actualizar información de contacto:**
- Edita `templates/base.html` (footer)
- Edita `templates/contacto.html`

**Cambiar horarios:**
- Edita `templates/base.html` (footer)
- Edita `templates/contacto.html`

## 🔧 Solución de Problemas

### La aplicación no inicia
```bash
# Verifica la versión de Python (debe ser 3.7+)
python --version

# Reinstala las dependencias
pip install --force-reinstall -r requirements.txt
```

### Las imágenes no cargan
- Verifica tu conexión a internet (las imágenes son de Unsplash)
- Para producción, descarga las imágenes y guárdalas en `static/images/`

### Error al crear smoothie
- Asegúrate de seleccionar al menos una fruta
- Asegúrate de seleccionar una base líquida
- Verifica que tu navegador tenga cookies habilitadas (usa sesiones)

### Los estilos no se aplican
```bash
# Limpia el caché del navegador:
# Chrome/Edge: Ctrl + Shift + Delete
# Firefox: Ctrl + Shift + Delete
# O presiona Ctrl + F5 para recargar sin caché
```

## 📊 Estructura de Datos

### Smoothie Object
```python
{
    'id': int,              # ID único
    'nombre': str,          # Nombre del smoothie
    'descripcion': str,     # Descripción atractiva
    'precio': float,        # Precio en USD
    'imagen': str,          # URL de la imagen
    'ingredientes': list,   # Lista de ingredientes
    'calorias': int,        # Calorías totales
    'categoria': str,       # Categoría del smoothie
    'beneficios': list      # Beneficios para la salud
}
```

### Ingrediente Object
```python
{
    'id': str,      # ID único (slug)
    'nombre': str,  # Nombre para mostrar
    'precio': float,# Costo adicional
    'calorias': int # Calorías que aporta
}
```

## 🎯 Próximas Mejoras Sugeridas

- [ ] Sistema de pedidos online con carrito
- [ ] Integración con pasarelas de pago
- [ ] Base de datos para guardar pedidos
- [ ] Panel de administración
- [ ] Sistema de usuarios y login
- [ ] Programa de lealtad automatizado
- [ ] Integración con delivery (Uber Eats, etc.)
- [ ] Notificaciones por email
- [ ] Sistema de reseñas y calificaciones
- [ ] Blog de recetas y nutrición
- [ ] API REST para apps móviles

## 📞 Soporte

Para preguntas o problemas:
- Revisa esta guía primero
- Consulta el README.md para información técnica
- Revisa la sección de solución de problemas

## 📄 Licencia

Este proyecto está disponible para uso personal y comercial.

---

¡Disfruta creando smoothies deliciosos! 🍹✨
