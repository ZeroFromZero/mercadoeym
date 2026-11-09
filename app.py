import os
import sqlite3
from functools import wraps
from flask import (Flask, render_template, request, flash,
                   redirect, url_for, session, g, jsonify)
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge

app = Flask(__name__)
app.secret_key = 'mercado_eym_clave_2026'

# ── Configuración ────────────────────────────────────────────────────────────
DATABASE   = os.path.join(app.root_path, 'mercado.db')
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'productos')
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp', 'gif'}

ADMIN_USER     = 'admin'
ADMIN_PASSWORD = 'mercado2026'   # cambialo después de la primera entrada

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ── Categorías ────────────────────────────────────────────────────────────────
CATEGORIAS = [
    {'id': 'frutas',   'nombre': 'Frutas',             'icono': '🍓', 'descripcion': 'Frutas frescas de temporada'},
    {'id': 'verduras', 'nombre': 'Verduras y Tubérc.',  'icono': '🥦', 'descripcion': 'Del campo directo al mercado'},
    {'id': 'carnes',   'nombre': 'Carnes',              'icono': '🥩', 'descripcion': 'Cortes frescos todos los días'},
    {'id': 'lacteos',  'nombre': 'Lácteos y Huevos',   'icono': '🥛', 'descripcion': 'Producción local y diaria'},
    {'id': 'almacen',  'nombre': 'Almacén',             'icono': '🛒', 'descripcion': 'Secos, conservas y más'},
    {'id': 'varios',   'nombre': 'Varios',              'icono': '📦', 'descripcion': 'Superfoods y productos naturales'},
]

# ── Base de datos ─────────────────────────────────────────────────────────────
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """Crea la tabla y migra los productos hardcodeados si la BD está vacía."""
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre      TEXT    NOT NULL,
            descripcion TEXT    NOT NULL,
            precio      REAL    NOT NULL,
            unidad      TEXT    NOT NULL,
            imagen      TEXT    NOT NULL DEFAULT 'img1.jpg',
            categoria   TEXT    NOT NULL,
            origen      TEXT    NOT NULL DEFAULT 'Local',
            destacado   INTEGER NOT NULL DEFAULT 0
        )
    ''')
    db.commit()

    # Migrar datos iniciales sólo si la tabla está vacía
    if db.execute('SELECT COUNT(*) FROM productos').fetchone()[0] == 0:
        seed = [
            ('Mango','Mango maduro y dulce, cosechado en la zona.',5000,'kg','mango.jpg','frutas','Local',1),
            ('Fresas','Fresas frescas de temporada.',8000,'kg','fresas.jpg','frutas','Local',1),
            ('Piña','Piña grande y jugosa de la región.',7000,'unidad','pina-grande.jpg','frutas','Local',0),
            ('Plátano','Plátanos maduros para comer o cocinar.',3000,'kg','platano.jpg','frutas','Local',0),
            ('Sandía','Sandía entera, grande y dulce.',15000,'unidad','sandia.jpg','frutas','Local',1),
            ('Papaya','Papaya madura y rica en vitaminas.',6000,'kg','papaya.jpg','frutas','Local',0),
            ('Kiwi','Kiwis frescos, excelente fuente de vitamina C.',12000,'kg','kiwi.jpg','frutas','Importado',0),
            ('Durazno','Duraznos frescos y maduros.',9000,'kg','durazno.jpg','frutas','Local',0),
            ('Moras','Moras frescas de temporada.',10000,'kg','moras.jpg','frutas','Local',0),
            ('Arándanos','Arándanos frescos, ricos en antioxidantes.',14000,'kg','arandanos.jpg','frutas','Importado',0),
            ('Pitaya','Fruta del dragón fresca y de temporada.',18000,'kg','pitaya.jpg','frutas','Local',0),
            ('Coco Fresco','Coco entero con agua y pulpa.',8000,'unidad','coco-rallado.jpg','verduras','Local',1),
            ('Agua de Coco Natural','Agua de coco fresca, extraída en el momento.',6000,'unidad','agua-coco.jpg','verduras','Local',0),
            ('Piña Pequeña','Piñas pequeñas y dulces, frescas de la semana.',4000,'unidad','pina.jpg','verduras','Local',0),
            ('Proteína Natural en Polvo','Proteína de origen natural, sin colorantes.',85000,'500g','proteina.jpg','carnes','Nacional',1),
            ('Leche Entera Fresca','Leche entera de producción local, sin conservantes.',5000,'litro','leche-entera.jpg','lacteos','Local',1),
            ('Leche de Almendras','Leche vegetal, ideal para intolerantes a la lactosa.',18000,'litro','leche-almendra.jpg','lacteos','Nacional',0),
            ('Leche de Coco','Leche de coco cremosa, perfecta para cocinar.',15000,'400ml','leche-coco.jpg','lacteos','Nacional',0),
            ('Yogurt Natural','Yogurt natural sin azúcar, con probióticos.',7000,'500g','yogurt.jpg','lacteos','Local',0),
            ('Avena en Hojuelas','Avena tradicional, ideal para el desayuno.',6000,'kg','avena.jpg','almacen','Nacional',0),
            ('Miel Pura de Abeja','Miel artesanal 100% pura, sin aditivos.',25000,'500g','miel.jpg','almacen','Local',1),
            ('Granola Artesanal','Granola hecha a mano, sin azúcar refinada.',15000,'400g','granola.jpg','almacen','Artesanal',0),
            ('Cacao en Polvo','Cacao puro en polvo, sin azúcar.',12000,'250g','cacao.jpg','almacen','Nacional',0),
            ('Agua Mineral','Agua mineral natural, sin gas.',3000,'1.5 litros','agua.jpg','almacen','Nacional',0),
            ('Semillas de Chía','Semillas de chía ricas en omega-3 y fibra.',10000,'250g','chia.jpg','varios','Importado',0),
            ('Mantequilla de Maní','Mantequilla artesanal, sin conservantes.',18000,'350g','mantequilla-mani.jpg','varios','Artesanal',1),
            ('Pack Energizante','Granola, chía y miel combinados en un pack.',35000,'pack','energia.jpg','varios','Artesanal',1),
            ('Pack Nutritivo','Avena, cacao y mantequilla de maní.',40000,'pack','nutritivo.jpg','varios','Artesanal',0),
        ]
        db.executemany('''
            INSERT INTO productos
                (nombre, descripcion, precio, unidad, imagen, categoria, origen, destacado)
            VALUES (?,?,?,?,?,?,?,?)
        ''', seed)
        db.commit()

# ── Helpers ───────────────────────────────────────────────────────────────────
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.errorhandler(RequestEntityTooLarge)
def handle_large_file(e):
    flash('El archivo es demasiado grande. Máximo permitido: 50 MB.', 'error')
    return redirect(request.referrer or url_for('admin_productos'))

def get_cat(cat_id):
    return next((c for c in CATEGORIAS if c['id'] == cat_id), None)

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin_logged_in'):
            flash('Necesitás iniciar sesión para acceder al panel.', 'error')
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated

# ── Rutas públicas ────────────────────────────────────────────────────────────
@app.route('/')
def index():
    db = get_db()
    destacados = db.execute(
        'SELECT * FROM productos WHERE destacado=1 ORDER BY id DESC'
    ).fetchall()
    # Productos agrupados por categoría
    productos_por_cat = []
    for cat in CATEGORIAS:
        items = db.execute(
            'SELECT * FROM productos WHERE categoria=? ORDER BY nombre', (cat['id'],)
        ).fetchall()
        if items:
            productos_por_cat.append({'cat': cat, 'productos': items})
    return render_template('index.html',
                           productos_destacados=destacados,
                           productos_por_cat=productos_por_cat,
                           categorias=CATEGORIAS)


@app.route('/productos')
def catalogo():
    db = get_db()
    categoria_sel = request.args.get('categoria', None)
    if categoria_sel:
        lista = db.execute(
            'SELECT * FROM productos WHERE categoria=? ORDER BY nombre',
            (categoria_sel,)
        ).fetchall()
        cat_obj = get_cat(categoria_sel)
    else:
        lista = db.execute('SELECT * FROM productos ORDER BY categoria, nombre').fetchall()
        cat_obj = None
    return render_template('catalogo.html',
                           productos=lista,
                           categorias=CATEGORIAS,
                           categoria_sel=categoria_sel,
                           cat_obj=cat_obj)


@app.route('/producto/<int:producto_id>')
def producto_detalle(producto_id):
    db = get_db()
    producto = db.execute('SELECT * FROM productos WHERE id=?', (producto_id,)).fetchone()
    if not producto:
        flash('Producto no encontrado.', 'error')
        return redirect(url_for('catalogo'))
    relacionados = db.execute(
        'SELECT * FROM productos WHERE categoria=? AND id!=? LIMIT 3',
        (producto['categoria'], producto_id)
    ).fetchall()
    cat_obj = get_cat(producto['categoria'])
    return render_template('producto_detalle.html',
                           producto=producto,
                           relacionados=relacionados,
                           cat_obj=cat_obj)


@app.route('/buscar')
def buscar():
    """Búsqueda de productos por nombre o descripción"""
    q = request.args.get('q', '').strip()
    if not q:
        return redirect(url_for('catalogo'))
    db = get_db()
    lista = db.execute(
        '''SELECT * FROM productos
           WHERE nombre LIKE ? OR descripcion LIKE ?
           ORDER BY nombre''',
        (f'%{q}%', f'%{q}%')
    ).fetchall()
    return render_template('buscar.html',
                           productos=lista,
                           categorias=CATEGORIAS,
                           q=q)


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre  = request.form.get('nombre', '').strip()
        email   = request.form.get('email', '').strip()
        mensaje = request.form.get('mensaje', '').strip()
        if nombre and email and mensaje:
            flash('¡Gracias por tu mensaje! Te contactaremos pronto.', 'success')
            return redirect(url_for('contacto'))
        else:
            flash('Por favor completá todos los campos.', 'error')
    return render_template('contacto.html')


@app.route('/sobre-nosotros')
def sobre_nosotros():
    return render_template('sobre_nosotros.html')


# ── Carrito ───────────────────────────────────────────────────────────────────
def get_cart():
    """Devuelve el carrito de la sesión como lista de dicts con datos del producto."""
    cart = session.get('cart', {})  # {id: cantidad}
    if not cart:
        return [], 0, 0
    db = get_db()
    items = []
    total = 0
    count = 0
    for pid, qty in cart.items():
        p = db.execute('SELECT * FROM productos WHERE id=?', (pid,)).fetchone()
        if p:
            subtotal = p['precio'] * qty
            total += subtotal
            count += qty
            items.append({
                'id': p['id'],
                'nombre': p['nombre'],
                'precio': p['precio'],
                'unidad': p['unidad'],
                'imagen': p['imagen'],
                'cantidad': qty,
                'subtotal': subtotal,
            })
    return items, total, count


@app.context_processor
def inject_cart_count():
    """Hace disponible cart_count en todos los templates."""
    cart = session.get('cart', {})
    return {'cart_count': sum(cart.values()) if cart else 0}


@app.route('/carrito/agregar/<int:pid>', methods=['POST'])
def carrito_agregar(pid):
    db = get_db()
    producto = db.execute('SELECT * FROM productos WHERE id=?', (pid,)).fetchone()
    if not producto:
        flash('Producto no encontrado.', 'error')
        return redirect(url_for('catalogo'))

    qty = request.form.get('cantidad', 1, type=int)
    if qty < 1:
        qty = 1

    cart = session.get('cart', {})
    pid_str = str(pid)
    cart[pid_str] = cart.get(pid_str, 0) + qty
    session['cart'] = cart
    flash(f'"{producto["nombre"]}" agregado al carrito.', 'success')

    # Si es AJAX, devolver JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'ok': True, 'count': sum(cart.values())})

    return redirect(request.referrer or url_for('catalogo'))


@app.route('/carrito')
def carrito():
    items, total, count = get_cart()
    return render_template('carrito.html', items=items, total=total, count=count)


@app.route('/carrito/actualizar/<int:pid>', methods=['POST'])
def carrito_actualizar(pid):
    qty = request.form.get('cantidad', 1, type=int)
    if qty < 1:
        qty = 1
    cart = session.get('cart', {})
    pid_str = str(pid)
    if pid_str in cart:
        cart[pid_str] = qty
        session['cart'] = cart
        flash('Carrito actualizado.', 'success')
    return redirect(url_for('carrito'))


@app.route('/carrito/quitar/<int:pid>', methods=['POST'])
def carrito_quitar(pid):
    cart = session.get('cart', {})
    pid_str = str(pid)
    if pid_str in cart:
        del cart[pid_str]
        session['cart'] = cart
        flash('Producto quitado del carrito.', 'success')
    return redirect(url_for('carrito'))


@app.route('/carrito/vaciar', methods=['POST'])
def carrito_vaciar():
    session.pop('cart', None)
    flash('Carrito vaciado.', 'success')
    return redirect(url_for('carrito'))


@app.route('/carrito/checkout')
def carrito_checkout():
    """Genera el mensaje de WhatsApp con todos los productos del carrito."""
    items, total, count = get_cart()
    if not items:
        flash('El carrito está vacío.', 'error')
        return redirect(url_for('carrito'))

    texto = "🛒 *Pedido - Supermercado EYM*%0A%0A"
    for item in items:
        texto += f"• {item['nombre']} x{item['cantidad']} - ₲{item['subtotal']:,.0f}%0A"
    texto += f"%0A*Total: ₲{total:,.0f}*%0A%0A¿Confirmás el pedido?"
    return redirect(f"https://wa.me/595985328017?text={texto}")


# ── Admin: login / logout ─────────────────────────────────────────────────────
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if session.get('admin_logged_in'):
        return redirect(url_for('admin_dashboard'))
    if request.method == 'POST':
        user = request.form.get('usuario', '').strip()
        pwd  = request.form.get('password', '').strip()
        if user == ADMIN_USER and pwd == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            flash('Bienvenido al panel de administración.', 'success')
            return redirect(url_for('admin_dashboard'))
        flash('Usuario o contraseña incorrectos.', 'error')
    return render_template('admin/login.html')


@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    flash('Sesión cerrada.', 'success')
    return redirect(url_for('admin_login'))


# ── Admin: dashboard ──────────────────────────────────────────────────────────
@app.route('/admin')
@login_required
def admin_dashboard():
    db = get_db()
    total     = db.execute('SELECT COUNT(*) FROM productos').fetchone()[0]
    destacados = db.execute('SELECT COUNT(*) FROM productos WHERE destacado=1').fetchone()[0]
    por_cat   = db.execute(
        'SELECT categoria, COUNT(*) as cnt FROM productos GROUP BY categoria'
    ).fetchall()
    ultimos   = db.execute(
        'SELECT * FROM productos ORDER BY id DESC LIMIT 5'
    ).fetchall()
    return render_template('admin/dashboard.html',
                           total=total,
                           destacados=destacados,
                           por_cat=por_cat,
                           ultimos=ultimos,
                           categorias=CATEGORIAS)


# ── Admin: listar productos ───────────────────────────────────────────────────
@app.route('/admin/productos')
@login_required
def admin_productos():
    db = get_db()
    categoria_sel = request.args.get('categoria', '')
    busqueda      = request.args.get('q', '').strip()

    query  = 'SELECT * FROM productos WHERE 1=1'
    params = []
    if categoria_sel:
        query += ' AND categoria=?'
        params.append(categoria_sel)
    if busqueda:
        query += ' AND (nombre LIKE ? OR descripcion LIKE ?)'
        params += [f'%{busqueda}%', f'%{busqueda}%']
    query += ' ORDER BY categoria, nombre'

    lista = db.execute(query, params).fetchall()
    return render_template('admin/productos.html',
                           productos=lista,
                           categorias=CATEGORIAS,
                           categoria_sel=categoria_sel,
                           busqueda=busqueda)


# ── Admin: crear producto ─────────────────────────────────────────────────────
@app.route('/admin/productos/nuevo', methods=['GET', 'POST'])
@login_required
def admin_nuevo_producto():
    if request.method == 'POST':
        nombre      = request.form.get('nombre', '').strip()
        descripcion = request.form.get('descripcion', '').strip()
        precio      = request.form.get('precio', '0').strip()
        unidad      = request.form.get('unidad', '').strip()
        categoria   = request.form.get('categoria', '').strip()
        origen      = request.form.get('origen', 'Local').strip()
        destacado   = 1 if request.form.get('destacado') else 0

        errors = []
        if not nombre:      errors.append('El nombre es obligatorio.')
        if not descripcion: errors.append('La descripción es obligatoria.')
        if not unidad:      errors.append('La unidad es obligatoria.')
        if not categoria:   errors.append('La categoría es obligatoria.')
        try:
            precio_val = float(precio)
            if precio_val < 0:
                errors.append('El precio no puede ser negativo.')
        except ValueError:
            errors.append('El precio debe ser un número.')
            precio_val = 0

        # Imagen
        imagen_nombre = 'img1.jpg'
        file = request.files.get('imagen')
        if file and file.filename:
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                imagen_nombre = 'productos/' + filename
            else:
                errors.append('Formato de imagen no permitido. Usá JPG, PNG o WEBP.')

        if errors:
            for e in errors:
                flash(e, 'error')
            return render_template('admin/form_producto.html',
                                   categorias=CATEGORIAS,
                                   modo='nuevo',
                                   form=request.form)

        db = get_db()
        db.execute('''
            INSERT INTO productos
                (nombre, descripcion, precio, unidad, imagen, categoria, origen, destacado)
            VALUES (?,?,?,?,?,?,?,?)
        ''', (nombre, descripcion, precio_val, unidad, imagen_nombre, categoria, origen, destacado))
        db.commit()
        flash(f'Producto "{nombre}" creado correctamente.', 'success')
        return redirect(url_for('admin_productos'))

    return render_template('admin/form_producto.html',
                           categorias=CATEGORIAS,
                           modo='nuevo',
                           form={})


# ── Admin: editar producto ────────────────────────────────────────────────────
@app.route('/admin/productos/<int:pid>/editar', methods=['GET', 'POST'])
@login_required
def admin_editar_producto(pid):
    db = get_db()
    producto = db.execute('SELECT * FROM productos WHERE id=?', (pid,)).fetchone()
    if not producto:
        flash('Producto no encontrado.', 'error')
        return redirect(url_for('admin_productos'))

    if request.method == 'POST':
        nombre      = request.form.get('nombre', '').strip()
        descripcion = request.form.get('descripcion', '').strip()
        precio      = request.form.get('precio', '0').strip()
        unidad      = request.form.get('unidad', '').strip()
        categoria   = request.form.get('categoria', '').strip()
        origen      = request.form.get('origen', 'Local').strip()
        destacado   = 1 if request.form.get('destacado') else 0

        errors = []
        if not nombre:      errors.append('El nombre es obligatorio.')
        if not descripcion: errors.append('La descripción es obligatoria.')
        if not unidad:      errors.append('La unidad es obligatoria.')
        if not categoria:   errors.append('La categoría es obligatoria.')
        try:
            precio_val = float(precio)
            if precio_val < 0:
                errors.append('El precio no puede ser negativo.')
        except ValueError:
            errors.append('El precio debe ser un número.')
            precio_val = 0

        imagen_nombre = producto['imagen']
        file = request.files.get('imagen')
        if file and file.filename:
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                imagen_nombre = 'productos/' + filename
            else:
                errors.append('Formato de imagen no permitido. Usá JPG, PNG o WEBP.')

        if errors:
            for e in errors:
                flash(e, 'error')
            return render_template('admin/form_producto.html',
                                   categorias=CATEGORIAS,
                                   modo='editar',
                                   producto=producto,
                                   form=request.form)

        db.execute('''
            UPDATE productos
            SET nombre=?, descripcion=?, precio=?, unidad=?, imagen=?,
                categoria=?, origen=?, destacado=?
            WHERE id=?
        ''', (nombre, descripcion, precio_val, unidad, imagen_nombre,
              categoria, origen, destacado, pid))
        db.commit()
        flash(f'Producto "{nombre}" actualizado.', 'success')
        return redirect(url_for('admin_productos'))

    return render_template('admin/form_producto.html',
                           categorias=CATEGORIAS,
                           modo='editar',
                           producto=producto,
                           form=dict(producto))


# ── Admin: eliminar producto ──────────────────────────────────────────────────
@app.route('/admin/productos/<int:pid>/eliminar', methods=['POST'])
@login_required
def admin_eliminar_producto(pid):
    db = get_db()
    producto = db.execute('SELECT * FROM productos WHERE id=?', (pid,)).fetchone()
    if producto:
        db.execute('DELETE FROM productos WHERE id=?', (pid,))
        db.commit()
        flash(f'Producto "{producto["nombre"]}" eliminado.', 'success')
    else:
        flash('Producto no encontrado.', 'error')
    return redirect(url_for('admin_productos'))


# ── Admin: toggle destacado ───────────────────────────────────────────────────
@app.route('/admin/productos/<int:pid>/destacado', methods=['POST'])
@login_required
def admin_toggle_destacado(pid):
    db = get_db()
    producto = db.execute('SELECT * FROM productos WHERE id=?', (pid,)).fetchone()
    if producto:
        nuevo = 0 if producto['destacado'] else 1
        db.execute('UPDATE productos SET destacado=? WHERE id=?', (nuevo, pid))
        db.commit()
    return redirect(request.referrer or url_for('admin_productos'))


# ── Inicialización ────────────────────────────────────────────────────────────
with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
