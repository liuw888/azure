import os
import sys
from werkzeug.utils import secure_filename
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, flash
import datetime
from bs4 import BeautifulSoup



@app.route('/', methods=['GET', 'POST'])
def index():
    print('app works')
  
    return 'Hello World!'


@app.route("/hi")
def hi():
    return "Hi World!"



if __name__ == "__main__":
    app.run(debug=True)
