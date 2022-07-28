

import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from sqlalchemy.ext.declarative import declarative_base

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///cafes.db")
db = SQLAlchemy(app)
Base = declarative_base()
wifi = ["✘","💪","💪💪","💪💪💪","💪💪💪💪","💪💪💪💪💪"]
coffee = ["✘","☕","☕☕","☕☕☕","☕☕☕☕","☕☕☕☕☕"]
power=["✘","🔌","🔌🔌","🔌🔌🔌","🔌🔌🔌🔌","🔌🔌🔌🔌"]
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    location  = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.Text, nullable=False)
    map_url = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.String(250), nullable=False)
    has_wifi = db.Column(db.String(250), nullable=False)
    can_take_calls = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(),URL(require_tld=True)])
    open = StringField(label='Opening Time e.g 8AM', validators=[DataRequired()])
    close =StringField(label='Opening Close e.g 6:30PM', validators=[DataRequired()])
    coffee = SelectField(label='Coffee Rating', choices=coffee, validators=[DataRequired()])
    Wifi = SelectField(label='Wifi Strength', choices= wifi,validators=[DataRequired()])
    power= SelectField(label='Power',choices=power ,validators=[DataRequired()])
    submit = SubmitField('Submit')

db.session.commit()



@app.route('/')
def cafes():
   
    cafe =Cafe.query.all()
    for i in cafe:
        print(i.name)
    return render_template('index.html', cafes=cafe)


if __name__ == '__main__':
    app.run(debug=True)
