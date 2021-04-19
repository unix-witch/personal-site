from flask import Flask, render_template, send_from_directory
import os
app = Flask('app')





@app.route('/')
def index():
    return render_template("index.html")

@app.route('/misc')
def misc():
    return render_template("misc.html")

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('./favicon.ico')

app.run(host='0.0.0.0', port=8080)