#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'weather.html',
        data=[{'name':'Toronto', 'cid':'6167863'}, {'name':'Montreal', 'cid':'6077243'},
        {'name':'Ottawa', 'cid':'6094817'}, {'name':'Edmonton', 'cid':'5946768'},
        {'name':'Vancouver', 'cid':'6173331'}, {'name':'Brampton', 'cid':'5907364'}, 
        {'name':'Athens', 'cid':'264371'}, {'name':'Krakow', 'cid':'3094802'}])

@app.route("/result" , methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    #print(select)
    resp = query_api(select)
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error)

if __name__=='__main__':
    app.run(debug=True)
