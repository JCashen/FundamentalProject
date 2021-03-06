from application import db

class Walls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.id'), nullable =False)
    nickname = db.Column(db.String(30), unique=True)
    wall_size = db.Column(db.String(30), unique=True)
    rating = db.Column(db.Float(5), nullable=True)

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wall_name = db.Column(db.String(50), nullable=False)
    county = db.Column(db.String(50), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    walls = db.relationship('Activities', backref='locations')
    
class Activities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wall_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable =False)
    activity_name =  db.Column(db.String(50), nullable=False)
    additional_equiptment = db.Column(db.Boolean, nullable=False)
    

