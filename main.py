from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return form

form = """
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <p>working?</p>
        <form method='POST'>
            <label>Rotate by:</label>
            <input type='text' value='0'/>
            <textarea name='rot'>
            </textarea name='text'>
            <input type='submit' value='Encrypt!'/>
        </form>
            
    </body>
</html>
"""

app.run()