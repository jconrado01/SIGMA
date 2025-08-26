from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db  # tu objeto SQLAlchemy
from app.models import EntradaAlmacen, EntradaDetalle, Producto  # los modelos ORM

bp_entradas = Blueprint('entradas', __name__, url_prefix='/entradas')

# Listar entradas
@bp_entradas.route('/')
def index():
    entradas = EntradaAlmacen.query.order_by(EntradaAlmacen.id_entrada.desc()).all()
    return render_template('entradas/index.html', entradas=entradas)

# Crear nueva entrada
@bp_entradas.route('/nueva', methods=['GET', 'POST'])
def nueva():
    productos = Producto.query.all()

    if request.method == 'POST':
        # Cabecera
        entrada = EntradaAlmacen(
            contrato_suministro=request.form['contrato_suministro'],
            id_contratista=request.form['id_contratista'],
            nombre_contratista=request.form['nombre_contratista'],
            documento_representante=request.form['documento_representante'],
            nombre_representante=request.form['nombre_representante'],
            objeto_contrato=request.form['objeto_contrato'],
            valor_contrato=request.form['valor_contrato'],
            plazo_contrato=request.form['plazo_contrato'],
            acta_inicio=request.form['acta_inicio'],
            supervisor_contrato=request.form['supervisor_contrato'],
            notas=request.form['notas']
        )
        db.session.add(entrada)
        db.session.flush()  # para obtener id_entrada antes de commit

        # Detalles (pueden venir como listas desde el formulario)
        ids_productos = request.form.getlist('id_producto')
        cantidades = request.form.getlist('cantidad')

        for i in range(len(ids_productos)):
            detalle = EntradaDetalle(
                id_entrada=entrada.id_entrada,
                id_producto=ids_productos[i],
                cantidad=cantidades[i]
            )
            db.session.add(detalle)

        db.session.commit()
        flash("Entrada registrada con éxito", "success")
        return redirect(url_for('entradas.index'))

    return render_template('entradas/nueva.html', productos=productos)
