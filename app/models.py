from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.Boolean, default=True, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    marca = db.Column(db.String(100))
    modelo = db.Column(db.String(100))
    serial = db.Column(db.String(100))
    stock = db.Column(db.Numeric(12, 2), default=0)
    unidad_medida = db.Column(db.String(50))

    def __repr__(self):
        return f"<Producto {self.nombre}>"

class EntradaAlmacen(db.Model):
    __tablename__ = 'entrada_almacen'
    id_entrada = db.Column(db.Integer, primary_key=True)
    contrato_suministro = db.Column(db.String(100), nullable=False)
    id_contratista = db.Column(db.String(20), nullable=False)
    nombre_contratista = db.Column(db.String(150), nullable=False)
    documento_representante = db.Column(db.String(20))
    nombre_representante = db.Column(db.String(150))
    objeto_contrato = db.Column(db.Text)
    valor_contrato = db.Column(db.Numeric(15,2))
    plazo_contrato = db.Column(db.String(100))
    acta_inicio = db.Column(db.Date)
    supervisor_contrato = db.Column(db.String(150))
    notas = db.Column(db.Text)
    fecha_registro = db.Column(db.DateTime, server_default=db.func.now())

    detalles = db.relationship("EntradaDetalle", backref="entrada", cascade="all, delete-orphan")

class EntradaDetalle(db.Model):
    __tablename__ = 'entrada_detalle'
    id_detalle = db.Column(db.Integer, primary_key=True)
    id_entrada = db.Column(db.Integer, db.ForeignKey("entrada_almacen.id_entrada"), nullable=False)
    id_producto = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable=False)
    cantidad = db.Column(db.Numeric(12,2), nullable=False)
    fecha_registro = db.Column(db.DateTime, server_default=db.func.now())