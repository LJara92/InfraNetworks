from flask import Flask, request, render_template, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'infranetworks@hotmail.com'  
app.config['MAIL_PASSWORD'] = ''
app.config['SECRET_KEY'] = ''

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inicio')
def inicio():
    return render_template("index.html")

@app.route('/nosotros')
def nosotros():
    return render_template("nosotros.html")
    
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        company = request.form['company']
        preferred_contact_time = request.form['preferred_contact_time']
        message = request.form['message']
        
        msg = Message(f'*** Contacto "{name}" ***', 
                      sender='infranetworks@hotmail.com',
                      recipients=['infranetworks@hotmail.com'])
        msg.body = f"""
        Nombre: {name}
        E-mail: {email}
        Teléfono: {phone}
        Empresa: {company if company else 'No especificado'}
        Horario de disponibilidad: {preferred_contact_time}
        Mensaje: {message}
        """
        try:
            mail.send(msg)
            flash('Su mensaje ha sido enviado. ¡Muchas gracias!')
        except Exception as e:
            flash('Error, mensaje no enviado')
    
        return redirect(url_for('contacto'))
    
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
