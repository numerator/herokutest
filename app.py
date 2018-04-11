from flask import Flask, render_template, request
# import requests
# import json
import model

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <img src="/static/blockM.png"/>
        <h1>UM Sports Info!</h1>
        <ul>
            <li><a href="/bball"> Men's Basketball </a></li>
        </ul>
    '''

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    return render_template("hello.html", firstname='', lastname='')

@app.route('/bball', methods=['GET', 'POST'])
def bball():
    # sortby = 'year'     #default
    # sortorder = 'desc'  #default
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_bball_seasons(sortby, sortorder)
    else:
        seasons = model.get_bball_seasons()

    # return render_template("seasons.html", sport="Men's Basketball",
    #     seasons=seasons, sortby=sortby, sortorder=sortorder)
    return render_template("seasons.html", sport="Men's Basketball",
         seasons=seasons)


if __name__ == '__main__':
    app.run(debug=True)
