from flask import Blueprint, render_template, request, jsonify, session
from app import db
from app.models import Producto
from app.models import Usuario

productos_bp = Blueprint('productos', __name__)

@productos_bp.route('/productos')
def productos():
    #usuario = Usuario.query.get(session['usuario_id'])
    return render_template('productos/listar.html')

@productos_bp.route('/productos/data')
def productos_data():
    try:
        productos = Producto.query.all()
        data = [{
            "id": p.id,
            "nombre": p.nombre,
            "marca": p.marca,
            "modelo": p.modelo,
            "serial": p.serial,
            "unidad_medida": p.unidad_medida
        } for p in productos]
        return jsonify({"data": data})
    except Exception as e:
        return jsonify({"data": [], "error": str(e)})

@productos_bp.route('/productos/crear', methods=['POST'])
def productos_crear():
    nombre = request.form.get('nombre')
    marca = request.form.get('marca')
    modelo = request.form.get('modelo')
    serial = request.form.get('serial')
    unidad_medida = request.form.get('unidad_medida')

    nuevo = Producto(nombre=nombre, marca=marca, modelo=modelo, serial=serial, unidad_medida=unidad_medida)
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"success": True, "message": "Producto creado exitosamente"})

@productos_bp.route('/productos/editar/<int:id>', methods=['POST'])
def productos_editar(id):
    producto = Producto.query.get_or_404(id)
    producto.nombre = request.form.get('nombre')
    producto.marca = request.form.get('marca')
    producto.modelo = request.form.get('modelo')
    producto.serial = request.form.get('serial')
    producto.unidad_medida = request.form.get('unidad_medida')
    db.session.commit()
    return jsonify({"success": True, "message": "Producto actualizado exitosamente"})

@productos_bp.route('/productos/eliminar/<int:id>', methods=['POST'])
def productos_eliminar(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({"success": True, "message": "Producto eliminado exitosamente"})

@productos_bp.route('/buscar_productos', methods=['GET'])
def buscar_productos():
    termino = request.args.get('q', '').strip()
    if not termino:
        return jsonify([])

    resultados = Producto.query.filter(
        Producto.nombre.ilike(f"%{termino}%") |
        Producto.marca.ilike(f"%{termino}%") |
        Producto.modelo.ilike(f"%{termino}%") |
        Producto.serial.ilike(f"%{termino}%")
    ).limit(10).all()

    data = [
        {
            "id": p.id,
            "nombre": p.nombre,
            "marca": p.marca,
            "modelo": p.modelo,
            "serial": p.serial,
            "unidad_medida": p.unidad_medida
        }
        for p in resultados
    ]

    return jsonify(data)