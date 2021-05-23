from flask import Flask, render_template
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

from models import Table


@app.route('/')
def index():
    fields = Table.query.all()
    return render_template('tables/index.html', fields=fields)


if __name__ == '__main__':
    app.run(debug=True)
