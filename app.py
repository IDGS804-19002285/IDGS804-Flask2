from flask import Flask, render_template
from flask import request
from flask import make_response
from flask_wtf.csrf import CSRFProtect
from flask import flash
import forms

app = Flask (__name__)
app.config['SECRET_KEY']="Esta es una clave encriptada"
csrf=CSRFProtect()

@app.route("/formprueba")
def formprueba():
  
    return render_template("formprueba.html")

@app.route("/Alumnos",methods=['GET','POST'])
def Alumnos():
    reg_alum=forms.UserForm(request.form)
    datos = list()
    if request.method == 'POST' and reg_alum.validate():
        datos.append(reg_alum.matricula.data)
        datos.append(reg_alum.nombre.data)
        print(reg_alum.matricula.data)
        print(reg_alum.nombre.data)
    return render_template("Alumnos.html", form=reg_alum,datos=datos)

@app.route("/traductor",methods=['GET','POST'])
def traductor():
    reg_alum=forms.UserForm(request.form)
    datos = list()
    if request.method == 'POST' and reg_alum.validate():
        datos.append(reg_alum.matricula.data)
        datos.append(reg_alum.nombre.data)
        print(reg_alum.matricula.data)
        print(reg_alum.nombre.data)
    return render_template("traductor.html", form=reg_alum,datos=datos)


@app.route("/cookies",methods=['GET','POST'])
def cookies():
    reg_user=forms.LoginForm(request.form)
    response = make_response(render_template('cookies.html',form=reg_user,))

    if request.method == 'POST' and reg_user.validate():
        user=reg_user.username.data
        password=reg_user.password.data
        datos=user+'@'+password
        success_message = 'Bienvenid@ {}'.format(user)
        response.set_cookies('datos_usuario',datos)
        flash(success_message)
    return response

if __name__=='__main__':
    csrf.init_app(app)
    app.run(debug=True,port=3000)