from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:7174302@localhost/height_collector'
app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://zlujqjtzrmtogg:f3a9a3a7044f249c514c8ce9375ab81c09a5ff0ec0c53afba589f533784ab53b@ec2-54-83-51-78.compute-1.amazonaws.com:5432/deeq6kcv3po5u0?sslmode=require'

db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key= True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/succses", methods=['POST'])

def succses():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]

        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data = Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height=round(average_height,1)
            send_email(email, height, average_height)
            return render_template("succses.html")
        return render_template("index.html", text = "Email already exist!")



if __name__ == '__main__':
    app.debug = True
    app.run()
