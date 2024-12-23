#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fadil's basic flask template (v1.0)
https://github.com/wahyuakhmadfadillah/flask-template
@wahyuakhmadfadillah
"""

from flask import Flask, render_template

DEVELOPMENT_ENV = True

app = Flask(__name__)

app_data = {
    "name": "Fadil's Basic Flask Template",
    "description": "A basic Flask app using bootstrap for layout",
    "author": "Fadil",
    "html_title": "Fadil's Basic Flask Template",
    "project_name": "Basic Flask Template",
    "keywords": "flask, webapp, template, basic",
}

@app.route("/")
def index():
    return render_template("index.html", app_data = app_data)

@app.route("/about")
def about():
    return render_template("about.htmk", app_data = app_data)

@app.route("/service")
def service():
    return render_template("service.html", app_data = app_data)

@app.route("/contact")
def contact():
    return render_template("contact.html", app_data = app_data)

if __name__ == "__main__":
    app.run(debug=DEVELOPMENT_ENV)  