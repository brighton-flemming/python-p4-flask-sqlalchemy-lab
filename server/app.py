#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app!</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal,query.filter(Animal.id == id).first()

    if not animal:
        response_body = '<h1>404 animal not found</h1>'
        response = make_response(response_body, 404)
        return response
    response_body = f'''
     <h1>Information about {animal.name}</h1>
     <h2>Animal species of the animal above is {animal.species}</h2>
     <h2>The animal's dwelling place is {animal.enclosure.environment}</h2>
    '''

    response = make_response(response_body, 200)

    return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    return ''

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    return ''


if __name__ == '__main__':
    app.run(port=5555, debug=True)
