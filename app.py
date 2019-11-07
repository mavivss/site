from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from formulario import Mensagemform

app = Flask(__name__)
db = SQLAlchemy(app)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhasmensagens.db'
app.config ['SECRET_KEY'] = 'virotia é incrível'

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.Text, nullable=False)

    def __repre__(self):
        return self.mensagem



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/novamensagem', methods={'POST', 'GET'})
def novaMensagem():
    
    form = Mensagemform()

    print(form.mensagem.data)
    
    return render_template('mensagem.html', form=form)


if __name__ == "__main__":
   app.run(debug=True)