from flask import Flask, request, redirect
from caesar import rotate_string

import random

app = Flask(__name__)
app.config['DEBUG'] = True
textstring = ""
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/encrypt" methods='post'>
            <label>
            Rotate by:
            <input name="rot" type="text" value="0">
            </label>
            <textarea name="text" value="">{0}
            </textarea>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    crypto = request.args.get("result")
    if crypto:
        textstring = crypto
    else:
        textstring = ""
    return form.format(textstring)

@app.route("/encrypt")
def encrypt():
    text = request.args.get('text')
    rotation = request.args.get('rot')
    product = rotate_string(text,rotation)
    #return "encrypt is working"
    return redirect("/?result=" + product)

app.run()
