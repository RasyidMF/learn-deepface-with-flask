from helper.utils import getEnv

from flask import Flask
from flask_cors import CORS

from routes.home import home
from routes.api import api

def boot():
    app = Flask(getEnv('FLASK_NAME', __name__))
    
    # Disable CORS
    CORS(app)
    
    # Register Blueprints
    app.register_blueprint(home)
    app.register_blueprint(api)
    
    # Running the service
    app.run(
        host=getEnv('FLASK_HOST', '0.0.0.0'),
        port=getEnv('FLASK_PORT', '8000'),
        debug=getEnv('APP_DEBUG', 'true') == 'true'
    )
    
# Starting Flask App
if __name__ == "__main__":
    boot()