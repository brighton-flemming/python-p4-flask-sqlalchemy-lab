from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# metadata = MetaData(naming_convention={
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# })

metadata = MetaData(naming_convention={
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), unique=True)
    birthday = db.Column(db.Date, nullable=True)

    animals = db.relationship('Animal', backref='zookeeper')
    
    def __repr__(self):
        return f'<Zookeeper {self.name}, {self.birthday}, {self.animals.name}>'

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(300))
    open_to_visitors = db.Column(db.Boolean)

    animals = db.relationship('Animal', backref='enclosure')

    def __repr__(self):
        return f'Enclosure {self.environment}, {self.animals}'

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    species = db.Column(db.String(300))

    enclosure  = db.relationship('Enclosure', backref='animal')
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    def __repr__(self):
        return f'Animal {self.name}, {self.species}, {self.enclosure}'



