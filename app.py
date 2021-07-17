from flask import Flask
from utils import util
from erp.blueprints.home import Home

app = Flask(__name__)
app.secret_key = util.as_base64(util.get_ip()+'_mini_erp')

app.register_blueprint(Home)

app.run(debug=True, use_reloader=True)
