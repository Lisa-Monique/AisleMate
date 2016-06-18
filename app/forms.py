from flask.ext.wtf import Form
from wtforms import SelectField, TextField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Email, EqualTo

# input_name&id = FieldType("Label Text")
class LoginForm(Form):
    inputEmailIn = TextField("Email Address", [InputRequired(message='Please enter valid email address'), Email(message='Please enter valid email address')])
    inputPasswordIn = PasswordField("Password", [InputRequired(message='Please enter password')])
    submitIn = SubmitField("Sign me in!")

class JoinForm(Form):
    inputEmailUp = TextField("Email Address", [InputRequired(message='Please enter email address'), Email(message='Please enter valid email address')])
    inputPasswordUp1 = PasswordField("Password", [InputRequired(message='Please enter password'), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField("Repeat Password")
    submitUp = SubmitField("Sign me up!")

class ContactForm(Form):
	name = TextField("Your Name", [InputRequired(message="Please enter your name")])
	email = TextField("Your Email", [InputRequired(message="Please enter your email address"), Email(message='Please enter valid email address')])
	message = TextAreaField("Message")

class MailingForm(Form):
	mailEmail = TextField("YOUR EMAIL ADDRESS", [InputRequired(message="Please enter your email address"), Email(message='Please enter valid email address')])
	submitMail = SubmitField("Subscribe Me!")

class NewForm(Form):
    item = TextField("Name of Item", [InputRequired(message="Please choose an item")])
    aisle = SelectField(u'Aisle', choices=[('Dairy, Milk, Eggs', 'Dairy, Milk, Eggs'), ('Petcare', 'Petcare'), ('Babycare', 'Babycare'), ('Snacks', 'Snacks'), ('Grains, Pasta', 'Grains, Pasta'), ('Breakfast', 'Breakfast'), ('Cleaning', 'Cleaning'), ('Frozen Food', 'Frozen Food'), ('Meat', 'Meat'), ('Baking', 'Baking'), ('Canned Food', 'Canned Food'), ('Toilettries', 'Toilettries'), ('Drinks', 'Drinks'), ('Deli', 'Deli'), ('Bakery', 'Bakery'), ('Produce', 'Produce'), ('Tobacco', 'Tobacco'), ('NewsPapers', 'Newspapers'), ('Flowers', 'Flowers'), ('Alcohol', 'Alcohol'), ('Pharmacy', 'Pharmacy'), ('Miscellaneous', 'Miscellaneous')])
    submitItem = SubmitField("Add Item!")
