from flask import Flask, render_template
from Flask _sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)

app.config ['SQLALCHEMY DATABASE_URI:'] = 'sqlite:///minhasmensagens.db'

class Mensagem(db.model):
    id = db.column(db.interger, primary key=True)
    mensagem = db.Column(db.text, nullable=False)

    def__repre__(self)
    return self.mensagem



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nova mensagem')
def novaMensagem():
    return render_template('mensagem.html')


if __name__ == "__main__":
   app.run(debug=True)