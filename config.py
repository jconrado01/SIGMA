
class Config:
    USER_DB = 'postgres'
    PASS_DB = 'admin'
    URL_DB = 'localhost'
    NAME_DB = 'sigma_db'
    FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    SQLALCHEMY_DATABASE_URI = FULL_URL_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'clave-super-secreta'


