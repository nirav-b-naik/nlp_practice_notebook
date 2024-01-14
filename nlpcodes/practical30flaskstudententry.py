#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 10:47:48 2022

@author: dai
"""

from flask import Flask, redirect, url_for, request,render_template

app = Flask(__name__)

@app.route("/")
def student():
    return render_template('student.html')

@app.route("/result", methods = ['POST','GET'])
def result():
    if request.method == "POST":
        result = request.form
    return render_template('result.html', result = result)

if __name__=="__main__":
    app.run(host= 192.168.10.125, port=2020)
    
    print(result)
