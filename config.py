import os

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', '10.128.0.100')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASS = os.getenv('MYSQL_PASS')
    MYSQL_DB   = os.getenv('MYSQL_DB')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))
    # Nombre de la tabla como variable de entorno
    MYSQL_TABLE = os.getenv('MYSQL_TABLE', 'tn_virtuales_estratificacion')