from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Mensagemform(FlaskForm):
    mensagem = StringField('Mensagem:', validators=[DataRequired])
    botao = SubmitField('enviar msg')