from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired('Este campo es requerido')])
    password = PasswordField('Contraseña', validators=[DataRequired('Este campo es requerido')])
    enviar = SubmitField('Iniciar sesión')


class IngresoForm(FlaskForm):
    fecha = StringField('Fecha', validators=[DataRequired('Este campo es requerido')])
    nombre = StringField('Nombre', validators=[])
    apellido = StringField('Apellido', validators=[])
    dni = StringField('DNI', validators=[DataRequired('Este campo es requerido')])
    enviar = SubmitField('Enviar')
    cancelar = SubmitField('Cancelar', render_kw={'class': 'btn btn-secondary', 'formnovalidate': 'True'})

