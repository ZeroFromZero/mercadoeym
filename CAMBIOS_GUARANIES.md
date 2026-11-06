# 💰 Cambios a Moneda Guaraníes

## Resumen de Cambios

Se actualizó toda la aplicación para usar **Guaraníes Paraguayos (₲)** en lugar de dólares.

---

## 💵 Conversión de Precios

**Tasa de conversión utilizada:** 1 USD ≈ 7,500 Guaraníes

### Smoothies del Menú

| Smoothie | Precio Anterior (USD) | Precio Nuevo (₲) |
|----------|----------------------|------------------|
| Paraíso Tropical | $5.99 | ₲45,000 |
| Explosión de Berries | $5.49 | ₲40,000 |
| Poder Verde Detox | $6.49 | ₲48,000 |
| Energía de Cacao | $5.99 | ₲45,000 |
| Amanecer Dorado | $5.79 | ₲42,000 |
| Dragón Rosa | $6.99 | ₲52,000 |
| Mango Tropical | $5.49 | ₲40,000 |
| Acai Bowl Smoothie | $7.49 | ₲55,000 |

### Ingredientes para Smoothies Personalizados

#### 🍓 Frutas
- Fresas: ₲3,500
- Plátano: ₲2,000
- Mango: ₲5,000
- Arándanos: ₲6,000
- Piña: ₲4,500
- Moras: ₲5,000
- Pitaya: ₲9,000
- Kiwi: ₲4,500
- Papaya: ₲3,500
- Durazno: ₲4,000 (NUEVO)
- Sandía: ₲3,000 (NUEVO)

#### 🥛 Bases Líquidas
- Leche de Almendras: ₲4,500
- Leche de Coco: ₲5,000
- Yogurt Natural: ₲3,500
- Agua de Coco: ₲6,000
- Leche Entera: ₲3,000 (NUEVO)
- Agua: ₲0 (Gratis)

#### ✨ Extras
- Proteína en Polvo: ₲11,000
- Semillas de Chía: ₲4,500
- Granola: ₲5,000
- Miel Orgánica: ₲3,000
- Mantequilla de Maní: ₲6,000
- Cacao Orgánico: ₲5,000
- Avena: ₲2,500 (NUEVO)
- Coco Rallado: ₲3,000 (NUEVO)

**Precio Base del Smoothie Personalizado:** ₲25,000

---

## ❌ Eliminación de Verduras

Se eliminó completamente la sección de verduras del creador de smoothies para enfocarse en smoothies de frutas dulces y deliciosos.

### Verduras Eliminadas:
- ~~Espinaca~~
- ~~Kale~~
- ~~Apio~~
- ~~Pepino~~
- ~~Zanahoria~~

### Razón:
Enfoque en smoothies de frutas tradicionales, más apetecibles para el público general.

---

## 🆕 Nuevos Ingredientes Agregados

### Frutas:
- 🍑 **Durazno** - ₲4,000 (30 kcal)
- 🍉 **Sandía** - ₲3,000 (20 kcal)

### Bases:
- 🥛 **Leche Entera** - ₲3,000 (40 kcal)

### Extras:
- 🌾 **Avena** - ₲2,500 (40 kcal)
- 🥥 **Coco Rallado** - ₲3,000 (35 kcal)

---

## 📝 Archivos Modificados

### Backend (Python)
- ✅ `app.py`
  - Precios de smoothies convertidos a guaraníes
  - Precios de ingredientes convertidos a guaraníes
  - Precio base actualizado: ₲25,000
  - Eliminada lógica de verduras
  - Formato de precio actualizado en flash messages

### Frontend (Templates)
- ✅ `templates/index.html` - Formato de precios: ₲{:,}
- ✅ `templates/menu.html` - Formato de precios: ₲{:,}
- ✅ `templates/smoothie_detalle.html` - Formato de precios: ₲{:,}
- ✅ `templates/crear_smoothie.html`
  - Eliminada sección de verduras (Paso 2)
  - Renumerados los pasos (ahora son 4 en lugar de 5)
  - Agregados emojis para nuevos ingredientes
  - Actualizado formato de precios: ₲{:,}
  - Tips actualizados sin mención de verduras
- ✅ `templates/resumen_smoothie.html`
  - Eliminada sección de verduras
  - Actualizado formato de precios: ₲{:,}
  - Contador de ingredientes actualizado

---

## 🎨 Formato de Visualización

### Antes:
```
$5.99
$45.00
$0.50
```

### Ahora:
```
₲45,000
₲340,500
₲3,500
```

**Características:**
- Símbolo de guaraní: ₲
- Separador de miles con comas
- Sin decimales (guaraníes son enteros)

---

## 🔄 Estructura del Creador de Smoothies

### Antes (5 pasos):
1. Frutas
2. Verduras
3. Base Líquida
4. Extras
5. Tamaño

### Ahora (4 pasos):
1. 🍓 Frutas (11 opciones)
2. 🥛 Base Líquida (6 opciones)
3. ✨ Extras (8 opciones)
4. 📏 Tamaño (3 opciones)

---

## 💡 Total de Ingredientes Disponibles

- **Frutas:** 11 opciones (agregadas 2 nuevas)
- **Verduras:** 0 opciones (eliminadas 5)
- **Bases:** 6 opciones (agregada 1 nueva)
- **Extras:** 8 opciones (agregados 2 nuevos, eliminados 2)

**Total:** 25 ingredientes únicos

---

## ✅ Verificación de Cambios

### Cambios Completados:
- [x] Precios de smoothies convertidos a guaraníes
- [x] Precios de ingredientes convertidos a guaraníes
- [x] Precio base actualizado
- [x] Formato de visualización (₲ con separador de miles)
- [x] Eliminación de verduras del código
- [x] Eliminación de verduras de templates
- [x] Nuevos ingredientes agregados
- [x] Renumeración de pasos en creador
- [x] Tips actualizados
- [x] Contador de ingredientes corregido

### Funcionalidad Verificada:
- [x] Menú muestra precios en guaraníes
- [x] Detalle de smoothies muestra precios en guaraníes
- [x] Creador de smoothies calcula en guaraníes
- [x] Resumen muestra precio total en guaraníes
- [x] No hay referencias a verduras en la UI
- [x] Flash messages muestran precios en guaraníes

---

## 🚀 Cómo Probar los Cambios

1. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

2. Verifica los precios en:
   - Página principal (smoothies destacados)
   - Menú completo
   - Detalle de cada smoothie
   - Creador de smoothies
   - Resumen del smoothie personalizado

3. Crea un smoothie personalizado:
   - Selecciona frutas
   - Elige base líquida
   - Agrega extras
   - Selecciona tamaño
   - Verifica que el precio se muestre en guaraníes con formato correcto

---

## 📊 Ejemplo de Cálculo

**Smoothie Personalizado:**
- Base: ₲25,000
- Fresa: +₲3,500
- Plátano: +₲2,000
- Mango: +₲5,000
- Yogurt Natural: +₲3,500
- Proteína: +₲11,000
- Tamaño Grande (+30%): ×1.3

**Total:** (25,000 + 3,500 + 2,000 + 5,000 + 3,500 + 11,000) × 1.3 = **₲65,000**

---

## 📝 Notas Importantes

1. **No hay decimales** en guaraníes (es moneda entera)
2. **Separador de miles** con comas para mejor legibilidad
3. **Símbolo ₲** siempre va antes del número
4. Los cálculos internos se hacen en enteros
5. La aplicación está completamente funcional con guaraníes

---

¡Cambios completados exitosamente! 🎉🇵🇾
