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
            "serial": p.serial
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

    nuevo = Producto(nombre=nombre, marca=marca, modelo=modelo, serial=serial)
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
    db.session.commit()
    return jsonify({"success": True, "message": "Producto actualizado exitosamente"})

@productos_bp.route('/productos/eliminar/<int:id>', methods=['POST'])
def productos_eliminar(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({"success": True, "message": "Producto eliminado exitosamente"})
