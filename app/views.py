from app import app, db, lm, bcrypt
from flask import render_template, request, flash, redirect, session, url_for, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import NewForm, LoginForm, JoinForm, ContactForm, MailingForm
from .models import User, List, Item, Aisle

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
  login = LoginForm()
  join = JoinForm()
  contact = ContactForm()
  mail = MailingForm()
  if login.validate_on_submit():
    user = User.query.filter_by(email=login.inputEmailIn.data).first_or_404()
    if user and bcrypt.check_password_hash(user.password, login.inputPasswordIn.data):
      db.session.add(user)
      db.session.commit()
      login_user(user, remember=True)
      print current_user.email
      return redirect("/myAisleMate/rb")
    else:
      flash("Incorrect email or password")
      return redirect("/index")
  elif join.validate_on_submit():
    user = User(
      email=join.inputEmailUp.data, 
      password=join.inputPasswordUp1.data
    )
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return redirect("/myAisleMate/rb")
  return render_template('index.html',
                         title ='Home',
                         login = login,
                         join = join,
                         contact = contact,
                         mail = mail)

@app.route('/myAisleMate/<supermarket>')
def home(supermarket):
  print supermarket
  current_list = List.query.filter_by(user_id=current_user.id).first()
  items = None
  if current_list is not None:
    items = Item.query.filter_by(list_id=current_user.id)
  else:
    items = Item.query.filter_by(list_id=1)
  aisles = []
  order = []
  for item in items:
    if item.aisle not in aisles:
      aisles.append(item.aisle)
  if supermarket == 'rb':
    order = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
  elif supermarket == 'rh':
    order = [2,3,6,1,8,10,4,5,7,21,16,11,9,12,13,14,15,17,18,19,20,22]
  elif supermarket == 'mj':
    order = [22,1,6,9,20,17,10,8,4,12,19,3,14,5,16,2,7,11,13,15,18,21]
  else:
    return redirect('myAisleMate/rb')
  return render_template('myAisleMate.html', aisles=aisles, order=order, items=items, supermarket=supermarket)

@app.route('/newItem', methods=['GET', 'POST'])
def add():
  new = NewForm()
  if request.method == 'POST':
    if new.validate_on_submit:
      name = new.item.data
      aisle_name = new.aisle.data
      aisle_id = Aisle.query.filter_by(name=aisle_name).first()
      current_list = List.query.filter_by(user_id=current_user.id).first()
      if current_list is not None:
        print 'hi'
        item = Item(name=name, aisle=aisle_id, owner=current_list)
        db.session.add(item)
        db.session.commit()
        return redirect('/myAisleMate/rb')
      else:
        nl = List(user_id=current_user.id)
        item = Item(name=name, aisle=aisle_id, owner=nl)
        db.session.add(item)
        db.session.commit()
        print 'no'
        return redirect('/myAisleMate/rb')
  return render_template('newItem.html', new=new)

@app.route('/remove/<item>', methods=['GET', 'POST'])
def remove(item):
  message = None
  current_list = List.query.filter_by(user_id=current_user.id).first()
  i = Item.query.filter_by(name=item, owner=current_list).first()
  print i.name
  db.session.delete(i)
  db.session.commit()
  return redirect('/myAisleMate/rb')


@app.route('/logout', methods=['GET'])
@login_required
def logout():
  logout_user()
  return redirect("/index")