import os
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
# https://pythonspot.com/en/flask-web-forms/
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Wikipedia URL:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    print (form.errors)
    if request.method == 'POST':
        name='"' + request.form['name'] + '"'
        print (name)
        os.system('wget -O file.html ' + name )
        os.system('python3 analyzer.py file.html > templates/data.js')



        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')

    return render_template('d3js/index.html', form=form)

@app.route("/data.js")
def data():
    return render_template('data.js')

@app.route("/histogram.html")
def historgam():
    return render_template('d3js/histogram.html')

@app.route("/force.html")
def force():
    return render_template('d3js/force.html')

@app.route("/minimap_wrapper.html")
def minimap_wrapper():
    return render_template('d3js/minimap_wrapper.html')

@app.route("/minimap2.html")
def minimap():
    return render_template('d3js/minimap2.html')

@app.route("/lexical_dispersion_plot.html")
def lexical_dispersion_plot():
    return render_template('d3js/lexical_dispersion_plot.html')

@app.route("/bubble.html")
def bubble():
    return render_template('d3js/bubble.html')

@app.route("/star.html")
def star():
    return render_template('d3js/star.html')


if __name__ == "__main__":
    app.run()
