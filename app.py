from flask import Flask, render_template
from system_info import SystemInfo

app = Flask(__name__)

@app.route('/')
def index():
    system_info = SystemInfo()
    return render_template('index.html', system_info=system_info)