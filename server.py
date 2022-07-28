


from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from flask_sqlalchemy import SQLAlchemy
#
# TEMPLATE_DIR = os.path.abspath('../templates')
# STATIC_DIR = os.path.abspath('../static')
app = Flask(__name__)


app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"
db = SQLAlchemy(app)
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
# all Flask routes below
# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route('/add',methods=["POST" ,"GET"])
# def add_cafe():
#     form = CafeForm()
#     if form.validate_on_submit():
#         with open('cafe-data.csv', mode="a") as file:
#             csv_data = file.write(f"\n{form.cafe.data},{form.location.data},{form.open.data},{form.close.data},{form.coffee.data},{form.Wifi.data},{form.power.data}")
#
#         print("True")
#     # Exercise:
#     # Make the form write a new row into cafe-data.csv
#     # with   if form.validate_on_submit()
#     return render_template('add.html', form=form)


@app.route('/')
def cafes():
    # with open('cafe-data.csv', newline='') as csv_file:
    #     csv_data = csv.reader(csv_file, delimiter=',')
    #     list_of_rows = []
    #     for row in csv_data:
    #         list_of_rows.append(row)
    cafe =Cafe.query.all()
    for i in cafe:
        print(i.name)
    return render_template('index.html', cafes=cafe)


if __name__ == '__main__':
    app.run(debug=True)
