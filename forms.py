from wtforms import Form
from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField,FieldList,FormField,SelectField,RadioField

from wtforms.fields import EmailField
from wtforms import validators

def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula = StringField('Matricula',
    [validators.DataRequired(message='El campo es requerido'),
     validators.length(min=5,max=10,message='Ingrese minimo 5 maximo 10')])
    nombre=StringField('Nombre',
    [validators.DataRequired(message='El campo nombre es requerido'),
     validators.length(min=5,max=10,message='Ingrese minimo 5 maximo 10')])

    apaterno=StringField('Apaterno',[mi_validacion])
    amaterno=StringField('Amaterno')
    email=EmailField('Correo')


class LoginForm(Form):
    username = StringField('Usuario',
    [validators.DataRequired(message='El campo es requerido'),
     validators.length(min=5,max=10,message='Ingrese minimo 5 maximo 10')])
    password = PasswordField('Contraseña',
    [validators.DataRequired(message='El campo nombre es requerido'),
     validators.length(min=5,max=10,message='Ingrese minimo 5 maximo 10')])