from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)

# Flaskアプリケーションとデータベースの初期化後
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    e_mail = db.Column(db.String(50), unique=True)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False)
    phone = db.Column(db.String(50), unique=False)
    country = db.Column(db.String(50), unique=False)

with app.app_context():
    # DBを初期化（テーブルが存在しない場合に作成）
    db.create_all() 

    user = User.query.filter_by(username='testuser').first()
    if user is None:
        testuser = User(username='testuser', e_mail='test@test')
        db.session.add(testuser)
        db.session.commit()

admin = Admin(app, name='MyApp', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Member, db.session)) 

@app.route('/')
def index():
    members = Member.query.all()
    events = [

    ]

    user = User.query.filter_by(username='testuser').first()
    user_name = user.username
    return render_template(
        'index.html',
        members = members,
        user_name = user_name,
    )

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )

if __name__ == "__main__":
    app.run(debug=True)

# 次DB作成
# https://www.youtube.com/watch?v=EQIAzH0HvzQ&t=2200s
    
