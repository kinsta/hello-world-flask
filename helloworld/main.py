
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_view():
    return render_template('index.html')
