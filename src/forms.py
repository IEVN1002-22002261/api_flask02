from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, SelectField, EmailField, BooleanField, SubmitField, IntegerField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField("Matricula",[validators.DataRequired(message='El campo es requerido')])
    nombre=StringField("Nombre",[validators.DataRequired(message='El campo es requerido')])
    apellido=StringField("Apellido",[validators.DataRequired(message='El campo es requerido')])
    email=EmailField("Correo",[validators.Email(message='El campo es requerido')])