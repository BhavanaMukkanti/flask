# in this python file we need to create an Application instance
# application instance is nothing but the object of Flask class of flask package

from flask import Flask,render_template,request

app=Flask(__name__)# application instance

app.config['SECRET_KEY']='csrftoken'

from flask_wtf import Form

from wtforms import StringField,SubmitField

from wtforms.validators import Required

# appliation instance is having  route method


@app.route('/fun1')
def fun1():
    return 'hai this our first flask view function'

@app.route('/wish/<name>')
def wish(name):
    return 'hai hello MR/MS {}'.format(name)

@app.route('/template')
def template():
    return render_template('first.html',name='Django',age=23)

@app.route('/anchor')
def Anchor():
    return 'This is a navigated Anchor Tag'

@app.route('/form',methods=['GET',"POST"])
def form():
    if request.method=='POST':
        form_data=request.form
        print(form_data)
        return form_data['username']
    return render_template('form.html')

#creating a form class

class NameForm(Form):
    name=StringField('enter ur name',validators=[Required()])
    submit=SubmitField()

@app.route('/webform',methods=['GET','POST'])
def webform():
    form=NameForm()
    if form.validate_on_submit():
        name=form.data['name']
        print(form.data)
        return name
    return render_template('webform.html',form=form)


# application instance is having the run method inorder to run the server

if __name__=='__main__':

    app.run(debug=True,host='192.168.56.1',port=5001)