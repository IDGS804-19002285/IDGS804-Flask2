from flask import Flask, render_template
from flask import request
from flask import make_response
from flask_wtf.csrf import CSRFProtect
from flask import flash
import traductor
import forms

app = Flask (__name__)
# app.config['SECRET_KEY']="Esta es una clave encriptada"
# csrf=CSRFProtect()

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


@app.route("/traducir", methods=['GET','POST'])
def traducir():
    req_in = traductor.traducirIn(request.form)
    req_out = traductor.traducirOut(request.form)
    datos = list()
    pal2 = ''
    # if request.method == 'POST' and req_in.validate():
    if request.method == 'POST':
        if req_out.envio.data == 'tra' and req_out.validate():
            palabra = ''
            for d in req_out.pal.data:
                palabra += d.lower()

            e=open('traductor_esp.txt','r')
            i=open('traductor_ing.txt','r')
            dicionarioE = e.readlines()
            dicionarioI = i.readlines()

            if req_out.idioma.data == 'esp':
                
                for item in dicionarioE:
                    if palabra == item.replace('\n',''):
                        pal2 = dicionarioI[dicionarioE.index(item)].replace('\n','')
            else:
                for item in dicionarioI:
                    if palabra == item.replace('\n',''):
                        pal2 = dicionarioE[dicionarioI.index(item)].replace('\n','')
                        
            e.close()
            i.close()
            datos.append('La palabra traducida fue: "'+palabra+'"')

        if req_in.envio.data == 'gua' and req_in.validate():
            esp = ''
            ing = ''
            for d in req_in.esp.data:
                esp += d.lower()
            for d in req_in.ing.data:
                ing += d.lower()
            datos.append('Palabra guardada (Español) '+esp)
            datos.append('Palabra guardada (Ingles) '+ing)
            e=open('traductor_esp.txt','a')
            i=open('traductor_ing.txt','a')
            e.write(esp+'\n')
            i.write(ing+'\n')
            e.close()
            i.close()

    return render_template("traductor.html",formIn=req_in,formOut=req_out, datos=datos,pal2 = pal2)


# @app.route("/cookies",methods=['GET','POST'])
# def cookies():
#     reg_user=forms.LoginForm(request.form)
#     response = make_response(render_template('cookies.html',form=reg_user,))

#     if request.method == 'POST' and reg_user.validate():
#         user=reg_user.username.data
#         password=reg_user.password.data
#         datos=user+'@'+password
#         success_message = 'Bienvenid@ {}'.format(user)
#         response.set_cookies('datos_usuario',datos)
#         flash(success_message)
#     return response

if __name__=='__main__':
    # csrf.init_app(app)
    app.run(debug=True,port=3000)