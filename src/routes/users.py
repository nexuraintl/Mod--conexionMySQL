from flask import Blueprint, request, jsonify
from src.database.db_mysql import MySQLManager
from config import Config

strat_bp = Blueprint('strat_bp', __name__)

# READ: Obtener registros
@strat_bp.route('/', methods=['GET'])
def get_data():
    conn = MySQLManager.get_connection()
    try:
        with conn.cursor() as cursor:
            # Usamos el nombre de la tabla desde la configuración
            cursor.execute(f"SELECT * FROM {Config.MYSQL_TABLE} LIMIT 100")
            result = cursor.fetchall()
            return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# CREATE: Insertar registro
@strat_bp.route('/', methods=['POST'])
def create_data():
    data = request.json
    conn = MySQLManager.get_connection()
    try:
        with conn.cursor() as cursor:
            # Ejemplo: asumiendo columnas 'campo1' y 'campo2', ajusta según tu tabla
            columns = ", ".join(data.keys())
            placeholders = ", ".join(["%s"] * len(data))
            sql = f"INSERT INTO {Config.MYSQL_TABLE} ({columns}) VALUES ({placeholders})"
            cursor.execute(sql, list(data.values()))
        conn.commit()
        return jsonify({"message": "Registro exitoso"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# UPDATE: Actualizar un registro por ID
@strat_bp.route('/<int:id>', methods=['PUT'])
def update_data(id):
    data = request.json
    if not data:
        return jsonify({"error": "No se proporcionaron datos para actualizar"}), 400

    conn = MySQLManager.get_connection()
    try:
        with conn.cursor() as cursor:
            # Construimos la consulta dinámicamente según los campos enviados
            # Ejemplo: SET campo1=%s, campo2=%s
            fields = ", ".join([f"{key}=%s" for key in data.keys()])
            values = list(data.values())
            values.append(id) # Para el WHERE id = %s

            sql = f"UPDATE {Config.MYSQL_TABLE} SET {fields} WHERE id = %s"
            
            cursor.execute(sql, values)
            
            if cursor.rowcount == 0:
                return jsonify({"message": "No se encontró el registro o no hubo cambios"}), 404
                
        conn.commit()
        return jsonify({"message": "Registro actualizado correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()