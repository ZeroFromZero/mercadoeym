# 🍹 Smoothie Paradise - Sitio Web Flask

Una aplicación web moderna y atractiva para un negocio de smoothies, construida con Flask, diseño responsive y fotos reales de smoothies.

## 📋 Características

- **Página Principal**: Hero section atractivo con smoothies destacados y fotos reales
- **Menú Completo**: Catálogo de 8 smoothies únicos con imágenes reales de Unsplash
- **Creador de Smoothies**: ¡NUEVO! Crea tu propio smoothie personalizado eligiendo ingredientes
- **Página de Detalle**: Información completa de cada smoothie con ingredientes, beneficios y calorías
- **Formulario de Contacto**: Sistema de mensajes con validación
- **Sobre Nosotros**: Historia y valores del negocio
- **Diseño Responsive**: Funciona perfectamente en móviles, tablets y escritorio
- **Animaciones Modernas**: Efectos visuales suaves y atractivos
- **Información Nutricional**: Calorías y beneficios para cada smoothie

## 🚀 Instalación

### Prerrequisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd smoothie-paradise
   ```

2. **Crear un entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual**
   
   En Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   En macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Uso

### Iniciar la aplicación

```bash
python app.py
```

La aplicación estará disponible en: `http://localhost:5000`

### Rutas disponibles

- `/` - Página principal
- `/menu` - Menú completo de smoothies
- `/smoothie/<id>` - Detalle de un smoothie específico
- `/crear-smoothie` - **¡NUEVO!** Creador de smoothies personalizados
- `/resumen-smoothie` - Resumen del smoothie personalizado creado
- `/contacto` - Formulario de contacto
- `/sobre-nosotros` - Información sobre el negocio

## 📁 Estructura del Proyecto

```
smoothie-paradise/
│
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
│
├── static/               # Archivos estáticos
│   └── css/
│       └── style.css     # Estilos CSS
│
└── templates/            # Plantillas HTML
    ├── base.html         # Template base
    ├── index.html        # Página principal
    ├── menu.html         # Menú completo
    ├── smoothie_detalle.html  # Detalle de smoothie
    ├── contacto.html     # Página de contacto
    └── sobre_nosotros.html    # Sobre nosotros
```

## 🍹 Smoothies Disponibles

1. **Paraíso Tropical** - Mango, piña, plátano y leche de coco ($5.99) - 220 kcal
2. **Explosión de Berries** - Fresas, arándanos, moras y yogurt ($5.49) - 180 kcal
3. **Poder Verde Detox** - Espinaca, kale, manzana verde y jengibre ($6.49) - 150 kcal
4. **Energía de Cacao** - Plátano, cacao, mantequilla de maní y leche de almendras ($5.99) - 280 kcal
5. **Amanecer Dorado** - Naranja, zanahoria, mango y cúrcuma ($5.79) - 160 kcal
6. **Dragón Rosa** - Pitaya, fresas, plátano y leche de coco ($6.99) - 200 kcal
7. **Mango Tropical** - Mango maduro, maracuyá y yogurt griego ($5.49) - 190 kcal
8. **Acai Bowl Smoothie** - Açaí, plátano, fresas y granola ($7.49) - 240 kcal

## 🎨 Creador de Smoothies Personalizado

### Ingredientes Disponibles:

**Frutas:** Fresas, Plátano, Mango, Arándanos, Piña, Moras, Pitaya, Kiwi, Papaya

**Verduras:** Espinaca, Kale, Apio, Pepino, Zanahoria

**Bases Líquidas:** Leche de Almendras, Leche de Coco, Yogurt Natural, Agua de Coco, Agua

**Extras:** Proteína en Polvo, Semillas de Chía, Granola, Miel Orgánica, Mantequilla de Maní, Cacao Orgánico, Jengibre Fresco, Cúrcuma

### Tamaños:
- Regular (12oz / 350ml) - Precio base
- Grande (16oz / 470ml) - +30%
- Extra Grande (20oz / 590ml) - +60%

## 🎨 Personalización

### Cambiar colores

Edita las variables CSS en `static/css/style.css`:

```css
:root {
    --primary-color: #ff6b6b;
    --secondary-color: #4ecdc4;
    --accent-color: #ffe66d;
    /* ... más colores */
}
```

### Agregar más smoothies

Edita la lista `smoothies` en `app.py`:

```python
smoothies = [
    {
        'id': 9,
        'nombre': 'Nuevo Smoothie',
        'descripcion': 'Descripción deliciosa del smoothie',
        'precio': 5.99,
        'imagen': 'https://images.unsplash.com/photo-url',  # URL de Unsplash
        'ingredientes': ['Ingrediente 1', 'Ingrediente 2'],
        'calorias': 200,
        'categoria': 'tropical',
        'beneficios': ['Beneficio 1', 'Beneficio 2']
    }
]
```

### Agregar ingredientes al creador de smoothies

Edita el diccionario `ingredientes_disponibles` en `app.py`:

```python
ingredientes_disponibles = {
    'frutas': [
        {'id': 'nueva-fruta', 'nombre': 'Nueva Fruta', 'precio': 0.50, 'calorias': 20}
    ],
    # ... más categorías
}
```

### Cambiar información de contacto

Edita el footer en `templates/base.html` y la página de contacto en `templates/contacto.html`.

## 🔧 Configuración de Producción

Para usar en producción, **recuerda cambiar**:

1. **Secret Key** en `app.py`:
   ```python
   app.secret_key = 'tu_clave_secreta_segura_aqui'
   ```

2. **Debug Mode** en `app.py`:
   ```python
   app.run(debug=False)
   ```

3. Usa un servidor WSGI como **Gunicorn**:
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```

## 🌐 Despliegue

### Opciones de hosting recomendadas:

- **Heroku**: Ideal para principiantes
- **PythonAnywhere**: Gratuito para proyectos pequeños
- **DigitalOcean**: Para más control
- **AWS/Google Cloud**: Para proyectos empresariales

## 📱 Responsive Design

La aplicación está completamente optimizada para:
- 📱 Dispositivos móviles (< 480px)
- 📱 Tablets (480px - 768px)
- 💻 Escritorio (> 768px)

## 🤝 Contribuciones

Las mejoras son bienvenidas. Para contribuir:

1. Haz un fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 📝 Notas Importantes

- Este proyecto usa Flask en modo desarrollo. Para producción, configura un servidor WSGI apropiado.
- Las imágenes de smoothies son de Unsplash y se cargan desde URLs externas. Para producción, considera descargarlas y servirlas localmente.
- El formulario de contacto actualmente solo muestra un mensaje de confirmación. Para producción, deberías implementar envío de emails o guardar en base de datos.
- El creador de smoothies guarda los datos en sesión (session). Para un sistema de pedidos real, considera usar una base de datos.
- Los precios y calorías en el creador de smoothies son aproximados y se calculan dinámicamente.

## 🐛 Solución de Problemas

### La aplicación no inicia

- Verifica que el entorno virtual esté activado
- Asegúrate de que todas las dependencias estén instaladas
- Revisa que el puerto 5000 no esté en uso

### Los estilos no se aplican

- Verifica que la carpeta `static/css/` exista
- Limpia el caché del navegador (Ctrl + F5)
- Revisa la consola del navegador por errores

### Error "Template not found"

- Asegúrate de que la carpeta `templates/` exista
- Verifica que todos los archivos HTML estén en su lugar

## 📄 Licencia

Este proyecto está disponible para uso personal y comercial.

## 👨‍💻 Autor

Creado con ❤️ para Smoothie Paradise

---

¡Disfruta tu aplicación de smoothies! 🍹✨
