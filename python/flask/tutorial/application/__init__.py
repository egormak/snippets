from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

# Избежать циклических импортов, поэтому внизу
from application import routes
