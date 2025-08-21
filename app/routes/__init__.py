from .main import main_bp
from .auth import auth_bp
from .productos import productos_bp

all_blueprints = [
    main_bp,
    auth_bp,
    productos_bp
]