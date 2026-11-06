from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'mercado_eym_clave_2026'

# Categorías del mercado
categorias = [
    {'id': 'frutas',   'nombre': 'Frutas',            'icono': '🍓', 'descripcion': 'Frutas frescas de temporada'},
    {'id': 'verduras', 'nombre': 'Verduras y Tubérc.', 'icono': '🥦', 'descripcion': 'Del campo directo al mercado'},
    {'id': 'carnes',   'nombre': 'Carnes',             'icono': '🥩', 'descripcion': 'Cortes frescos todos los días'},
    {'id': 'lacteos',  'nombre': 'Lácteos y Huevos',  'icono': '🥛', 'descripcion': 'Producción local y diaria'},
    {'id': 'almacen',  'nombre': 'Almacén',            'icono': '🛒', 'descripcion': 'Secos, conservas y más'},
    {'id': 'varios',   'nombre': 'Varios',             'icono': '📦', 'descripcion': 'Superfoods y productos naturales'},
]

# Productos del mercado (precios en guaraníes paraguayos)
productos = [

    # ── FRUTAS ──────────────────────────────────────────────────────────────
    {
        'id': 1,
        'nombre': 'Mango',
        'descripcion': 'Mango maduro y dulce, cosechado en la zona. Ideal para jugos, postres o comer al natural.',
        'precio': 5000,
        'unidad': 'kg',
        'imagen': 'mango.jpg',
        'categoria': 'frutas',
        'origen': 'Local',
        'destacado': True,
    },
    {
        'id': 2,
        'nombre': 'Fresas',
        'descripcion': 'Fresas frescas de temporada. Perfectas para jugos, mermeladas y postres.',
        'precio': 8000,
        'unidad': 'kg',
        'imagen': 'fresas.jpg',
        'categoria': 'frutas',
        'origen': 'Local',
        'destacado': True,
    },
    {
        'id': 3,
        'nombre': 'Piña',
        'descripcion': 'Piña grande y jugosa de la región. Lista para consumir.',
        'precio': 7000,
        'unidad': 'unidad',
        'imagen': 'pina-grande.jpg',
        'categoria': 'frutas',
        'origen': 'Local',
        'destacado': False,
    },
    {
        'id': 4,
        'nombre': 'Plátano',
        'descripcion': 'Plátanos maduros para comer o cocinar. Disponibles por kilo o racimo.',
        'precio': 3000,
        'unidad': 'kg',
        'imagen': 'platano.jpg',
        'categoria': 'frutas',
        'origen': 'Local',
        'destacado': False,
    },
    {
        'id': 5,
        'nombre': 'Sandía',
        'descripcion': 'Sandía entera, grande y dulce. Ideal para refrescarse en el verano paraguayo.',
        'precio': 15000,
        'unidad': 'unidad',
        'imagen': 'sandia.jpg',
        'categoria': 'frutas',
        'origen': 'Local',
        'destacado': True,
    },
    {
        'id': 6,
        'nombre': 'Papaya',
        'descripcion': 'Papaya madura y rica en vitaminas. Excelente para el desayuno.',
        'precio': 6000,
        'unidad': 'kg',
        'imagen': 'papaya.jpg',
        'categoria': 'frutas',
        'origen': 'Local',
        'destacado': False,
    },
    {
        'id': 7,
        'nombre': 'Kiwi',
        'descripcion': 'Kiwis frescos, excelente fuente de vitamina C y antioxidantes.',
        'precio': 12000,
        'unidad': 'kg',
        'imagen': 'kiwi.jpg',
        'categoria': 'frutas',
        'origen': 'Importado',
        'destacado': False,
    },
    {
        'id': 8,
        'nombre': 'Durazno',
        'descripcion': 'Duraznos frescos y maduros, ideales para mermeladas y postres caseros.',
        'precio': 9000,
        'unidad': 'kg',
        'imagen': 'durazno.jpg',
        'categoria': 'frutas',
        'origen': 'Local',
        'destacado': False,
    },
    {
        'id': 9,
        'nombre': 'Moras',
        'descripcion': 'Moras frescas de temporada. Ricas en antioxidantes y perfectas para jugos.',
        'precio': 10000,
        'unidad': 'kg',
        'imagen': 'moras.jpg',
        'categoria': 'frutas',
        'origen': 'Local',
        'destacado': False,
    },
    {
        'id': 10,
        'nombre': 'Arándanos',
        'descripcion': 'Arándanos frescos, uno de los frutos con más antioxidantes naturales.',
        'precio': 14000,
        'unidad': 'kg',
        'imagen': 'arandanos.jpg',
        'categoria': 'frutas',
        'origen': 'Importado',
        'destacado': False,
    },
    {
        'id': 11,
        'nombre': 'Pitaya',
        'descripcion': 'Fruta del dragón fresca. Exótica, nutritiva y de temporada.',
        'precio': 18000,
        'unidad': 'kg',
        'imagen': 'pitaya.jpg',
        'categoria': 'frutas',
        'origen': 'Local',
        'destacado': False,
    },

    # ── VERDURAS ─────────────────────────────────────────────────────────────
    {
        'id': 12,
        'nombre': 'Coco Fresco',
        'descripcion': 'Coco entero con agua y pulpa. Refrescante y nutritivo, traído directo del campo.',
        'precio': 8000,
        'unidad': 'unidad',
        'imagen': 'coco-rallado.jpg',
        'categoria': 'verduras',
        'origen': 'Local',
        'destacado': True,
    },
    {
        'id': 13,
        'nombre': 'Agua de Coco Natural',
        'descripcion': 'Agua de coco fresca, extraída en el momento. Hidratante y natural.',
        'precio': 6000,
        'unidad': 'unidad',
        'imagen': 'agua-coco.jpg',
        'categoria': 'verduras',
        'origen': 'Local',
        'destacado': False,
    },
    {
        'id': 14,
        'nombre': 'Piña Pequeña',
        'descripcion': 'Piñas pequeñas y dulces, frescas de la semana. Precio por unidad.',
        'precio': 4000,
        'unidad': 'unidad',
        'imagen': 'pina.jpg',
        'categoria': 'verduras',
        'origen': 'Local',
        'destacado': False,
    },

    # ── CARNES ───────────────────────────────────────────────────────────────
    {
        'id': 15,
        'nombre': 'Fresa de Temporada (conserva)',
        'descripcion': 'Fresas frescas seleccionadas para conservas artesanales. Precio por bandeja.',
        'precio': 12000,
        'unidad': 'bandeja',
        'imagen': 'fresa.jpg',
        'categoria': 'carnes',
        'origen': 'Local',
        'destacado': False,
    },
    {
        'id': 16,
        'nombre': 'Proteína Natural en Polvo',
        'descripcion': 'Proteína de origen natural, sin colorantes ni sabores artificiales.',
        'precio': 85000,
        'unidad': '500g',
        'imagen': 'proteina.jpg',
        'categoria': 'carnes',
        'origen': 'Nacional',
        'destacado': True,
    },

    # ── LÁCTEOS Y HUEVOS ─────────────────────────────────────────────────────
    {
        'id': 17,
        'nombre': 'Leche Entera Fresca',
        'descripcion': 'Leche entera de producción local, entregada a diario. Sin conservantes.',
        'precio': 5000,
        'unidad': 'litro',
        'imagen': 'leche-entera.jpg',
        'categoria': 'lacteos',
        'origen': 'Local',
        'destacado': True,
    },
    {
        'id': 18,
        'nombre': 'Leche de Almendras',
        'descripcion': 'Leche vegetal de almendras, ideal para intolerantes a la lactosa.',
        'precio': 18000,
        'unidad': 'litro',
        'imagen': 'leche-almendra.jpg',
        'categoria': 'lacteos',
        'origen': 'Nacional',
        'destacado': False,
    },
    {
        'id': 19,
        'nombre': 'Leche de Coco',
        'descripcion': 'Leche de coco cremosa, perfecta para cocinar y preparar postres.',
        'precio': 15000,
        'unidad': '400ml',
        'imagen': 'leche-coco.jpg',
        'categoria': 'lacteos',
        'origen': 'Nacional',
        'destacado': False,
    },
    {
        'id': 20,
        'nombre': 'Yogurt Natural',
        'descripcion': 'Yogurt natural sin azúcar, cremoso y con probióticos. De producción local.',
        'precio': 7000,
        'unidad': '500g',
        'imagen': 'yogurt.jpg',
        'categoria': 'lacteos',
        'origen': 'Local',
        'destacado': False,
    },

    # ── ALMACÉN ──────────────────────────────────────────────────────────────
    {
        'id': 21,
        'nombre': 'Avena en Hojuelas',
        'descripcion': 'Avena tradicional en hojuelas, ideal para el desayuno y recetas saludables.',
        'precio': 6000,
        'unidad': 'kg',
        'imagen': 'avena.jpg',
        'categoria': 'almacen',
        'origen': 'Nacional',
        'destacado': False,
    },
    {
        'id': 22,
        'nombre': 'Miel Pura de Abeja',
        'descripcion': 'Miel artesanal 100% pura, directamente del productor local. Sin aditivos.',
        'precio': 25000,
        'unidad': '500g',
        'imagen': 'miel.jpg',
        'categoria': 'almacen',
        'origen': 'Local',
        'destacado': True,
    },
    {
        'id': 23,
        'nombre': 'Granola Artesanal',
        'descripcion': 'Granola hecha a mano con avena, miel y frutas secas. Sin azúcar refinada.',
        'precio': 15000,
        'unidad': '400g',
        'imagen': 'granola.jpg',
        'categoria': 'almacen',
        'origen': 'Artesanal',
        'destacado': False,
    },
    {
        'id': 24,
        'nombre': 'Cacao en Polvo',
        'descripcion': 'Cacao puro en polvo, sin azúcar. Para bebidas, repostería y recetas saludables.',
        'precio': 12000,
        'unidad': '250g',
        'imagen': 'cacao.jpg',
        'categoria': 'almacen',
        'origen': 'Nacional',
        'destacado': False,
    },
    {
        'id': 25,
        'nombre': 'Agua Mineral',
        'descripcion': 'Agua mineral natural, sin gas. Disponible en varios tamaños.',
        'precio': 3000,
        'unidad': '1.5 litros',
        'imagen': 'agua.jpg',
        'categoria': 'almacen',
        'origen': 'Nacional',
        'destacado': False,
    },

    # ── VARIOS ───────────────────────────────────────────────────────────────
    {
        'id': 26,
        'nombre': 'Semillas de Chía',
        'descripcion': 'Semillas de chía ricas en omega-3, fibra y proteína vegetal.',
        'precio': 10000,
        'unidad': '250g',
        'imagen': 'chia.jpg',
        'categoria': 'varios',
        'origen': 'Importado',
        'destacado': False,
    },
    {
        'id': 27,
        'nombre': 'Mantequilla de Maní',
        'descripcion': 'Mantequilla de maní artesanal, sin conservantes ni azúcar añadida.',
        'precio': 18000,
        'unidad': '350g',
        'imagen': 'mantequilla-mani.jpg',
        'categoria': 'varios',
        'origen': 'Artesanal',
        'destacado': True,
    },
    {
        'id': 28,
        'nombre': 'Producto Natural',
        'descripcion': 'Selección de productos 100% naturales disponibles en el mercado.',
        'precio': 8000,
        'unidad': 'unidad',
        'imagen': 'natural.jpg',
        'categoria': 'varios',
        'origen': 'Local',
        'destacado': False,
    },
    {
        'id': 29,
        'nombre': 'Pack Energizante',
        'descripcion': 'Combinación de productos energizantes naturales: granola, chía y miel.',
        'precio': 35000,
        'unidad': 'pack',
        'imagen': 'energia.jpg',
        'categoria': 'varios',
        'origen': 'Artesanal',
        'destacado': True,
    },
    {
        'id': 30,
        'nombre': 'Pack Nutritivo',
        'descripcion': 'Kit de productos nutritivos seleccionados: avena, cacao y mantequilla de maní.',
        'precio': 40000,
        'unidad': 'pack',
        'imagen': 'nutritivo.jpg',
        'categoria': 'varios',
        'origen': 'Artesanal',
        'destacado': False,
    },
]


@app.route('/')
def index():
    """Página principal"""
    destacados = [p for p in productos if p.get('destacado')]
    return render_template('index.html',
                           productos_destacados=destacados,
                           categorias=categorias)


@app.route('/productos')
def catalogo():
    """Catálogo completo, con filtro opcional por categoría"""
    categoria_sel = request.args.get('categoria', None)
    if categoria_sel:
        lista = [p for p in productos if p['categoria'] == categoria_sel]
        cat_obj = next((c for c in categorias if c['id'] == categoria_sel), None)
    else:
        lista = productos
        cat_obj = None
    return render_template('catalogo.html',
                           productos=lista,
                           categorias=categorias,
                           categoria_sel=categoria_sel,
                           cat_obj=cat_obj)


@app.route('/producto/<int:producto_id>')
def producto_detalle(producto_id):
    """Detalle de un producto"""
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if not producto:
        flash('Producto no encontrado.', 'error')
        return redirect(url_for('catalogo'))
    relacionados = [p for p in productos
                    if p['categoria'] == producto['categoria']
                    and p['id'] != producto_id][:3]
    cat_obj = next((c for c in categorias if c['id'] == producto['categoria']), None)
    return render_template('producto_detalle.html',
                           producto=producto,
                           relacionados=relacionados,
                           cat_obj=cat_obj)


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    """Página de contacto"""
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        email = request.form.get('email', '').strip()
        mensaje = request.form.get('mensaje', '').strip()
        if nombre and email and mensaje:
            flash('¡Gracias por tu mensaje! Te contactaremos pronto.', 'success')
            return redirect(url_for('contacto'))
        else:
            flash('Por favor completá todos los campos.', 'error')
    return render_template('contacto.html')


@app.route('/sobre-nosotros')
def sobre_nosotros():
    """Página sobre nosotros"""
    return render_template('sobre_nosotros.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
