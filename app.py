from flask import Flask, jsonify
import os
# Importamos el objeto strat_bp desde el archivo rutas
from src.routes.users import strat_bp 

app = Flask(__name__)

# Ruta de salud para Cloud Run
@app.route('/health')
def health():
    return jsonify({
        "status": "up", 
        "service": "mod-conexionMySQL",
        "database": "MySQL"
    }), 200

# Registro del Blueprint con el prefijo correcto
# Esto hará que tus rutas sean: /api/v1/strat/
app.register_blueprint(strat_bp, url_prefix='/api/v1/strat')

if __name__ == '__main__':
    # Cloud Run define la variable PORT, si no existe usa 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)