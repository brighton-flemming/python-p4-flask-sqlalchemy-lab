#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db, render_as_batch=True)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app!</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()

    if not animal:
        return make_response('<h1>404 animal not found</h1>', 404)
    
    response_body = '''
    <html>
    <head><title>Animal Information</title></head>
    <body>
        <h1>Information about {{ animal.name }}</h1>
        <h2>Animal species of the animal above is {{ animal.species }}</h2>
        <h2>The animal's dwelling place is {{ animal.enclosure.environment }}</h2>
    </body>
    </html>
    '''

    return make_response(render_template_string(response_body, animal=animal), 200)

    

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()

    if not zookeeper:
        return make_response("<h1>404 zookeeper not found</h1>", 404)
    
    response_body = '''
    <html>
    <head><title>Zookeeper Information</title></head>
    <body>
        <h1> The name of the lad/lassie in charge is {{ zookeeper.name }}</h1>
        <h2> Fortunately, he/she was brought into this world on {{ zookeeper.birthday }}</h2>
        <h2> The animals he/she takes care of:
            <ul>
                {% for animal in zookeeper.animals %}
                    <li>{{ animal.name }}:{{animal.species}}</li>
                {% endfor %}
            </ul>
        </h2>
    </body>
    </html>
    '''

    return make_response(render_template_string(response_body, zookeeper=zookeeper), 200)


@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()

    if not enclosure:
        return make_response('<h1>404 enclosure not found</h1>', 404)
    
    response_body = '''
    <html>
    <head><title>Enclosure Information</title></head>
    <body>
        <h1>Dwelling place: {{ enclosure.environment }}</h1>
        <h2>Open To Visitors: {{ enclosure.open_to_visitors }}</h2>
        <h2>Animals that dwell here:
            <ul>
                {% for animal in enclosure.animals %}
                    <li>{{ animal.name }}: {{animal.species}}</li>
                {% endfor %}
            </ul>
        </h2>
    </body>
    </html>
    '''

    return make_response(render_template_string(response_body, enclosure=enclosure), 200)





if __name__ == '__main__':
    app.run(port=5555, debug=True)



