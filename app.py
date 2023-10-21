from flask import Flask
from flask import render_template,request
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import data_required

FAI=Flask(__name__)
@FAI.route('/wish/<name>')
def wish(name):
    return f'Good Morning {name}'

@FAI.route('/page')
def page():
    return render_template('first.html',Name='Deepthi')

@FAI.route('/page2')
def page2():
    return render_template('second.html')

@FAI.route('/htmlforms',methods=['GET','POST'])
def htmlforms():
    if request.method=='POST':
        fd=request.form
        return fd['n']
    return render_template('htmlforms.html')

class NameForm(Form):
    name=StringField(validators=[data_required()])

@FAI.route('/webforms',methods=['GET','POST'])
def webforms():
    form=NameForm()
    if request.method=='POST':
        NFO=NameForm.reques


if __name__=='__main__':
    FAI.run(debug=True)

