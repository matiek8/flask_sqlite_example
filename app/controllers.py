from flask import Flask, render_template
from . import app
from .models import File


@app.route('/')
def index():
    files = File.query.all()
    return render_template('index.html', files=files)
