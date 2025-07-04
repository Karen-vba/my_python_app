from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "postgresql://admin:123456@127.0.0.1:5432/testdb"

db = SQLAlchemy(app)

class Students(db.Model):

    __tablename__ = "Students"
    sid  = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    tel  = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    email= db.Column(db.String(100))

    def __init__(self, name, tel, addr, email):
        self.name = name
        self.tel = tel
        self.addr = addr
        self.email= email

#
@app.route("/")
def index():
    db.create_all()
    return "資料庫連線成功!"

@app.route("/insert")
def insert():
    student=Students("炭治郎","0910111111","台北市","demo@demo.com")
    db.session.add(student)
    db.session.commit()
    return "新增一筆記錄成功!"

@app.route("/insertall")
def insert_all():
    student1=Students("大郎","0910111111","台北市","demo@demo.com")
    student2=Students("小郎","0910111111","台北市","demo@demo.com")
    student=(student1,student2)
    db.session.add_all(student)
    db.session.commit()
    return "新增多筆記錄成功!"


if __name__=="__main__":
    app.run()












    



