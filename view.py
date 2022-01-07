# coding: utf-8
# render_templateは使用するHTMLファイルを指定するためのメソッド
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User

#appという変数にFlaskを定義
#これでFlaskが使える
app = Flask(__name__, static_folder=None)

#DBとの接続
engine = create_engine('sqlite:///test.db')
session = sessionmaker(bind= engine)()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    age = int(request.form['age'])
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
    return redirect(url_for('database'))

@app.route('/database', methods=['GET'])
def database():
    users = session.query(User).all()
    return render_template('database.html', users=users)

#メイン関数
if __name__ == '__main__':
    app.run(debug=True)