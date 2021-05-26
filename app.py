import json

from flask import Flask, render_template, jsonify, request, make_response
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

from models import Table


@app.route('/', methods=['GET', 'POST'], defaults={'page': 1})
@app.route('/<int:page>', methods=['GET', 'POST'])
def index(page):
    fields = Table.query.paginate(page=page, per_page=5, error_out=False)

    if request.method == 'POST':
        condition = request.form['condition']
        column = request.form['column']
        search_value = request.form['search_value']

        if condition == 'contains' and column == 'name':
            fields = Table.query.filter(Table.name.like(search_value)).paginate(page=page, per_page=5, error_out=False)

        elif column == 'quantity':

            if condition == '=':
                fields = Table.query.filter(Table.quantity == int(search_value)).paginate(page=page, per_page=5, error_out=False)
            elif condition == '>':
                fields = Table.query.filter(Table.quantity < int(search_value)).paginate(page=page, per_page=5, error_out=False)
            elif condition == '<':
                fields = Table.query.filter(Table.quantity > int(search_value)).paginate(page=page, per_page=5, error_out=False)

        else:

            if condition == '=':
                fields = Table.query.filter(Table.distance == int(search_value)).paginate(page=page, per_page=5, error_out=False)
            elif condition == '>':
                fields = Table.query.filter(Table.distance < int(search_value)).paginate(page=page, per_page=5, error_out=False)
            elif condition == '<':
                fields = Table.query.filter(Table.distance > int(search_value)).paginate(page=page, per_page=5, error_out=False)

    return render_template('tables/index.html', fields=fields)


if __name__ == '__main__':
    app.run(debug=True)
