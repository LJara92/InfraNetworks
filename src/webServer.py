from flask import *

app = Flask(__name__)

#Rutas 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inicio')
def inico():
    return render_template("index.html")

@app.route('/nosotros')
def nosotros():
    return render_template("nosotros.html")
    
@app.route('/contacto')
def contacto():
    return render_template("contacto.html")



app.run(host='0.0.0.0', port=5000, debug=True)