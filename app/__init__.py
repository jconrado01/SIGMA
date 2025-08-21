from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Importa y registra todos los blueprints
    from app.routes import all_blueprints
    for bp in all_blueprints:
        app.register_blueprint(bp)

    # Context processor: agrega `usuario` automáticamente a todas las plantillas
    @app.context_processor
    def inject_usuario():
        from app.models import Usuario  # Import aquí para evitar el ciclo
        usuario = None
        if 'usuario_id' in session:
            usuario = Usuario.query.get(session['usuario_id'])
        return dict(usuario=usuario)

    return app
