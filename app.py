from flask import Flask, render_template
from flask import request
from flask_wtf.csrf import CSRFProtect

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
    if request.method == 'POST':
        print(reg_alum.matricula.data)
        print(reg_alum.nombre.data)
    return render_template("Alumnos.html", form=reg_alum)



if __name__=='__main__':
    csrf.init_app(app)
    app.run(debug=True,port=3000)